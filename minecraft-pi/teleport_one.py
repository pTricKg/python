# minecraft pi API necessities

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

# coordinates to teleport to
x = 40
y = 7
z = 83 # should be homebase

# actual teleport

mc.player.setTilePos(x,y,z)


