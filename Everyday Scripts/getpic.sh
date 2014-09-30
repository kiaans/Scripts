#Shell Script to get ID card pic of a student
#!/bin/bash
echo "Enter starting ID of the batch: "
read ID
echo "Enter ending ID of the batch: "
read eID
#mkdir /home/krsumeet/StudentPics
#cd /home/krsumeet/StudentPics
for ((i=ID; i<=eID; i++))
do
	wget https://10.100.56.31:8443/webapp/intranet/StudentPhotos/$i.jpg --no-check-certificate
done
