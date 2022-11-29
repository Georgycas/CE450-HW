"""
1.	Build up the hardware circuit and run the example program to observe what will happen

2.	Add a buzzer to the above circuit and design the program to make “z” sound as the turning indicator if the encoder
is turned one circle

"""
# Python Program

import RPi.GPIO as GPIO
import time

RoAPin = 11  # pin11	-> Connected to CLK
RoBPin = 12  # pin12	-> Connected to DT
RoSPin = 13  # pin13	-> Connected to SW
beepin = 36

globalCounter = 0

flag = 0
Last_RoB_Status = 0  # two var. for pin B’s value
Current_RoB_Status = 0


def setup():
    GPIO.setmode(GPIO.BOARD)  # Numbers GPIOs by physical location
    GPIO.setup(RoAPin, GPIO.IN)  # input mode
    GPIO.setup(RoBPin, GPIO.IN)
    GPIO.setup(RoSPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Bottom pin
    GPIO.setup(beepin, GPIO.OUT)
    rotaryClear()


def rotaryDeal():
    global flag
    global Last_RoB_Status
    global Current_RoB_Status
    global globalCounter
    Last_RoB_Status = GPIO.input(RoBPin)  # Read in data from DT
    while not GPIO.input(RoAPin):
        Current_RoB_Status = GPIO.input(RoBPin)
        flag = 1
    if flag == 1:
        flag = 0
        if (Last_RoB_Status == 0) and (Current_RoB_Status == 1):
            globalCounter = globalCounter + 1
            print('globalCounter = %d' % globalCounter)
        if (Last_RoB_Status == 1) and (Current_RoB_Status == 0):
            globalCounter = globalCounter - 1
            print('globalCounter = %d' % globalCounter)
    if globalCounter % 22 == 0:
        beep()


def beep():
        GPIO.output(beepin, GPIO.HIGH)
        time.sleep(0.1)
        print("beep")
        GPIO.output(beepin, GPIO.LOW)
        time.sleep(0.5)

def clear():
    globCounter = 0
    print('globalCounter = %d' % globCounter)
    time.sleep(1)


def rotaryClear():
    GPIO.add_event_detect(RoSPin, GPIO.FALLING, callback=clear)


# wait for falling

def loop():
    global globalCounter
    while True:
        rotaryDeal()


# print 'globalCounter = %d' % globalCounter

def destroy():
    GPIO.cleanup()  # Release resource


setup()
try:
    loop()
except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()