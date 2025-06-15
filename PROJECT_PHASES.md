# HausaVoice – Project Development Phases 🎧🇳🇴

HausaVoice is an open-source voice AI project focused on building accurate and accessible **Hausa Speech-to-Text (STT)** and **Text-to-Speech (TTS)** tools, optimized for real-world use, especially in CPU-based environments.

---

## ✅ Phase 1: Environment Setup + Core Dependency Installation

- [x] Initialize project repo and folder structure
- [x] Create virtual environment (`venv`)
- [x] Install required core packages:

  - `faster-whisper` (STT engine)
  - `gTTS` (Google TTS engine)
  - `ffmpeg-python` (for audio conversion)
  - `pydub` (audio manipulation)
  - `python-dotenv`, `typer`, others as needed

- [x] Setup `.gitignore`, `requirements.txt`, and initial backend script

---

## ✅ Phase 2: Core Method Documentation & Planning

- [x] Create `methods.md` to define project functionalities
- [x] Finalize backend engine preference: **using `faster-whisper`**
- [x] Outline CLI command strategy
- [x] Plan for optimized CPU-only execution (no GPU required)

---

## 🧠 Phase 3: Method-by-Method Implementation

This phase focuses on **implementing and testing core methods**:

- [ ] `transcribe_audio()` – Transcribe Hausa audio files to text using `faster-whisper`
- [ ] `generate_tts()` – Convert Hausa text to audio using `gTTS` or later, `Coqui`
- [ ] `convert_audio()` – Convert `.aac` to `.wav` for model compatibility
- [ ] `batch_transcribe()` – Process multiple audio files at once
- [ ] `benchmark_model()` – Evaluate model speed and quality
- [ ] CLI integration for all core methods

---

## 💡 Phase 4: CLI Prototype & Simple Runner

- [ ] Build CLI runner using `typer`
- [ ] Accept file input or mic capture
- [ ] Print STT text or play TTS audio
- [ ] Include logs and error handling

---

## 🌍 Phase 5: Dataset Collection & Fine-Tuning Preparation

- [ ] Collect Hausa voice samples (your own or public datasets)
- [ ] Transcribe and label them for supervised learning
- [ ] Plan fine-tuning or model training with `faster-whisper`
- [ ] Save/export checkpoints and prep for open-source release

---

## 💼 Future Phases

- [ ] Create public API for developers
- [ ] Integrate HausaVoice into schools/services
- [ ] Build Hausa-first AI products and mobile apps

---

**HausaVoice is a library and developer-first tool.** We aim to build something others can install, run, and contribute to. Your dream of an accessible Hausa voice AI ecosystem is already becoming reality.
