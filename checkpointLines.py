import pyglet
from hitLine import hitLine

class checkpointLines:
    def __init__(self, wallsArr):
        self.wallCtr = 0
        self.wallsArr = wallsArr
        self.spriteArr = []
        self.wallHitboxArr = []

        self.currentCheckpoint = 0

        self.wallThicc = 1

        self.labelBatch = pyglet.graphics.Batch()
        self.inRange = False

        self.wallBatch = pyglet.graphics.Batch()

        for wall in wallsArr:
            
            print("wall " + str(self.wallCtr))
            image = "checkPoint" + str(self.wallCtr) + ".png"
            image = pyglet.image.load('Res/sprites/' + image)
            sprite = pyglet.sprite.Sprite(image, x=0, y = 0, batch = self.wallBatch)
            self.spriteArr.append(sprite)
            self.calcWallHitbox(wall)

            self.wallCtr += 1

        for wallHitbox in self.wallHitboxArr:
            wallHitbox.updateEdges()
            

    def draw(self):
        self.wallBatch.draw()

    def checkCollision(self, hitboxAdd):    
        ctr = 0
        if self.wallHitboxArr[self.currentCheckpoint].checkCollision(hitboxAdd):
            print("REACHED:", self.currentCheckpoint)
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