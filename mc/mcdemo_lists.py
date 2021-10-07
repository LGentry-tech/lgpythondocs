#Allison Gentry
#Places a randomly colored wool block

'''Setup program for mc ad two buttons
Create a counter for variable that starts at 0
Create a list of blockdata numbers for the colors
Define a function called placenext
The function takes one argument called direction, it changes the counter by adding the direction
argument, place a wool block of the color from the list where your index matches the counter
If the counter is out of bounds of the index reset it
In a forever loop: First button Placenext(1), second button pressed(-1)
'''

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

counter = 0
woolColors =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def placeNext(direction):
    global counter
    counter += direction
    
    if counter < 0:
        counter = 0
    if counter > 14:
        counter = 0
    mc.setBlock(-65, 20, 37, 35, woolColors[counter])

while True:
    
    if GPIO.input(6) == GPIO.LOW:
        placeNext(1)
    if GPIO.input(13) == GPIO.LOW:
        placeNext(-1)
    
placeNext()