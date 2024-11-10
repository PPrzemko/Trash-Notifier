# Beta status, there are still some bugs...

In test mode, the time filter is bypassed and the python script is executed every minute.

```yaml
version: '3'
services:
  trash-reminder:
    image: trash-reminder
    container_name: 15_Trash-Reminder
    restart: unless-stopped
    environment:
      WEBHOOK_URL: "https://discord.com/api/webhooks/119XXXX"
      IGNORE_SUBJECTS: ""
      ALL_NOTIFICATION_SUBJECTS: ""
      DELIMITER: ";"
      NOTIFICATION_TIME: "10:00"
#      MODE: "test"
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - /etc/timezone:/etc/timezone:ro
      - /docker/15_TrashCalender/v2/trash_calender.csv:/app/trashcalender.csv
    networks:
      trashreminder-net:
        ipv4_address: 172.18.15.11

networks:
  trashreminder-net:
    driver: bridge
    ipam:
      config:
        - subnet: 172.18.15.0/24
          gateway: 172.18.15.1
```