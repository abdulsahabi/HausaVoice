# hausa_voice/tts.py

from gtts import gTTS

class HausaTTS:
    def __init__(self, lang="ha"):
        self.lang = lang

    def speak(self, text, output_path="output.mp3"):
        tts = gTTS(text=text, lang=self.lang)
        tts.save(output_path)
        return output_path
