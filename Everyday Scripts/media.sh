#!/bash/sh

if ps ax | grep -v grep | grep mpd > /dev/null
then mpc="$(mpc)" && notify-send "$mpc"
#else if ps ax | grep -v grep | grep clementine > /dev/null
#then notify-send "clementine running"
else clementine
fi
