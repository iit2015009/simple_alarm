import sys
import random
import	webbrowser 
import time
def wakeupfunc():
	input=open('link.txt','r');
	urllis=input.readlines();
	url=random.choice(urllis)
	webbrowser.open(url,new=1,autoraise=False)
	argl=sys.argv
arg=sys.argv
print arg
while True:
	stri=time.strftime("%Y-%m-%d %H:%M")
	strl=stri.split(' ')
	print "now its"+strl[1]
	if strl[1]==arg[1]:
		print("wake up!")
		wakeupfunc()
		break
	time.sleep(60)



