import email.utils
from config.settings import EMAIL_USER, EMAIL_PASS
from helpers.logger import setup_logger
from helpers.tracer import trace
from helpers.sanitizer import sanitize_for_csv
from helpers.mail_parser import extract_body
from services.imap_service import connect, search_last_n_hours, fetch_messages
from writers.csv_writer import write_csv

logger = setup_logger()
trace = trace(logger)

@trace
def parse_email(msg):
    return {
        "sender": email.utils.parseaddr(msg.get("From"))[1],
        "receiver": email.utils.parseaddr(msg.get("To"))[1],
        "subject": sanitize_for_csv(msg.get("Subject", "")),
        "timestamp": sanitize_for_csv(msg.get("Date", "")),
        "body": sanitize_for_csv(extract_body(msg, logger))
    }

@trace
def main():
    con = connect(EMAIL_USER, EMAIL_PASS, logger)
    ids = search_last_n_hours(con, hours=72, logger=logger)
    msgs = fetch_messages(con, ids, logger)

    rows = [parse_email(msg) for msg in msgs]

    if rows:
        write_csv(rows, logger)
    else:
        logger.warning("No emails found")

    con.logout()
    logger.info("IMAP connection closed")

if __name__ == "__main__":
    main()
