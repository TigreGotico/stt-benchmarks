import os

from jiwer import wer
from json_database import JsonStorage
from ovos_utils.parse import fuzzy_match, MatchStrategy

template = """
# Language: {lang}
{rating}

## Benchmarks
{average}
{datasets}
"""
dataset_template = """

### DATASET: **{name}**

| PLUGIN                        | MODEL                          | WER                 | Damerau Similarity |
|-------------------------------|--------------------------------|---------------------|--------------------|"""
data_line = "\n| {plugin_name}         | {model}           | {wer}  | {sim} |"

formula_template = """
## PLUGIN RATING 

> **(1 - WER) * SIMILARITY * 100**

| PLUGIN | MODEL | RATING |
|--------|-------|--------|"""
r_line = "\n| {plugin_name} | {model} | {score} |"

for LANG in ["pt", "en", "ca", "gl"]:
    cv = "/home/miro/PycharmProjects/stt-benchmarks/transcripts/mozilla-foundation/common_voice_17_0"
    fl = "/home/miro/PycharmProjects/stt-benchmarks/transcripts/google/fleurs"
    gig = "/home/miro/PycharmProjects/stt-benchmarks/transcripts/speechcolab/gigaspeech"
    bracarense = "/home/miro/PycharmProjects/stt-benchmarks/transcripts/my-north-ai/cv_mls_psfb_zero_synthetic"
    libri = "/home/miro/PycharmProjects/stt-benchmarks/transcripts/facebook/multilingual_librispeech"
    libriheavy = "/home/miro/PycharmProjects/stt-benchmarks/transcripts/mythicinfinity/Libriheavy-HQ"
    ppl = "/home/miro/PycharmProjects/stt-benchmarks/transcripts/MLCommons/peoples_speech"
    vpopl = "/home/miro/PycharmProjects/stt-benchmarks/transcripts/facebook/voxpopuli"
    court = "/home/miro/PycharmProjects/stt-benchmarks/transcripts/janaab/supreme-court-speech"
    massive = "/home/miro/PycharmProjects/stt-benchmarks/transcripts/FBK-MT/Speech-MASSIVE"
    slr_ca = "/home/miro/PycharmProjects/stt-benchmarks/transcripts/projecte-aina/openslr-slr69-ca-trimmed-denoised"
    festcat = "/home/miro/PycharmProjects/stt-benchmarks/transcripts/projecte-aina/festcat_trimmed_denoised"
    frescat = "/home/miro/PycharmProjects/stt-benchmarks/transcripts/projecte-aina/LaFrescat"
    #globe = "/home/miro/PycharmProjects/stt-benchmarks/transcripts/MushanW/GLOBE"
    openslr = "/home/miro/PycharmProjects/stt-benchmarks/transcripts/openslr/openslr"
    cvpt = "/home/miro/PycharmProjects/stt-benchmarks/transcripts/my-north-ai/common_voice_pt_pt"
    mls = "/home/miro/PycharmProjects/stt-benchmarks/transcripts/DynamicSuperb/MultiLingualSpeechRecognition_MLS-pt"
    tedxbr = "/home/miro/PycharmProjects/stt-benchmarks/transcripts/dominguesm/mTEDx-ptbr"
    coraabr = "/home/miro/PycharmProjects/stt-benchmarks/transcripts/DynamicSuperb/PTBRSpeechRecognition_CORAA"

    sents = {}
    transcs = {}

    if LANG == "pt":
        datasets = [bracarense, massive, cv, fl, libri, cvpt, mls, tedxbr, coraabr]
    elif LANG == "gl":
        datasets = [cv,
                    fl,
                    openslr  # suspect it was in training data for nos
                    ]
    elif LANG == "ca":
        datasets = [cv, fl, slr_ca, festcat, frescat]
    else:
        datasets = [cv, fl, gig, ppl, vpopl, court, libriheavy]

    mkdowm = ""
    for path in datasets:
        mkdowm += dataset_template.format(name=path.split('/')[-1])

        for plugin in os.listdir(path):

            # skip suspected data used in training (WER suspiciously low)
            if (plugin == "ovos-stt-plugin-nos" and
                    path == openslr and
                    LANG == "gl"):
                continue

            for root, folders, files in os.walk(f"{path}/{plugin}"):
                for f in files:
                    if f.endswith(f"_{LANG}.json"):
                        n = f"{plugin} {f}".replace(f"_transcriptions_{LANG}.json", "")
                        if f not in sents:
                            sents[n] = []
                            transcs[n] = []
                        sentences = []
                        transcripts = []
                        data = JsonStorage(f"{root}/{f}")
                        for tx in data.values():
                            ground = tx["ground"]. \
                                replace(" <PERIOD>", "."). \
                                replace(" <COMMA>", ","). \
                                replace(" <QUESTIONMARK>", "?"). \
                                replace(" <EXCLAMATIONPOINT>", "!"). \
                                replace("<SIL>", " ").lower().strip("'.,;:!?\"").strip()
                            ts = tx["transcript"].lower().strip("'.,;:!?\"").strip()
                            if not ground or not ts:
                                continue
                            sentences.append(ground)
                            transcripts.append(ts)
                        if not sentences:
                            continue
                        score = wer(sentences, transcripts)

                        score2 = sum([fuzzy_match(t, t2, MatchStrategy.DAMERAU_LEVENSHTEIN_SIMILARITY)
                                      for t, t2 in zip(sentences, transcripts)]) / len(sentences)

                        mkdowm += data_line.format(plugin_name=plugin, wer=score, sim=score2,
                                                   model=f.replace(f"_transcriptions_{LANG}.json", ""))

                        sents[n] += sentences
                        transcs[n] += transcripts

    RATINGS = {}

    avg_mkdown = dataset_template.format(name="All datasets")
    for p in sents:
        score = wer(sents[p], transcs[p])
        score2 = sum([fuzzy_match(t, t2, MatchStrategy.DAMERAU_LEVENSHTEIN_SIMILARITY)
                      for t, t2 in zip(sents[p], transcs[p])]) / len(sents[p])
        RATINGS[p] = (1 - score) * score2 * 100

        avg_mkdown += data_line.format(plugin_name=p.split(" ")[0], wer=score, sim=score2, model=p.split(" ")[1])

    score_mkdown = formula_template
    for p in sorted(RATINGS, key=lambda k: RATINGS[k], reverse=True):
        score = min(100, max(0, RATINGS[p]))
        score_mkdown += r_line.format(score=score, plugin_name=p.split(" ")[0], model=p.split(" ")[1])

    lang_mkdowm = template.format(lang=LANG, datasets=mkdowm, rating=score_mkdown, average=avg_mkdown)

    print(lang_mkdowm)
    with open(f"{LANG}.md", "w") as f:
        f.write(lang_mkdowm)
