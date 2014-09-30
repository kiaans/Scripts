#!/bin/bash

#mpd={ps -A | grep mpd}
if ps ax | grep -v grep | grep mpd > /dev/null
then mpc prev && mpc="$(mpc)" && notify-send "$mpc"
else clementine --previous
fi
