#Implement
#Add LED

import RPi.GPIO as GPIO
import time

BeepPin = 11    # pin11

def setup():
	GPIO.setmode(GPIO.BOARD)        # Numbers GPIOs by physical location
	GPIO.setup(BeepPin, GPIO.OUT)   # Set BeepPin's mode is output
	GPIO.output(BeepPin, GPIO.HIGH) # Set BeepPin high(+3.3V) to off beep

def loop():
	while True:
		GPIO.output(BeepPin, GPIO.LOW)	# Switch on Buzzer
		time.sleep(0.1)		  	# 0.1s delay
		GPIO.output(BeepPin, GPIO.HIGH)
		time.sleep(0.1)

def destroy():
	GPIO.output(BeepPin, GPIO.HIGH)    # beep off
	GPIO.cleanup()                     # Release resource



print('Press Ctrl+C to end the program...')

setup()
try:
	loop()
except 	KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
	destroy()