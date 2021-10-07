#Allison Gentry
#Place a block

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
    mc.setBlocks(pos.x, pos.y-1, pos.z, 247)