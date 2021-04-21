import pyglet
from hitbox import hitbox
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

        self.dotBatch = pyglet.graphics.Batch()

        image = pyglet.image.load('Res/sprites/dot.png')
        self.dot1 = pyglet.sprite.Sprite(image, x=0, y = 0, batch = self.dotBatch)
        self.dot2 = pyglet.sprite.Sprite(image, x=0, y = 0, batch = self.dotBatch)

        self.collisionDot = pyglet.sprite.Sprite(image, x=0, y =0, batch = self.dotBatch)

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
            print(wallHitbox.leftMostx)
            print(wallHitbox.rightMostx)
            print(wallHitbox.topMosty)
            print(wallHitbox.botMosty)
            

    def draw(self):
        self.wallBatch.draw()
        self.dotBatch.draw()
        self.labelBatch.draw()

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
        for wall in self.wallHitboxArr:
            wallDistance = wall.findDistances(hitboxAdd)
            if wallDistance != -1:
                if minDistance > wallDistance:
                    minDistance = wallDistance
        
        print(minDistance)
            
            
                
    def calcWallHitbox(self, wall):
        wallhitbox = hitLine(wall[0][0], wall[0][1], wall[1][0], wall[1][1])
        self.wallHitboxArr.append(wallhitbox)
    
    
