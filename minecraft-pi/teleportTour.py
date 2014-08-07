# import minecraft api necessities
import time
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()


''' Do not use coordinates > 127 on x and z'''

time.sleep(10)

x = 40
y = 7
z = 83

# move player: setTile is for integers
mc.player.setTilePos(x,y,z)

time.sleep(5)

x = 10
y = 11
z = 50

# move player: setTile is for integers
mc.player.setTilePos(x,y,z)

time.sleep(5)

x = 76
y = 7
z = 106

# move player: setTile is for integers
mc.player.setTilePos(x,y,z)

time.sleep(2)

x = 76
y = 7
z = 115

# move player: setTile is for integers
mc.player.setTilePos(x,y,z)

time.sleep(2)

x = 76
y = 7
z = 106

# move player: setTile is for integers
mc.player.setTilePos(x,y,z)
