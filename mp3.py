import os
import glob
from time import sleep
import subprocess
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.IN) # pause
GPIO.setup(23,GPIO.IN) # stop
GPIO.setup(24,GPIO.IN) # Next
GPIO.setup(25,GPIO.IN) # Previous

os.chdir('home/pi/Music')
f = glob.glob('*.mp3')
print(f)
h= len(f) #quantity of mp3
print(h)
flag=1
pt=0 #audio's number
st=0 #Stop status

#kill previous mp3
os.system('sudo killall omxplayer.bin')
while 1:
	if flag==1:
		player = subprocess.Popen(["omxplayer",f[pt]],stdin=subprocess.PIPE)
		fi = player.poll()
		flag=0
		st=0

	if (GPIO.input(22) == 0): #Pause
		sleep(0.5)
		fi=player.poll()
		if fi!=0:
			player.stdin.write("p")
	if (GPIO.input(23) == 0): #Stop
                sleep(0.5)
                fi=player.poll()
                if fi!=0:
                        player.stdin.write("q")
			st=1

	if (GPIO.input(24) == 0): #Next
                if st==0
			player.stdin.write("q")
		flag=1
		pt=pt+1
		if pt>h-1
			pt=h-1
		sleep(0.5)

	elif (GPIO.input(25) == 0): #Previous
                if st==0
                        player.stdin.write("q")
                flag=1
                pt=pt-1
                if pt<0
                        pt=h-1
                sleep(0.5)
	else:
		fi = player.poll()
		if(fi==0 and st ==0)
			flag=1
			pt=pt+1
			if pt>h-1
				pt=0
	sleep(0.1)
