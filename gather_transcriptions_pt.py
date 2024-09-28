import os
import random
import soundfile as sf
from datasets import load_dataset
from json_database import JsonStorage
from ovos_stt_plugin_chromium import ChromiumSTT
from ovos_stt_plugin_citrinet import CitrinetSTT
from ovos_stt_plugin_fasterwhisper import FasterWhisperSTT
from ovos_stt_plugin_mms import MMSSTT
from speech_recognition import Recognizer, AudioFile
from tqdm import tqdm  # Import tqdm for progress tracking
from ovos_stt_plugin_server import OVOSHTTPServerSTT

LANG = "pt"

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
    #("ovos-stt-plugin-mms", "facebook/mms-1b-all", MMSSTT()),
    ("ovos-stt-plugin-citrinet", "neongeckocom/stt_pt_citrinet_512_gamma_0_25", CitrinetSTT({"lang": "pt"})),

    # ("ovos-stt-plugin-fasterwhisper", "large-v3", FasterWhisperSTT({"model": "large-v3",
    #                                                                "use_cuda": True,
    #                                                                "compute_type": "float16",
    # ("ovos-stt-plugin-fasterwhisper", "tiny", FasterWhisperSTT({"model": "tiny",
    #("ovos-stt-plugin-fasterwhisper", "small", FasterWhisperSTT({"model": "small",
    #                   "beam_size": 5,
    #                   "cpu_threads": 4
    #                   })),
    #("ovos-stt-plugin-fasterwhisper", "large-v2", OVOSHTTPServerSTT({"url": "http://0.0.0.0:8080/stt"})),
   # ("ovos-stt-plugin-fasterwhisper-zuazo", "whisper-small-pt",
   #  FasterWhisperSTT({"model": "Jarbas/faster-whisper-small-pt-cv13",
   # ("ovos-stt-plugin-fasterwhisper", "faster-whisper-small-pt-MyNorthAI",
   #  FasterWhisperSTT({"model": "Jarbas/faster-whisper-small-pt-MyNorthAI",
   #                    "beam_size": 5,
   #                    "cpu_threads": 4
   #                    }))
]

DATASETS = [(ds[0],
             load_dataset(ds[0], ds[1],
                          split=ds[2],
                          streaming=ds[3],
                          trust_remote_code=True))
            for ds in [
                ("my-north-ai/common_voice_pt_pt", "default", "test", True),  # pt-pt
                ("DynamicSuperb/PTBRSpeechRecognition_CORAA", "default", "test", True),  # pt-br
                ("DynamicSuperb/MultiLingualSpeechRecognition_MLS-pt", "default", "test", True),  # pt-br
                ("dominguesm/mTEDx-ptbr", "default", "test", True),  # pt-br
                ("my-north-ai/cv_mls_psfb_zero_synthetic", "default", "test_bracarense", True),  # pt-pt
                ("FBK-MT/Speech-MASSIVE", "pt-PT", "validation", True),  # pt-pt
                ("google/fleurs", "pt_br", "test", True),  # pt-br
                ("facebook/multilingual_librispeech", "portuguese", "test", True), # mainly pt-br , some pt-pt
                ("mozilla-foundation/common_voice_17_0", "pt", "test", True),  # mainly pt-br , some pt-pt
            ]]

#random.shuffle(DATASETS)
for d, dataset in DATASETS:
    print("Loading dataset:", d, "size:", dataset.info.dataset_size)
    print(dataset.features["audio"])
    out_path = f"{DL_PATH}/{d}"

    # Using tqdm to show progress
    for sample in tqdm(dataset, desc=f"Processing {d}", unit="audio", total=dataset.info.dataset_size):
        audio_data = sample['audio']['array']  # This contains audio data
        name = sample['audio']['path']  # Original path
        # print(sample)
        ground_truth = (sample.get('sentence') or
                        sample.get("transcript") or
                        sample.get("transcription") or
                        sample.get("utt") or
                        sample.get("normalized_text") or
                        sample.get("text") or
                        sample.get("text_original") or
                        sample.get("text_transcription") or
                        sample.get("voice_text") or
                        sample.get("label"))
        if not ground_truth or ground_truth in ["<OTHER>", "<MUSIC>", "<NOISE>", "<SIL>"]:
            continue
        ground_truth = ground_truth. \
            replace(" <PERIOD>", "."). \
            replace(" <COMMA>", ","). \
            replace(" <QUESTIONMARK>", "?"). \
            replace(" <EXCLAMATIONPOINT>", "!"). \
            replace("<SIL>", " ")

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
                         samplerate=dataset.features["audio"].sampling_rate or 16000)
                # Transcribe the audio
                transcript = transcribe(audio_file_path, LANG, stt)

                print(f"STT: {plugin_name} Transcript: {transcript}")
            db[name] = {"ground": ground_truth, "transcript": transcript}
            db.store()
