# import minecraft api necessities

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
''' Do not use coordinates > 127 on x and z'''

# coordinates to teleport to

x = 40
y = 7
z = 83

# move player
mc.player.setTilePos(x,y,z)   

