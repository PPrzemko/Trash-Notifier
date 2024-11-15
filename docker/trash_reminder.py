import csv
import datetime
import logging
import os
import requests

logging.basicConfig(filename='TrashNotify.log', level=logging.WARNING,
                    format='%(asctime)s:%(levelname)s:%(message)s', filemode='a')


def send_webhook_message(message, webhook_url):
    data = {"content": message}

    response = requests.post(webhook_url, json=data)

    if response.status_code == 204:
        message = f"Discord notification sent successfully! : {message}"
        print(message)
        logging.info(message)
    else:
        message = f"Failed to send Discord notification. Status code: {response.status_code} : {message}"
        print(message)
        logging.warning(message)


def current_year_match(start_date, current_date, webhook_url) -> bool:
    if start_date.year != current_date.year:
        message = f"Achtung: CSV fehler. Jahr in CSV entspricht nicht dem Aktuellen. current_date {current_date}, csv_date {start_date}"
        send_webhook_message(message, webhook_url)
        logging.error(message)
        return False
    return True


def check_and_send_reminders(csv_file, delimiter, webhook_url):
    with open(csv_file, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter)
        print(f"Delimiter: {delimiter}")
        print(f"CSV Headers: {reader.fieldnames}")
        for row in reader:
            print(f"Processing row: {row}")
            subject = row['Subject']
            start_date = row['Start Date']
            start_time = row['Start Time']
            end_date = row['End Date']
            end_time = row['End Time']
            location = row['Location']
            # description = row['Description'] #sucks because icorrect message. PUT OUT TRASH TODAY!
            description = f"{subject} heute rausstellen. Wird morgen abgeholt."
            try:
                start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
            except ValueError as ve:
                print(f"Invalid date format in row: {row}. Error: {ve}")
                continue
            # Because notification should be sent one day before Trash collection
            notification_date = start_date - datetime.timedelta(days=1)
            print (f"Notification_Date: {notification_date}")
            current_date = datetime.datetime.now().date()

            if not current_year_match(start_date, current_date, webhook_url): break
            ignore_subjects = os.getenv("IGNORE_SUBJECTS", [])
            if subject in ignore_subjects: continue
            if notification_date == current_date: send_webhook_message(f"@everyone Erinnerung: {description}", webhook_url)


def main():
    webhook_url = os.getenv("WEBHOOK_URL")
    csv_file_path = "/app/trashcalender.csv"
    delimiter = os.getenv("DELIMITER")
    print ("Script running")
    check_and_send_reminders(csv_file_path, delimiter, webhook_url)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.exception("main crashed. Error: %s", e)