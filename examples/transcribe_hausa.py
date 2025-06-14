from hausa_voice.stt import HausaSTT
from hausa_voice.utils import convert_to_wav

# Convert to WAV
wav_path = convert_to_wav("audio.aac")

# Transcribe Hausa
transcriber = HausaSTT("base")
text = transcriber.transcribe(wav_path)

print("🗣️ Hausa Transcription:")
print(text)
