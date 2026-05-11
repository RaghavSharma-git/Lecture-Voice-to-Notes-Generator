from transformers import pipeline

# Load model once globally (important for performance)
summarizer_model = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text):
    # Limit input size (BART can't handle extremely long text)
    max_input_length = 1024
    text = text[:max_input_length]

    summary = summarizer_model(
        text,
        max_length=150,
        min_length=40,
        do_sample=False
    )

    return summary[0]["summary_text"]

def convert_to_bullets(text):
    sentences = text.split(". ")
    bullets = []

    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) > 20:
            bullets.append(f"- {sentence}")

    return "\n".join(bullets)