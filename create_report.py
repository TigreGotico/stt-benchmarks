import os

from jiwer import wer
from json_database import JsonStorage
from ovos_utils.parse import fuzzy_match, MatchStrategy

PATH = "/home/miro/.local/share/transcripts"


def get_sim(ground, sents):
    s = sum([fuzzy_match(t, t2, MatchStrategy.DAMERAU_LEVENSHTEIN_SIMILARITY)
             for t, t2 in zip(ground, sents)]) / len(sents)
    return s


LANG2DATASET = {
    "pt-pt": [f"{PATH}/my-north-ai/common_voice_pt_pt",
              f"{PATH}/my-north-ai/cv_mls_psfb_zero_synthetic",
              f"{PATH}/FBK-MT/Speech-MASSIVE"
              ],
    "pt-br": [f"{PATH}/google/fleurs",
              f"{PATH}/PolyAI/minds14",
              f"{PATH}/dominguesm/mTEDx-ptbr",
              f"{PATH}/DynamicSuperb/PTBRSpeechRecognition_CORAA",
              f"{PATH}/DynamicSuperb/MultiLingualSpeechRecognition_MLS-pt",
              f"{PATH}/facebook/multilingual_librispeech"],
    "pt": [f"{PATH}/mozilla-foundation/common_voice_17_0",
           f"{PATH}/google/fleurs",
           f"{PATH}/PolyAI/minds14",
           f"{PATH}/my-north-ai/common_voice_pt_pt",  # TODO - benchmark for pt-pt
           f"{PATH}/my-north-ai/cv_mls_psfb_zero_synthetic",  # TODO - benchmark for pt-pt
           f"{PATH}/FBK-MT/Speech-MASSIVE",  # TODO - benchmark for pt-pt
           f"{PATH}/dominguesm/mTEDx-ptbr",
           f"{PATH}/DynamicSuperb/PTBRSpeechRecognition_CORAA",
           f"{PATH}/DynamicSuperb/MultiLingualSpeechRecognition_MLS-pt",
           f"{PATH}/facebook/multilingual_librispeech"],
    "gl": [f"{PATH}/openslr/openslr",
           f"{PATH}/google/fleurs",
           f"{PATH}/mozilla-foundation/common_voice_17_0"],
    "ca": [f"{PATH}/projecte-aina/openslr-slr69-ca-trimmed-denoised",
           f"{PATH}/projecte-aina/festcat_trimmed_denoised",
           f"{PATH}/projecte-aina/LaFrescat",
           f"{PATH}/google/fleurs",
           f"{PATH}/mozilla-foundation/common_voice_17_0"],
    "en": [f"{PATH}/openslr/openslr",
           f"{PATH}/PolyAI/minds14",
           f"{PATH}/LIUM/tedlium",
           f"{PATH}/edinburghcstr/ami",
           f"{PATH}/edinburghcstr/edacc",  # TODO - benchmark for foreign accent
           f"{PATH}/speechcolab/gigaspeech",
           f"{PATH}/MLCommons/peoples_speech",
           f"{PATH}/facebook/voxpopuli",
           f"{PATH}/janaab/supreme-court-speech",
           f"{PATH}/mythicinfinity/Libriheavy-HQ",
           f"{PATH}/google/fleurs",
           f"{PATH}/mozilla-foundation/common_voice_17_0"]
}


def read_dbs(lang):
    SCORES = {}
    DATA = {}
    for path in LANG2DATASET[lang]:
        for plugin in os.listdir(path):
            for root, folders, files in os.walk(f"{path}/{plugin}"):
                for f in files:
                    l2 = lang.split("-")[0]
                    if f.endswith(f"_{l2}.json"):
                        model = f.split(f"_transcriptions_{l2}.json")[0]

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
                            if not tx.get("transcript", ""):
                                continue
                            ts = tx.get("transcript").lower().strip("'.,;:!?\"").strip()
                            if not ground or not ts:
                                continue
                            sentences.append(ground)
                            transcripts.append(ts)
                            if plugin not in DATA:
                                DATA[plugin] = {}
                            if model not in DATA[plugin]:
                                DATA[plugin][model] = {}
                            if path not in DATA[plugin][model]:
                                DATA[plugin][model][path] = []
                            DATA[plugin][model][path].append((ground, ts))
                        if not sentences:
                            continue
                        score = wer(sentences, transcripts)
                        score2 = sum([fuzzy_match(t, t2, MatchStrategy.DAMERAU_LEVENSHTEIN_SIMILARITY)
                                      for t, t2 in zip(sentences, transcripts)]) / len(sentences)
                        if plugin not in SCORES:
                            SCORES[plugin] = {}
                        if model not in SCORES[plugin]:
                            SCORES[plugin][model] = {}
                        if path not in SCORES[plugin][model]:
                            SCORES[plugin][model][path] = {}
                        SCORES[plugin][model][path] = {"wer": score, "similarity": score2}
    return SCORES, DATA


