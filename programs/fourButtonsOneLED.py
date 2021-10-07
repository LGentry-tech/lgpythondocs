#Allison Gentry
#4 Buttons, 1 LED

#Use a module for reqesting data online
import requests

#Use a module to control time
import time

#Setup for buttons and LEDs
import RPi.GPIO as GPIO # import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) #Use physical pin numbering

#Setup each pin number
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Start an infinite loop
while True:
    #wait for one second
    time.sleep(1)
    #check the first button
    if GPIO.input(6) == GPIO.LOW:
        print("Button up was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=up")
    elif GPIO.input(13) == GPIO.LOW:
        print("Button to wiggle was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=wiggle")
    elif GPIO.input(19) == GPIO.LOW:
        print("Button down was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=down")
    elif GPIO.input(26) == GPIO.LOW:
        print("Button to remove thumbs was pressed")
        requests.get("http://192.168.10.53:5000/tutd?thumb=oops")
