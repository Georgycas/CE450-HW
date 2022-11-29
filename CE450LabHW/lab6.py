# 7segment display midterm
#Hi you did a good job

# 7 segment display
# !/usr/bin/env python3
import RPi.GPIO as GPIO
import time

DSPin = 11
STCPPin = 13
SHCPPin = 15
BeepPin = 33

BIT_DICT = {'A': '01111107', 'B': '01100111',
            'C': '00110011', 'D': '01001111', 'E': '01110011',
            'F': '01110001', 'G': '00110111', 'H': '01100101',
            'I': '00001100', 'J': '00001111', 'K': '01110101',
            'L': '00100011', 'M': '01010101', 'N': '00111101',
            'O': '00111111', 'P': '01111001', 'Q': '01111100',
            'R': '00110001', 'S': '01110110', 'T': '01100011',
            'U': '00101111', 'V': '00101010', 'W': '01101010',
            'X': '01010010', 'Y': '01101110', 'Z': '01101011',
            '1': '00001100', '2': '01011011', '3': '01011110',
            '4': '01101100', '5': '01110110', '6': '01110111',
            '7': '00011100', '8': '01111111', '9': '01111100',
            '0': '00111111', ' ': '00000000'}

digits = 3


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(DSPin, GPIO.OUT)
    GPIO.setup(STCPPin, GPIO.OUT)
    GPIO.setup(SHCPPin, GPIO.OUT)
    GPIO.setup(BeepPin, GPIO.OUT)


def Beep():
    GPIO.output(BeepPin, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(BeepPin, GPIO.LOW)


def bitencrypt(message):
    bit = ''
    for letter in message:
        if letter != '':
            bit += BIT_DICT[letter] + ''
        else:
            bit += ''

    return bit


def shifter(dPin, cPin, sent):
    for x in range(len(sent)):

        if x % 8 == 0:
            GPIO.output(STCPPin, GPIO.HIGH)
            GPIO.output(STCPPin, GPIO.LOW)
            time.sleep(0.1)

        GPIO.output(cPin, GPIO.LOW)
        GPIO.output(dPin, sent[x] == 0 and GPIO.HIGH or GPIO.LOW)
        GPIO.output(cPin, GPIO.HIGH)

    return


def loop(send):
    while True:
        GPIO.output(STCPPin, GPIO.LOW)
        shifter(DSPin, SHCPPin, bitencrypt(send))
        GPIO.output(STCPPin, GPIO.HIGH)
        time.sleep(0.5)


def destroy():
    print('GPIO Cleaned')
    GPIO.cleanup()


if __name__ == '__main__':
    print('Program is Starting')
    setup()
    try:
        sender = "Hi you did a good job"[::-1]
        sender += ' ' * digits
        Beep()
        loop(sender.upper())
    except KeyboardInterrupt:
        destroy()
