#!/bin/bash

#mpd={ps -A | grep mpd}
if ps ax | grep -v grep | grep mpd > /dev/null
then mpc next && mpc="$(mpc)" && notify-send "$mpc"
else clementine --next
fi
