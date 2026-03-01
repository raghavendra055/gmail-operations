import re
from bs4 import BeautifulSoup
from config.settings import MAX_BODY_LEN

def extract_body(msg, logger):
    html = None

    for part in msg.walk():
        if part.get_content_type() == "text/html":
            payload = part.get_payload(decode=True)
            if payload:
                html = payload.decode(errors="ignore")
                break

    if not html:
        logger.warning("No HTML body found")
        return ""

    soup = BeautifulSoup(html, "lxml")

    for tag in soup(["script", "style", "head", "meta", "link", "img", "svg"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    text = re.sub(r"\s+", " ", text)

    logger.info(f"Email body cleaned | length={len(text)}")
    return text[:MAX_BODY_LEN]
