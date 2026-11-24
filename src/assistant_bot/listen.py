import json
import queue
import sounddevice as sd
from vosk import KaldiRecognizer, Model, SetLogLevel


SAMPLE_RATE = 16000
MODEL_PATH = "models/vosk-model-small-ru-0.22"

SetLogLevel(-1)
model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, SAMPLE_RATE)
chunks: queue.Queue[bytes] = queue.Queue()


def on_audio(data, frames, time, status) -> None:
    chunks.put(bytes(data))


def listen() -> str:
    with sd.RawInputStream(
        samplerate=SAMPLE_RATE,
        blocksize=8000,
        dtype="int16",
        channels=1,
        callback=on_audio,
    ):
        while True:
            if recognizer.AcceptWaveform(chunks.get()):
                text = json.loads(recognizer.Result())["text"]
                if text:
                    return text
