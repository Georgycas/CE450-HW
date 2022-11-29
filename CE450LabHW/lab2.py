#!/usr/bin/env python3
# 1	Design program to blink one LED and shift back and forth among 8 LEDs.
# 2	Make 2 LEDs at the two ends of 8 LEDs on the board blink and move in different directions and back.
# 3	Make 2 LEDs in the center blink in different directions and move back.

# There are 9 LEDs LedPins[0] indicates when the numbering is in reverse
import RPi.GPIO as GPIO
import time


LedPins = [7, 11, 13, 15, 29, 31, 33, 35, 37]  # 9 pins


def print_message(frm):
    print(frm)
    print("Please press Ctrl+C to end the program...")


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LedPins, GPIO.OUT)


def main():
    print_message("One LED Shift Back and Forth")

    while True:
        for i in range(1, len(LedPins)):
            GPIO.output(LedPins[i], GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(LedPins[i], GPIO.LOW)
        GPIO.output(LedPins[0], GPIO.HIGH)
        for i in range(1, len(LedPins)):
            GPIO.output(LedPins[-i], GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(LedPins[-i], GPIO.LOW)
        GPIO.output(LedPins[0], GPIO.LOW)

def eachend():
    print_message("Two LEDs at Each End")

    while True:
        for i in range(1, len(LedPins)):
            GPIO.output(LedPins[i], GPIO.HIGH)
            GPIO.output(LedPins[-i], GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(LedPins[i], GPIO.LOW)
            GPIO.output(LedPins[-i], GPIO.LOW)
        GPIO.output(LedPins[0], GPIO.HIGH)

        for i in range(1, len(LedPins)):
            GPIO.output(LedPins[-i], GPIO.HIGH)
            GPIO.output(LedPins[i], GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(LedPins[-i], GPIO.LOW)
            GPIO.output(LedPins[i], GPIO.LOW)
        GPIO.output(LedPins[0], GPIO.LOW)


def middle():
    print_message("Two LEDs at the Middle")

    while True:
        for i in range(5, len(LedPins)):
            GPIO.output(LedPins[i], GPIO.HIGH)
            GPIO.output(LedPins[-i], GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(LedPins[i], GPIO.LOW)
            GPIO.output(LedPins[-i], GPIO.LOW)
        GPIO.output(LedPins[0], GPIO.HIGH)

        for i in range(1, len(LedPins)-5):
            GPIO.output(LedPins[i], GPIO.HIGH)
            GPIO.output(LedPins[-i], GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(LedPins[i], GPIO.LOW)
            GPIO.output(LedPins[-i], GPIO.LOW)
        GPIO.output(LedPins[0], GPIO.LOW)


def destroy():
    GPIO.output(LedPins, GPIO.HIGH)
    GPIO.cleanup()


if __name__ == '__main__':
    setup()
    print("1. One LED Shift Back and Forth")
    print("2. Two LEDs at Each End")
    print("3. Two LEDs at the Middle")
    x = input("Enter A Mode Number ")
    try:
        if x == '1':
            main()
        elif x == '2':
            eachend()
        elif x == '3':
            middle()
        else:
            print("Not a valid input")
            destroy()
    except KeyboardInterrupt:
        destroy()