#Kumar Sumeet
#For Connecting to Gmail SMTP server.  
import smtplib  
#For composing the email message  
from email.MIMEMultipart import MIMEMultipart  
from email.MIMEBase import MIMEBase  
from email.MIMEText import MIMEText  
from email import Encoders  
  
from getpass import getpass #For getting password from the user  
import os  
  
gmail_user = "xxxxxxxxxxxx@gmail.com"  
  
def mail(to, subject, text):  
    """Sends email"""  
    msg = MIMEMultipart()  
  
    msg['From'] = gmail_user  
    msg['To'] = to  
    msg['Subject'] = subject  
    msg.attach(MIMEText(text)) 
   
    mailServer = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#    mailServer.starttls()    #All SMTP commands that follow will be ssl encrypted  
    mailServer.login(gmail_user, gmail_pwd)    #Login performed  
    mailServer.sendmail(gmail_user, to, msg.as_string())  
    mailServer.close()  
  
  
# RECEPIENTS ADDRESS, SUBJECT, BODY, PASSWORD input
entermore="y"  
recepients = []  
gmail_pwd = getpass()  
  
while entermore == "y":  
    recepient_email = raw_input("Email address: ")  
    recepients.append(recepient_email)  
    entermore = raw_input("Do you want to enter more recipients(y/n): ")  
  
#print recepients  
subject = raw_input("Subject: ")  
body = raw_input("Body: ")    
  
for email in recepients:  
    mail(email,subject,body)  
    print "Your email to "+str(email)+" has been sent successfully! :)" 
