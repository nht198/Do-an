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

os.chdir('home/pi/Desktop/Music')
f = glob.glob('*.mp3')
print(f)
h= len(f)
print(h)
flag=1
pt=0
st=0

os.system('sudo killall omxplayer.bin')

player = subprocess.Popen(["omxplayer",f[pt]],stdin=subprocess.PIPE)
fi = player.poll()
sleep(10)
print("haha")
player.stdin.write("p")
sleep(10)
player.stdin.write("p")

flag = 0
st = 0  

