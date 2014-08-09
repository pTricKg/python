# import minecraft api necessities

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
''' Do not use coordinates > 127 on x and z'''

# coordinates to build on

x = 80
y = 7
z = 106

blktype = 12

# place block
mc.setBlock(x,y,z,blktype)

# place second block
y = y + 1
mc.setBlock(x,y,z,blktype)