def calc_scores(data):
    # calc global across datasets
    RATINGS = {}
    WER = {}
    SIM = {}
    for plugin, dt in data.items():
        if plugin not in RATINGS:
            RATINGS[plugin] = {}
        if plugin not in WER:
            WER[plugin] = {}
        if plugin not in SIM:
            SIM[plugin] = {}
        for model, dt2 in dt.items():
            if model not in RATINGS[plugin]:
                RATINGS[plugin][model] = {}
            if plugin not in WER[plugin]:
                WER[plugin][model] = {}
            if plugin not in SIM[plugin]:
                SIM[plugin][model] = {}

            for path, data in dt2.items():
                txs = [d[0] for d in data]
                sentences = [d[1] for d in data]
                if not sentences:
                    continue
                score = wer(sentences, txs)
                score2 = sum([fuzzy_match(t, t2, MatchStrategy.DAMERAU_LEVENSHTEIN_SIMILARITY)
                              for t, t2 in zip(sentences, txs)]) / len(sentences)
                RATINGS[plugin][model][path] = (1 - score) * score2 * 100
                WER[plugin][model][path] = score
                SIM[plugin][model][path] = score2

    return RATINGS, WER, SIM


def per_plugin_markdown(scores):
    for plugin in scores:
        mkdown = ""
        mkdown += f"\n# WER: {plugin}"
        rows = []
        columns = ["dataset/model"]
        values = {}

        for model in scores[plugin]:
            values[model] = {}
            if model not in columns:
                columns.append(model)
            for path, data in scores[plugin][model].items():
                dataset = path.split("/")[-1]
                if dataset not in rows:
                    rows.append(dataset)
                values[model][dataset] = data

        mkdown += "\n|" + "|".join(columns) + "|"
        mkdown += "\n|" + "|".join(["-"] * len(columns)) + "|\n"

        lines = []

        for dataset in rows:
            line = f"| {dataset} "
            for model in columns[1:]:
                val = values[model].get(dataset)
                if val:
                    if isinstance(val, float):
                        line += f"| {round(val, 4)} "
                    else:
                        line += f"| {round(val['wer'], 4)} "
                else:
                    line += f"| N/A "
            lines.append(line + "|")

        lines = sorted(lines, key=lambda k: k.split("|")[2])
        mkdown += "\n".join(lines)
        yield plugin, mkdown


def plugin_ranking_markdown(data):
    mkdown = "|Plugin|Model|WER<br>(all samples)| WER<br>(average across datasets) | Damerau Similarity | Score |\n"
    mkdown += "|-----|-----|--------------------|----------------------------------|--------------------|-------|\n"
    rows = []
    for plugin in data:
        for model in data[plugin]:
            ground = []
            sents = []
            wers = []

            for _, dataset in data[plugin][model].items():
                ground += [s[0] for s in dataset]
                sents += [s[1] for s in dataset]
                wers.append(wer([s[0] for s in dataset],
                                [s[1] for s in dataset]))

            avg_w = sum(wers) / len(wers)

            total_w = wer(ground, sents)
            s = get_sim(ground, sents)

            werc = 1 - (total_w + avg_w) / 2
            score = werc * s * 100

            line = f"| {plugin} | {model} | {round(total_w, 4)} | {round(avg_w, 4)} | {round(s, 4)} | {round(score, 4)} |"

            rows.append((line, score))

    rows = sorted(rows, key=lambda k: k[1], reverse=True)
    rows = [r[0] for r in rows]
    mkdown += "\n".join(rows)

    return mkdown


if __name__ == "__main__":

    for LANG in ["pt-pt", "pt-br", "pt", "en", "ca", "gl"]:
        SCORES, DATA = read_dbs(LANG)

        rank = plugin_ranking_markdown(DATA)

        with open(f"ranked_plugins_{LANG}.md", "w") as f:
            f.write(rank)

        reports = []
        for plug, mkdown in per_plugin_markdown(SCORES):
            reports.append(mkdown)
            with open(f"{plug}_{LANG}.md", "w") as f:
                f.write(mkdown)

        with open(f"plugins_{LANG}.md", "w") as f:
            f.write("\n\n".join(reports))
