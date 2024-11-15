#!/bin/bash

NOTIFICATION_TIME=${NOTIFICATION_TIME}


# Prüfen, ob ein Testmodus aktiv ist
if [ "$MODE" = "test" ]; then
    echo "Manual mode"
    python /app/trash_reminder.py
    sleep 60
else
    while true; do
        CURRENT_TIME=$(date +%H:%M)
        echo "$(date +%FT%H.%M) - Starting Trash reminder check... waiting for start time: $NOTIFICATION_TIME"
        if [ "$CURRENT_TIME" == "$NOTIFICATION_TIME" ]; then
            echo "Start script:"
            python /app/trash_reminder.py
            sleep 60
            exit 0
        fi
        sleep 60
    done
fi