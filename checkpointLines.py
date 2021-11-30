import pyglet
from hitLine import hitLine

class checkpointLines:
    def __init__(self, wallsArr):
        self.wallCtr = 0
        self.wallsArr = wallsArr

        self.wallHitboxArr = []

        self.currentCheckpoint = 0

        self.inRange = False

        self.wallBatch = pyglet.graphics.Batch()

        for wall in wallsArr:      
            self.calcWallHitbox(wall)

            self.wallCtr += 1           

    def checkCollision(self, hitboxAdd):    
        ctr = 0
        if self.wallHitboxArr[self.currentCheckpoint].checkCollision(hitboxAdd):
            self.currentCheckpoint += 1
            if self.currentCheckpoint == self.wallCtr:
                self.currentCheckpoint = 0
            
            return True
        return False
          
    def calcWallHitbox(self, wall):
        wallhitbox = hitLine(wall[0][0], wall[0][1], wall[1][0], wall[1][1])
        self.wallHitboxArr.append(wallhitbox)
    
    def reset(self):
        self.currentCheckpoint = 0
