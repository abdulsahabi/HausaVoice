# 📘 HausaVoice Library – Method Documentation (Draft)

---

## 🔡 transcribe_from_file(file_path: str, model_size="base", lang="ha") → str

**Purpose:**
Convert Hausa speech from a recorded audio file into text using a Speech-to-Text model like Whisper or Faster-Whisper.

**Parameters:**

- `file_path`: Path to the audio file (e.g., .wav or .aac).
- `model_size`: Whisper model variant to use (tiny, base, small, medium, large).
- `lang`: Language code (default: "ha" for Hausa).

**Returns:**

- Hausa transcription as plain text.

**Use Case:**
Used when a user uploads or records an audio message offline and wants to transcribe the Hausa speech.

---

## 🎙️ transcribe_from_mic(duration=5) → str

**Purpose:**
Capture real-time audio from a microphone, then transcribe it into Hausa text.

**Parameters:**

- `duration`: Number of seconds to record.

**Returns:**

- Hausa transcription of the recorded speech.

**Use Case:**
Used in applications where the user speaks directly into the device — such as in mobile apps or voice assistants.

---

## 🔄 transcribe_stream(stream_data) → str

**Purpose:**
Transcribe real-time audio stream data (for future live transcription features).

**Parameters:**

- `stream_data`: Streamed audio data (e.g., from socket or web mic).

**Returns:**

- Live transcribed Hausa text.

**Use Case:**
Used in scenarios like live classrooms, calls, or meetings with Hausa speakers.

---

## 🗣️ text_to_speech(text: str, lang="ha", slow=False) → None

**Purpose:**
Convert Hausa text into spoken audio using a TTS engine (like gTTS or future custom models).

**Parameters:**

- `text`: The Hausa text to convert.
- `lang`: Language code (default: "ha").
- `slow`: Speak slowly for clarity (optional).

**Returns:**

- Plays the speech or saves it depending on implementation.

**Use Case:**
Used to give AI responses in Hausa, assist with language learning, or generate audio alerts.

---

## 💾 save_to_file(text: str, filename: str, lang="ha", slow=False)

**Purpose:**
Convert Hausa text to audio and save the result as an audio file (e.g., .mp3).

**Parameters:**

- `text`: Hausa text to convert.
- `filename`: Output file name.
- `lang`: Language (default is Hausa).
- `slow`: Option to speak slowly.

**Use Case:**
Useful for generating voice messages, tutorials, or podcast segments in Hausa.

---

## 🔄 convert_to_wav(source_path: str, target_path: str = None) → str

**Purpose:**
Convert any audio file (e.g., .aac, .mp3) into `.wav` format — the format required for most STT models.

**Parameters:**

- `source_path`: Original audio file path.
- `target_path`: Optional. If not provided, the output uses the same base name with `.wav`.

**Returns:**

- Path to the converted `.wav` file.

**Use Case:**
Solves compatibility issues with STT models that only accept .wav input.

---

## 🧹 clean_transcription(text: str) → str

**Purpose:**
Clean, normalize, and optionally remove filler words or errors from raw STT output.

**Parameters:**

- `text`: Raw transcribed text.

**Returns:**

- Cleaned, human-readable Hausa text.

**Use Case:**
Useful when displaying transcriptions in apps or sending to users in messages.

---

## 💻 CLI – hausavoice

**Command Line Tool:**
A CLI that allows users to interact with HausaVoice from the terminal.

**Supported Commands:**

- `hausavoice transcribe <path>` — Transcribe Hausa speech from an audio file.
- `hausavoice speak "<text>"` — Speak or convert Hausa text to speech.
