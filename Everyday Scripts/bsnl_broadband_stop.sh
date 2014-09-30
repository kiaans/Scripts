#!/bin/bash
#This script ends the BSNL Broadband Connection and gets back to the default routes through wlan0 to the router.

#Hanging-up Broadband
sudo pppoe-stop
#Deleting default BSNL gateway
sudo route del default gw 117.197.96.1
#Adding home router as the default gateway
sudo route add default gw 192.168.1.1
#hang-up notification
notify-send "BSNL Broadband Connection Closed."
