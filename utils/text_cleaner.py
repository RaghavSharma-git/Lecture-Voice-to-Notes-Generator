import re

def clean_transcript(text):
   
    fillers = ["uh", "umm", "you know", "like", "okay"]
    
    for word in fillers:
        text = re.sub(rf"\b{word}\b", "", text, flags=re.IGNORECASE)

    
    text = re.sub(r"\s+", " ", text)

   
    text = re.sub(r"\. ", ".\n\n", text)

    return text.strip()
