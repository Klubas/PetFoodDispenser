#!/bin/bash

if [ "$DEBUG" -eq "1" ] then
    echo 'DEBUG'
    path=/scripts/ServoControl/src/run.py
    echo $path
    chmod a+x $path
    python3 $path
fi

path=/scripts/cronjobs.sh
echo $path
chmod a+x $path
bash $path

#keep container alive
echo 'cron -f'
cron -f