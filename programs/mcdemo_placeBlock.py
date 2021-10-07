#Allison Gentry
#Place a block

from mcpi.minecraft import Minecraft
while True:
    mc = Minecraft.create()
    pos = mc.player.getTilePos()
    mc.setBlock(pos.x, pos.y-1, pos.z, 103)