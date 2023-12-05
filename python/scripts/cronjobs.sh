#!/bin/bash

crontab -r 2> /dev/null

if [ "$ENABLE_CRON_JOB" -eq "1" ]
then
  (            echo "00 06   * * *   root /scripts/ServoControl/src/run.py") | crontab - 
  (crontab -l; echo "00 09   * * *   root /scripts/ServoControl/src/run.py") | crontab -
  (crontab -l; echo "00 12   * * *   root /scripts/ServoControl/src/run.py") | crontab -
  (crontab -l; echo "00 15   * * *   root /scripts/ServoControl/src/run.py") | crontab -
  (crontab -l; echo "00 18   * * *   root /scripts/ServoControl/src/run.py") | crontab -
  (crontab -l; echo "00 21   * * *   root /scripts/ServoControl/src/run.py") | crontab -
fi

crontab -l