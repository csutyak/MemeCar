import pyglet
from hitLine import hitLine

class lineWalls:
    def __init__(self, wallsArr):
        self.wallCtr = 0
        self.wallsArr = wallsArr
        self.spriteArr = []
        self.wallHitboxArr = []

        self.wallThicc = 1

        self.labelBatch = pyglet.graphics.Batch()
        self.inRange = False

        self.wallBatch = pyglet.graphics.Batch()

        for wall in wallsArr:
            
            print("wall " + str(self.wallCtr))
            image = "wall" + str(self.wallCtr) + ".png"
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
        for wall in self.wallHitboxArr:
            if wall.checkCollision(hitboxAdd):
                return True
            else:
                ctr += 1
                if ctr == self.wallCtr:
                    return False

    def getLineDistanceArr(self, hitboxAdd):
        #self.topLeftx
        #self.topLefty
        #self.topRightx
        #self.topRighty
        #self.bottomLeftx
        #self.bottomLefty
        #self.bottomRightx
        #self.bottomRighty
        
        #top middle line
        minDistance = 99999999
        minDistanceArray = [minDistance,minDistance,minDistance,minDistance,minDistance,minDistance,minDistance,minDistance]
        
        #loops through wall    
        for wall in self.wallHitboxArr:

            #gets the distances of that wall
            wallDistanceArray = wall.findDistances(hitboxAdd)
            for index in range(8):
                if wallDistanceArray[index] != -1:
                    if minDistanceArray[index] > wallDistanceArray[index]:
                        minDistanceArray[index] = wallDistanceArray[index]

        return minDistanceArray
          
    def calcWallHitbox(self, wall):
        wallhitbox = hitLine(wall[0][0], wall[0][1], wall[1][0], wall[1][1])
        self.wallHitboxArr.append(wallhitbox)
    
    
