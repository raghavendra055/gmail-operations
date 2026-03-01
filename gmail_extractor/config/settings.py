import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("USER_EMAIL")
EMAIL_PASS = os.getenv("USER_PASSWORD")
IMAP_URL = "imap.gmail.com"

LOG_DIR = "logs"
OUT_DIR = "output"

MAX_BODY_LEN = 5000
