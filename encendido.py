import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)
pin=3
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	apagar=GPIO.input(pin)
	if apagar == False:
		os.system("sudo shutdown now")
GPIO.cleanup()