import torch
from torch.package.package_importer import PackageImporter
import sounddevice as sd


model = PackageImporter("models/v5_6_ru.pt").load_pickle("tts_models", "model")


def synthesize(text: str) -> torch.Tensor:
    audio = model.apply_tts(text=text, speaker="xenia", sample_rate=48000)
    return audio


def play(audio: torch.Tensor) -> None:
    sd.play(audio.numpy(), 48000)
    sd.wait()

