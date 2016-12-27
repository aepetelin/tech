print("")
print("*-------------------------------------------------------------------")
print("*         Raspbery Pi, lenvo.se, Gothenburg, 2016-2017              ")
print("*-------------------------------------------------------------------")
print("")

print("Hello World!")

import time
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)
GPIO.output(3, GPIO.LOW)

GPIO.setup(5, GPIO.OUT)
GPIO.output(5, GPIO.OUT)

GPIO.setup(7, GPIO.LOW)
GPIO.output(7, GPIO.LOW)

i = 0
while i < 10:
    i = i + 1
    GPIO.output(3, GPIO.HIGH)
    time.sleep(4)

    GPIO.output(5, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)

    GPIO.output(7, GPIO.HIGH)
    time.sleep(2)

    interval = 2
    section = 0.5
    progress = 0
    j = 0
    while (j < 5):
        j = j + 1
        time.sleep(section)
        GPIO.output(7, GPIO.LOW)
        time.sleep(section)
        GPIO.output(7, GPIO.HIGH)

    GPIO.output(7, GPIO.LOW)
    GPIO.output(5, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(5, GPIO.LOW)

    
GPIO.output(3, GPIO.LOW)
GPIO.output(5, GPIO.LOW)
GPIO.output(7, GPIO.LOW)


