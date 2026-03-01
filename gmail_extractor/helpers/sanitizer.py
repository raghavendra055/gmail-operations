import re

def sanitize_for_csv(text: str) -> str:
    if not text:
        return ""
    text = text.replace("\x00", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()
