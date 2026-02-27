import re

def clean_transcript(text):
    # Remove filler words
    fillers = ["uh", "umm", "you know", "like", "okay"]
    
    for word in fillers:
        text = re.sub(rf"\b{word}\b", "", text, flags=re.IGNORECASE)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Add paragraph breaks after periods
    text = re.sub(r"\. ", ".\n\n", text)

    return text.strip()