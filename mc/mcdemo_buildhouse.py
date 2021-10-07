#Allison Gentry
#Build minecraft house using one button

import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
def buildhouse():
    pos = mc.player.getTilePos()
    mc.setBlocks(pos.x+1, pos.y, pos.z+1, pos.x+6, pos.y+5, pos.z+6, 82)
    mc.setBlocks(pos.x+2, pos.y+1, pos.z+2, pos.x+5, pos.y+4, pos.z+5, 0)

GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    if GPIO.input(6) == GPIO.LOW:
        buildhouse()

