import os
import glob
from time import sleep
import subprocess
import RPi.GPIO as GPIO
import urllib2

GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.IN) # pause
GPIO.setup(23,GPIO.IN) # stop
GPIO.setup(24,GPIO.IN) # Next
GPIO.setup(25,GPIO.IN) # Previous

os.chdir('/home/pi/Music')
f = glob.glob('*.mp3')
print(f)
h= len(f) #quantity of mp3
print(h)
flag=1
pt=0 #audio's number

os.system('sudo killall omxplayer.bin')

while 1:
	if flag==1:
		player = subprocess.Popen(["omxplayer",f[pt]],stdin=subprocess.PIPE)
		print ("Dang choi bai: " + f[pt])
		fi = player.poll()
		flag=0
		st=0
	#read contents from url include button to play
	try:
		response = urllib2.urlopen('http://nht198-001-site1.1tempurl.com/mp3/status.php')
		status = response.read()
	except urllib2.HTTPError, e:
		print e.code
	except urllib2.URLError, e:
		print e.args 

	#end read, it written in 'status' var
	if (status=='Play'): # Pause or Play
		print("Play/Pause pressed")
		sleep(0.5)
		fi=player.poll() 
		if fi!=0:
			 player.stdin.write("p")

	if (status=='Stop'): #Stop
		print("Stop pressed")
                sleep(0.2)
                fi=player.poll()
		print("fi %d",fi)
#		player.kill()
                if fi!=0:
                        player.stdin.write("q")
			st=1

	if (status=='Next'): #Next
		print("Next pressed")
		sleep(0.3)
                if st==0:
			player.stdin.write("q")
		flag=1
		pt=pt+1
		if pt>h-1:
			pt=h-1
	

	elif (status=='Previous'): #Previous
		print("Previuos pressed")
		sleep(0.3)
                if st==0:
                        player.stdin.write("q")
                flag=1
                pt=pt-1
                if pt<0:
                        pt=h-1
