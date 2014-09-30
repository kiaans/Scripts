#!/bin/bash
#sudo route add -net 10.100.0.0 netmask 255.255.0.0 gw 10.100.91.4

touch /tmp/bfvpn
touch /tmp/pass.txt
wget --referer "http://www.bfvpn.com/free-vpn-account/" http://www.bfvpn.com/free-vpn-service/bestfreevpn.gif?$(date +%s) -O /tmp/bfvpn -q
tesseract /tmp/bfvpn /tmp/pass > /dev/null
sudo pptpsetup --create bfvpn --server bestfreevpn.com --username free --password $(cat /tmp/pass.txt) --encrypt --start
sudo route del default gw 10.100.91.4
sudo route add default gw 10.88.1.1
#notify-send "Connected to VPN. Pass $(cat /tmp/pass.txt)"
notify-send "Cyberoam By-Passed. Pass $(cat /tmp/pass.txt)"
