import imaplib
import email
from datetime import datetime, timedelta
from config.settings import IMAP_URL

def connect(user, password, logger):
    con = imaplib.IMAP4_SSL(IMAP_URL)
    con.login(user, password)
    con.select("INBOX")
    logger.info("Connected to IMAP")
    return con

def search_last_n_hours(con, hours, logger):
    since = (datetime.now() - timedelta(hours=hours)).strftime("%d-%b-%Y")
    status, data = con.search(None, f'(SINCE "{since}")')
    logger.info(f"Found {len(data[0].split())} emails since {since}")
    return data[0].split()

def fetch_messages(con, ids, logger):
    messages = []
    for eid in ids:
        _, data = con.fetch(eid, "(RFC822)")
        messages.append(email.message_from_bytes(data[0][1]))
    logger.info(f"Fetched {len(messages)} emails")
    return messages
