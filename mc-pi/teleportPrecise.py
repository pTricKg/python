# import minecraft api necessities

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

''' Do not use coordinates > 127 on x and z'''

# coordinates to teleport to

# home >
x = 76.4
y = 7.1
z = 106.3

# move player using floats with setPos
mc.player.setPos(x,y,z)

# move player using integers with:
# mc.playler.setTilePos(x,y.z)
