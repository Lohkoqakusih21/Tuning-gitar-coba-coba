import sounddevice as sd
import numpy as np

def capture_audio(duration, sample_rate):
    print("Recording...")

    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()

    return audio_data.flatten()

sample_rate = 44100  # Standard sample rate for audio
duration = 2  # Duration of the recording in seconds

audio_data = capture_audio(duration, sample_rate)
