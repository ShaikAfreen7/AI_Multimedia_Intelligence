import os

def run_audio_autoencoder(audio_path):
    size_kb = os.path.getsize(audio_path) // 1024
    if size_kb < 50:
        return "Audio Status: Normal"
    else:
        return "Audio Status: Anomaly Detected"

