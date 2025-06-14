# setup.py

from setuptools import setup, find_packages

setup(
    name="hausa_voice",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "whisper",
        "gtts",
        "pydub",
    ],
    author="Sahabi Abdulrahaman",
    description="Open-source Hausa Speech-to-Text and Text-to-Speech library",
    keywords=["hausa", "speech recognition", "text to speech", "ai", "whisper", "tts", "stt"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
