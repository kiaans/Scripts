#!/bin/bash

#mpd={ps -A | grep mpd}
if ps ax | grep -v grep | grep mpd > /dev/null
then mpc stop
else clementine --stop
fi
