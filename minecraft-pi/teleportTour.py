# import minecraft api necessities

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
import time

''' Do not use coordinates > 127 on x and z'''

x = 76
y = 7
z = 106

time.sleep(5)

x = 40
y = 7
z = 83

time.sleep(5)

x = 10
y = 11
z = 50

time.sleep(5)

x = 76
y = 7
z = 106

# move player: setTile is for integers
mc.player.setTilePos(x,y,z)
