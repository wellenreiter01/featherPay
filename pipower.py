#! /usr/bin/python
#pipower.py
import time
import os
import RPi.GPIO as GPIO

#set the signal pin high
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#the power switch script
GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_UP)
 
def Shutdown(channel):
 os.system("sudo reboot")
 
GPIO.add_event_detect(20, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)
 
while 1:
 time.sleep(1)
