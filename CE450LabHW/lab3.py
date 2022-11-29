#!/usr/bin/env python3
#TEST123
#dot B
#dash G
#space R
import RPi.GPIO as GPIO
import time

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

Rled =7
Gled =13
Bled =11
unit = 0.1


def print_message():
    print("Please press Ctrl+C to end the program...")


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Rled, GPIO.OUT)
    GPIO.setup(Gled, GPIO.OUT)
    GPIO.setup(Bled, GPIO.OUT)

def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            cipher += ' '

    return cipher

def dot():
    time.sleep(unit*3)
    GPIO.output(Bled, GPIO.HIGH)
    time.sleep(unit)
    GPIO.output(Bled, GPIO.LOW)

def dash():
    time.sleep(unit*3)
    GPIO.output(Gled, GPIO.HIGH)
    time.sleep(unit*3)
    GPIO.output(Gled, GPIO.LOW)

def space():
    GPIO.output(Rled, GPIO.HIGH)
    time.sleep(unit*4)
    GPIO.output(Rled, GPIO.LOW)


def main(msg):
    while True:
            for morse in msg:
                if morse == ' ':
                    space()
                elif morse == '.':
                    dot()
                elif morse == '-':
                    dash()
                else:
                    print("something is wrong",morse)
                time.sleep(unit*7)

def destroy():
    GPIO.cleanup()


if __name__ == '__main__':
    result = encrypt(input("Please Enter Message : ").upper())
    setup()
    try:
        main(result)
    except KeyboardInterrupt:
        destroy()