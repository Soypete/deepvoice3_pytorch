import os
import hparams
import json
import synthesis
import train
from os.path import exists, join, expanduser
from deepvoice3_pytorch import frontend

preset = "20180505_deepvoice3_ljspeech.json"
checkpoint_path = "20180505_deepvoice3_checkpoint_step000640000.pth"
# text = "test test test"

# Load parameters from preset
with open(preset) as f:
  hparams.hparams.parse_json(f.read())
  
# Inject frontend text processor
synthesis._frontend = getattr(frontend, "en")
train._frontend =  getattr(frontend, "en")

# alises
fs = hparams.hparams.sample_rate
hop_length = hparams.hparams.hop_size

def tts(model, text, p=0, speaker_id=None, fast=True, figures=True):
  from synthesis import tts as _tts
  waveform, alignment, spectrogram, mel = _tts(model, text, p, speaker_id, fast)
#   if figures:
    #   visualize(alignment, spectrogram)
  IPython.display.display(Audio(waveform, rate=fs))
  
# def visualize(alignment, spectrogram):
#   label_fontsize = 16
#   figure(figsize=(16,16))

#   subplot(2,1,1)
#   imshow(alignment.T, aspect="auto", origin="lower", interpolation=None)
#   xlabel("Decoder timestamp", fontsize=label_fontsize)
#   ylabel("Encoder timestamp", fontsize=label_fontsize)
#   colorbar()

#   subplot(2,1,2)
#   librosa.display.specshow(spectrogram.T, sr=fs, 
#                            hop_length=hop_length, x_axis="time", y_axis="linear")
#   xlabel("Time", fontsize=label_fontsize)
#   ylabel("Hz", fontsize=label_fontsize)
#   tight_layout()
#   colorbar()

from train import build_model
from train import restore_parts, load_checkpoint

model = build_model()
model = load_checkpoint(checkpoint_path, model, None, True)

print(idx, "test test test")
tts(model, "test test test", figures=False