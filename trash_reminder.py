import csv
import datetime
import logging
import os
import requests
from dotenv import load_dotenv

logging.basicConfig(filename='TrashNotify.log', level=logging.WARNING,
                    format='%(asctime)s:%(levelname)s:%(message)s', filemode='a')
load_dotenv()


def send_webhook_message(message, webhook_url):
    data = {"content": message}

    response = requests.post(webhook_url, json=data)

    if response.status_code == 204:
        message = "Discord notification sent successfully!"
        print(message)
        logging.info(message)
    else:
        message = f"Failed to send Discord notification. Status code: {response.status_code}"
        print(message)
        logging.warning(message)


def current_year_match(start_date, current_date, webhook_url) -> bool:
    if start_date.year < current_date.year:
        message = f"Achtung: CSV von dem Vorjahr erkannt."
        send_webhook_message(message, webhook_url)
        return False
    elif start_date.year > current_date.year:
        message = f"Achtung: CSV fürs neue Jahr erkannt."
        send_webhook_message(message, webhook_url)
        return False
    return True


def check_and_send_reminders(csv_file, webhook_url):
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            subject = row['Subject']
            start_date = row['Start Date']
            start_time = row['Start Time']
            end_date = row['End Date']
            end_time = row['End Time']
            location = row['Location']
            description = row['Description']

            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
            # Because notification should be sent one day before Trash collection
            notification_date = start_date - datetime.timedelta(days=1)
            current_date = datetime.datetime.now().date()

            if not current_year_match(start_date, current_date, webhook_url): break
            ignore_subjects = os.getenv('IGNORE_SUBJECTS', [])
            if subject in ignore_subjects: continue
            if notification_date == current_date: send_webhook_message(f"@everyone Erinnerung: {description}", webhook_url)


def main():
    # Beispielaufruf der Funktion mit der CSV-Datei
    webhook_url = os.getenv('WEBHOOK_URL', "") or logging.exception("NO WEBHOOK URL FOUND IN ENV FILE")
    csv_file_path = os.getenv('CSV_FILE_PATH', "") or logging.exception("NO CSV PATH URL FOUND IN ENV FILE")
    check_and_send_reminders(csv_file_path, webhook_url)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.exception("main crashed. Error: %s", e)
