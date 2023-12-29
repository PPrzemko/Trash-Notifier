# Trash-Reminder
This Python script serves as a reminder tool for upcoming trash collection events based on a CSV file schedule. It sends Discord notifications through a webhook to keep users informed about scheduled trash pickups. The script also includes a safeguard to notify users if the CSV file is for the previous or upcoming year.

## Usage
### 1. Clone the Repository:

`git clone https://github.com/PPrzemko/Trash-Notifier.git`

### 2. Install Dependencies:
`pip install -r requirements.txt`
### 3. Configure Script:
Rename .env.example file and edit it:

- WEBHOOK_URL= Discord Webhook URL 
- IGNORE_SUBJECTS=["Biotonne"] #Cant yet ignore Sonderabfall - leave empty if all should be sent
- ALL_NOTIFICATION_SUBJECTS = ["Restmüll + Gelber-Sack", "Papiertonne", "Biotonne", "Gelber-Sack", "Sonderabfall Abgabestelle"]
- CSV_FILE_PATH=Reichelsheim-Reichelsheim-2024.csv # URL to get the CSV: https://www.reso-gmbh.de/abfuhrplaene/ ( german Excel (Semicolon separated))

### 4. Configure Crontab:
Edit your crontab file using the crontab -e command and add the following line to run the script at your desired frequency. 
For example, to run the script every day at 3:00pm

0 15 * * * /path/to/python3 /path/to/your-repository/trash_reminder.py
Make sure to replace /path/to/python3 and /path/to/your-repository with the actual paths on your system.

### 5. Run the Script Manually:
You can also run the script manually to check for upcoming trash collection events without waiting for the cron job.



## Script Details
The script logs information to a file named TrashNotify.log.
Discord notifications are sent using a webhook when the specified trash collection event is approaching.
If an error occurs during execution, details are logged, and a notification is sent to Discord.
Feel free to modify and extend the script to adapt it for different schedules.

## Disclaimer
This script is provided as-is, and the maintainers are not responsible for any issues or misuse. Use it responsibly and ensure compliance with local waste management regulations.