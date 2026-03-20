import streamlit as st
import os
from utils.speech_to_text import transcribe_audio
from utils.text_cleaner import clean_transcript
from utils.summarizer import generate_summary, convert_to_bullets
from utils.quiz_generator import generate_mcqs

st.set_page_config(page_title="Lecture Voice to Notes", layout="centered")

st.title("🎙️ Lecture Voice-to-Notes Generator")
st.write("Upload lecture audio and get structured notes using AI.")

# Create folders
if not os.path.exists("audio"):
    os.makedirs("audio")

if not os.path.exists("transcripts"):
    os.makedirs("transcripts")

uploaded_file = st.file_uploader(
    "Upload your lecture audio (.mp3 or .wav)",
    type=["mp3", "wav"]
)

MAX_FILE_SIZE_MB = 25

if uploaded_file is not None:

    if uploaded_file.size > MAX_FILE_SIZE_MB * 1024 * 1024:
        st.error("❌ File too large. Please upload under 25MB.")
    else:
        file_path = os.path.join("audio", uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success("✅ File uploaded successfully!")

        st.write("### File Details:")
        st.write("File Name:", uploaded_file.name)
        st.write("File Type:", uploaded_file.type)
        st.write("File Size (KB):", round(uploaded_file.size / 1024, 2))

        st.audio(uploaded_file)

        if st.button("🧠 Generate Transcript"):

            
            for key in list(st.session_state.keys()):
                if key.startswith("mcq_") or key == "mcqs":
                    del st.session_state[key]

            # ------------------ TRANSCRIPTION ------------------
            with st.spinner("Transcribing audio... Please wait."):
                transcript = transcribe_audio(file_path)

            cleaned_text = clean_transcript(transcript)

            transcript_path = os.path.join(
                "transcripts",
                uploaded_file.name.split(".")[0] + ".txt"
            )

            with open(transcript_path, "w", encoding="utf-8") as f:
                f.write(cleaned_text)

            st.success("✅ Transcription Complete!")

            st.subheader("Cleaned Transcript:")
            st.write(cleaned_text)

            # ------------------ SUMMARY ------------------
            st.subheader("📌 AI Summary")

            with st.spinner("Generating summary..."):
                summary = generate_summary(cleaned_text)

            st.write(summary)

            # ------------------ NOTES ------------------
            st.subheader("📋 Exam-Ready Bullet Notes")

            bullet_notes = convert_to_bullets(summary)
            st.text(bullet_notes)

            # ------------------ MCQs ------------------
            st.session_state.mcqs = generate_mcqs(summary)



if "mcqs" in st.session_state:

    st.subheader("📝 Practice MCQs")

    mcqs = st.session_state.mcqs

    for i, mcq in enumerate(mcqs):
        st.write(f"**Q{i+1}. {mcq['question']}**")

        selected = st.radio(
            "Choose an option:",
            ["Select an answer"] + mcq["options"],
            key=f"mcq_{i}"
        )

        if selected != "Select an answer":
            if selected == mcq["answer"]:
                st.success("Correct ✅")
            else:
                st.error(f"Wrong ❌ | Correct Answer: {mcq['answer']}")