🎙️ AI-Powered Lecture Voice-to-Notes Generator

An AI-based web application that converts lecture audio into structured study material including cleaned transcripts, AI-generated summaries, exam-ready bullet notes, and interactive MCQs.

Built using Speech Recognition + NLP + Streamlit.

🚀 Features

🎧 Upload lecture audio (.mp3 / .wav)

🧠 Speech-to-text using OpenAI Whisper

🧹 Automatic transcript cleaning

📌 AI-powered summary generation

📋 Exam-ready bullet notes

📝 Interactive MCQs for practice

🌐 Clean web interface using Streamlit

🏗️ System Architecture

Audio Input
↓
Whisper (Speech-to-Text)
↓
Text Cleaning (Regex-based NLP)
↓
Transformer-based Summarization
↓
Bullet Note Conversion
↓
MCQ Generation

🛠️ Tech Stack
Frontend

Streamlit

Backend

Python

AI / NLP

OpenAI Whisper (Speech Recognition)

HuggingFace Transformers (Summarization)

Torch

Regex (Text Cleaning)

📂 Project Structure
lecture-voice-to-notes/
│
├── app.py
├── requirements.txt
│
├── audio/
├── transcripts/
│
└── utils/
    ├── speech_to_text.py
    ├── text_cleaner.py
    ├── summarizer.py
    └── quiz_generator.py
⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/lecture-voice-to-notes.git
cd lecture-voice-to-notes
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Install FFmpeg (Required for Whisper)

Download FFmpeg from:
https://www.gyan.dev/ffmpeg/builds/

Add bin folder to system PATH.

Verify:

ffmpeg -version
5️⃣ Run Application
streamlit run app.py
📊 How It Works

User uploads lecture audio

Whisper converts speech → text

Transcript is cleaned

Transformer model generates summary

Summary converted into bullet notes

MCQs generated dynamically

User interacts with quiz

🎯 Use Cases

Students who struggle with note-taking

Quick revision from long lectures

Self-assessment using generated MCQs

Educational AI experimentation

⚠️ Limitations

MCQs are rule-based (not fully semantic)

Very long audio may slow processing

Performance depends on hardware

Accuracy depends on audio quality

🔮 Future Improvements

Intelligent MCQ generation using LLMs

Difficulty selection for quizzes

Multilingual support

Live lecture recording

Score tracking dashboard

Cloud deployment

📸 Screenshots

(Add screenshots of your app here)

🔗 Deployment

Streamlit Cloud / Local Deployment

📚 References

OpenAI Whisper Documentation

HuggingFace Transformers Documentation

Streamlit Documentation

Python Official Documentation

👨‍💻 Author

Raghav Sharma
BCA Student
AI & NLP Enthusiast