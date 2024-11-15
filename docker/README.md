# Trash-Notifier Docker Container

The Trash Notifier is available here as a Docker container. You can build your own container with the files or simply use ours from the Docker Hub. You can use the compose script to specify all the important variables. You then only need the .csv file. It is important that the headings are in this format, otherwise you have to adapt the python script again.

```
Subject;Start Date;Start Time;End Date;End Time;Location;Description
```

Simply upload the .csv file to a folder on your Docker host and specify the volume mapping. Important, leave the name of the file and the path in the container the same :/app/trashcalender.csv

In test mode, the time filter is bypassed and the python script is executed every minute.

Here is the link to the Docker Hub: 
https://hub.docker.com/r/schefflerit/trash-reminder


```yaml
version: '3'
services:
  trash-reminder:
    image: schefflerit/trash-reminder
    container_name: 15_Trash-Reminder
    restart: unless-stopped
    environment:
      WEBHOOK_URL: "https://discord.com/api/webhooks/11XXXXX"
      IGNORE_SUBJECTS: ""
      ALL_NOTIFICATION_SUBJECTS: ""
      DELIMITER: ";"
      NOTIFICATION_TIME: "20:00"
#      MODE: "test"
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - /etc/timezone:/etc/timezone:ro
      - /docker/15_TrashCalender/v2/trash_calender.csv:/app/trashcalender.csv
```


Have a look, maybe we also have other interesting projects. Have a nice day and best regards SIT.