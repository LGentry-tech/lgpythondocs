#Allison Gentry
#Minecraft Code Example

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

mc.postToChat('hello')

mc.player.getTilePos()
player = mc.player.getTilePos()
mc.postToChat(player)