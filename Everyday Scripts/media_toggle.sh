#!/bin/bash

#mpd={ps -A | grep mpd}
if ps ax | grep -v grep | grep mpd > /dev/null
then mpc toggle && mpc="$(mpc)" && notify-send "$mpc"
else clementine --play-pause
fi
