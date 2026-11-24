import torch
from torch.package.package_importer import PackageImporter
import sounddevice as sd


model = PackageImporter("models/v5_6_ru.pt").load_pickle("tts_models", "model")
PAUSE = '<break time="200ms"/>'


def synthesize(ssml: str) -> torch.Tensor:
    audio = model.apply_tts(ssml_text=ssml, speaker="xenia", sample_rate=48000)
    return audio


def play(audio: torch.Tensor) -> None:
    sd.play(audio.numpy(), 48000)
    sd.wait()


def speak(phrases: list[str]) -> None:
    if not phrases:
        return
    else:
        ssml = build_ssml(phrases)
        audio = synthesize(ssml)
        play(audio)


def build_ssml(phrases: list[str]) -> str:
    body = PAUSE.join(phrases)
    return f"<speak>{body}</speak>"
