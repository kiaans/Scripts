#Author: Kumar Sumeet
#Script to spam someone's mailbox on this auspicious Tannuday :D

#For Connecting to Gmail SMTP server.  
import smtplib  
import time
#For composing the email message  
from email.MIMEMultipart import MIMEMultipart  
from email.MIMEBase import MIMEBase  
from email.MIMEText import MIMEText  
from email import Encoders  
  
from getpass import getpass #For getting password from the user  
import os  

f = open('contacts', 'r')
  
gmail_user = "your email here"  
  
def mail(to, subject, text):  
    """Sends email"""  
    msg = MIMEMultipart()  
  
    msg['From'] = gmail_user  
    msg['To'] = to  
    msg['Subject'] = subject  
    msg.attach(MIMEText(text)) 
   
    mailServer = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
#    mailServer.starttls()    #All SMTP commands that follow will be ssl encrypted  
    mailServer.login(gmail_user, gmail_pwd)    #Login performed  
    mailServer.sendmail(gmail_user, to, msg.as_string())  
    mailServer.close()  
  
  
# RECEPIENTS ADDRESS, SUBJECT, BODY, PASSWORD input
entermore="y"  
recepients = []  
#gmail_pwd = getpass()

### IF USING APPLICATION SPECIFIC PASSWORD, ENTER IT HERE UNDER THE QUOTES AND UNCOMMENT IT (Comment the line above too).
gmail_pwd = "your pass"  
  
####while entermore == "y":  
    ####recepient_email = raw_input("Email address: ")  
    ####recepients.append(recepient_email)  
    ####entermore = raw_input("Do you want to enter more recepients(y/n): ")  
  
#print recepients  
subject = "your subject here"  
body = "your body here"
    
#sub_mod = time.strftime("%Y-%m-%d %H:%M:%S")+subject
  
while True:
	try:
		recepient_email = f.readline()
		recepients.append(recepient_email)
		if not recepient_email: 
			break
	
	except IOError as error:
                print time.strftime('--%Y-%m-%d %I:%M %p--'), str(error)

try:
	for email in recepients:  
		mail(email,subject,body)  
		print "Your email to "+str(email)+" has been sent successfully! :)" 
#		sub_mod = time.strftime("%Y-%m-%d %H:%M:%S")+subject
  
#	time.sleep (3)
  
except IOError as error:
	print time.strftime('--%Y-%m-%d %I:%M %p--'), str(error)
