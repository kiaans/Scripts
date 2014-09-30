#cyberoam v2.0 autologin python script.
import urllib
import time

#Enter ID without '@da-iict.org'
username = 'ID'

#cyberoam password
password = 'pass'

#relogin time period in minutes
tm = 60

while True:
	try:
		f = urllib.urlopen('http://10.100.56.55:8090/httpclient.html','mode=191&username='+username+'@da-iict.org&password='+password+'&btnSubmit=Login')
		s = f.read()
		f.close()
		s = s[s.find('style="display:none">')+21:]
		s = s[:s.find('</div>')]
		print time.strftime('--%Y-%m-%d %I:%M %p--'), s+'.'
		
		time.sleep (tm*60)
	except IOError as error:
		print time.strftime('--%Y-%m-%d %I:%M %p--'), str(error)

