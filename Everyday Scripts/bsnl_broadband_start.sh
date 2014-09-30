#!/bin/bash
#This script connects to BSNL broadband through the router via wlan0 interface and adjusts the routes accordingly

#Dialing BSNL Connection
sudo pppoe-start
#Deleting default gateway of my home router
sudo route del default gw 192.168.1.1
#Adding BSNL's gateway as default
sudo route add default gw 117.197.96.1
#Adding gateway to the home network router for internal LAN.
sudo route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1
#sending success notification
notify-send "BSNL Broadband Connection Started"
