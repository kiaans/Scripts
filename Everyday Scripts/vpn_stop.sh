#!/bin/bash

sudo pptpsetup --delete bfvpn
sudo route del default gw 10.88.1.1
sudo route add default gw 10.100.91.4
sudo killall -HUP pppd
notify-send "Cyberoam By-Passing Stopped. Back  to Normal!"
