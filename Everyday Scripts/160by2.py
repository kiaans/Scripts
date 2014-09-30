import sys
import time
import urllib2, cookielib

if len(sys.argv)<5:
    print 'Usage:', sys.argv[0], '160by2_username', '160by2_password', 'receiver_number', 'text_to_send'
    sys.exit(1)

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64; rv:8.0) Gecko/20100101 Firefox/8.0')]

def login (user, passwd):
    f = opener.open('http://www.160by2.com/logincheck.aspx?iamindian=', 'txt_UserName='+user+'&txt_Passwd='+passwd)
    s = f.read()
    f.close()
    return 'logout' in s

def send (recvr, text):
    f = opener.open('http://www.160by2.com/publicsms_sendsms.aspx', 'nickname=kr.sum&group1=1&txt_mobileno='+recvr+'&txt_send_sms='+text)
    f.close()

def log (text, filename):
    f=open(filename, 'w')
    f.write(text)
    f.close()

sender = sys.argv[1]
password = sys.argv[2]
receiver = sys.argv[3]
text = ' '.join(sys.argv[4:])

print 'Logging in...',
sys.stdout.flush()
if login(sender, password):
    print 'done'
    print 'Sending text...',
    sys.stdout.flush()
    send(receiver, text)
    print 'done'
else:
    print 'Invalid username/password'
    sys.exit(2)


