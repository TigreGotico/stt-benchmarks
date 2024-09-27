import os

import soundfile as sf
from datasets import load_dataset
from json_database import JsonStorage
from ovos_stt_plugin_chromium import ChromiumSTT
from ovos_stt_plugin_fasterwhisper import FasterWhisperSTT
from ovos_stt_plugin_citrinet import CitrinetSTT
from ovos_stt_plugin_nemo import NemoSTT
from ovos_stt_plugin_mms import MMSSTT
from speech_recognition import Recognizer, AudioFile
from tqdm import tqdm  # Import tqdm for progress tracking

LANG = "en"

DL_PATH = "/run/media/miro/endeavouros/home/miro/download/"  # cache


def transcribe(wav, lang, stt) -> str:
    """Transcribe audio file using the specified STT."""
    with AudioFile(wav) as source:
        rec = Recognizer()
        audio = rec.record(source)
    try:
        transcript = stt.execute(audio, language=lang)
    except Exception as e:
        print(f"Error during transcription: {e}")  # Log the error
        transcript = ""
    return transcript


STTS = [
    #("ovos-stt-plugin-chromium", "chromium", ChromiumSTT()),
    ("ovos-stt-plugin-mms", "facebook/mms-1b-all", MMSSTT()),
    #("ovos-stt-plugin-nemo", "stt_en_quartznet15x5", NemoSTT({"lang": "en"})),
    #("ovos-stt-plugin-citrinet", "neongeckocom/stt_en_citrinet_512_gamma_0_25", CitrinetSTT({"lang": "en"})),
    #("ovos-stt-plugin-fasterwhisper", "large-v3", FasterWhisperSTT({"model": "large-v3",
    #                                                                "use_cuda": True,
    #                                                                "compute_type": "float16",
    #                                                                "beam_size": 5,
    #                                                                "cpu_threads": 12
    #                                                                }))

    # not even worth testing, they suck
    #("ovos-stt-plugin-vosk", "vosk-model-small-en-us-0.15", VoskKaldiSTT({"lang": "en"})),
    #("ovos-stt-plugin-vosk", "vosk-model-en-us-aspire-0.2", VoskKaldiSTT({"lang": "en", "large": True})),
]

DATASETS = [(ds[0],
             load_dataset(ds[0], ds[1],
                          split=ds[2],
                          streaming=ds[3],
                          trust_remote_code=True))
            for ds in [
                ("mozilla-foundation/common_voice_17_0", "en", "test", True),
                # ("mozilla-foundation/common_voice_13_0", "en", "test", True),
                ("google/fleurs", "en_us", "test", True),
                ("speechcolab/gigaspeech", "xs", "test", True),
            ]]

for d, dataset in DATASETS:
    print("Loading dataset:", d, "size:", dataset.info.dataset_size)
    print(dataset.features["audio"])
    out_path = f"{DL_PATH}/{d}"

    transcripts = []
    sentences = []

    # Using tqdm to show progress
    for sample in tqdm(dataset, desc=f"Processing {d}", unit="audio", total=dataset.info.dataset_size):
        audio_data = sample['audio']['array']  # This contains audio data
        name = sample['audio']['path']  # Original path
        # print(sample)
        ground_truth = sample.get('sentence') or sample.get("transcription") or sample.get("text")
        if not ground_truth or ground_truth in ["<OTHER>", "<MUSIC>", "<NOISE>"]:
            continue
        ground_truth = ground_truth. \
            replace(" <PERIOD>", "."). \
            replace(" <COMMA>", ","). \
            replace(" <QUESTIONMARK>", "?"). \
            replace(" <EXCLAMATIONPOINT>", "!")

        print(f"- Processing audio: {name}\nGround truth: {ground_truth}")
        for plugin_name, model, stt in STTS:
            dbp = f"{os.path.dirname(__file__)}/transcripts/{d}/{plugin_name}/{model}_transcriptions_{LANG}.json"
            os.makedirs(os.path.dirname(dbp), exist_ok=True)
            db = JsonStorage(dbp)

            if name in db:
                transcript = db[name]["transcript"]
            else:
                # Save the audio data to a WAV file
                audio_file_path = f"{out_path}/{name}.wav"
                os.makedirs(os.path.dirname(audio_file_path), exist_ok=True)
                sf.write(audio_file_path, audio_data,
                         samplerate=dataset.features["audio"].sampling_rate)
                # Transcribe the audio
                transcript = transcribe(audio_file_path, LANG, stt)

                print(f"STT: {plugin_name} Transcript: {transcript}")
            db[name] = {"ground": ground_truth, "transcript": transcript}
            db.store()

            transcripts.append(transcript.lower().strip("'\".?,!;:-_()[]{} "))
            sentences.append(ground_truth.lower().strip("'\".?,!;:-_()[]{} "))
