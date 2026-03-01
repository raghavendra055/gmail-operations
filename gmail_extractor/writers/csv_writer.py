import csv
import os
from datetime import datetime
from config.settings import OUT_DIR

os.makedirs(OUT_DIR, exist_ok=True)

def write_csv(rows, logger):
    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f"{OUT_DIR}/emails_{ts}.csv"

    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        writer.writerow([
            "sender",
            "receiver",
            "subject",
            "timestamp",
            "body"
        ])

        for row in rows:
            writer.writerow([
                row["sender"],
                row["receiver"],
                row["subject"],
                row["timestamp"],
                row["body"]
            ])

    logger.info(f"CSV written → {file_path}")
