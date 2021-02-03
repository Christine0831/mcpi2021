from mcpi.minecraft import Minecraft
mc = Minecraft.create()

import random
import time

while True:
    x,y,z = mc.player.getTilePos()
    x = x + random.randrange(-10,10)
    z = z + random.randrange(-10,10)
    y = y + 30
    
    mc.spawnEntity(x,y,z,93)
    time.sleep(0.2)
    




























def plantTree(x,y,z):
    mc.setBlocks(x-1,y+3,z-1,x+1,y+5,z+1,161)
    mc.setBlocks(x,y,z,x,y+4,z,17) 
    
    
    x,y,z = mc.player.getTilePos()
    
    for i in range(6):
        for j in range(6):
            plantTree(x + i*5,y,z + j*5)
    












    