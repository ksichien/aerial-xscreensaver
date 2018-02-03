#!/bin/bash

MPV="mpv --really-quiet --shuffle --no-audio --fs --loop=inf --no-stop-screensaver --wid=${XSCREENSAVER_WINDOW} --panscan=1"

HOUR=$(date +"%H")

DAY="${HOME}/Aerial/*-day-*.mov"
NIGHT="${HOME}/Aerial/*-night-*.mov"

if [ ${HOUR} -ge 7 -a ${HOUR} -le 19 ]
then
    eval "${MPV} ${DAY}"
else
    eval "${MPV} ${NIGHT}"
fi
