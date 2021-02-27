import pyglet
from hitbox import hitbox

class walls:
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
        self.dot3 = pyglet.sprite.Sprite(image, x=0, y = 0, batch = self.dotBatch)
        self.dot4 = pyglet.sprite.Sprite(image, x=0, y = 0, batch = self.dotBatch)

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
                

    def calcWallHitbox(self, wall):
        thiccness = int(self.wallThicc / 2)
        if wall[0][0] <= wall[1][0]:
            print("1")
            leftMostx = wall[0][0]
            rightMostx = wall[1][0]
        else:
            print("2")
            leftMostx = wall[1][0]
            rightMostx = wall[0][0]
        if wall[0][1] >= wall[1][1]:
            print("3")
            topMosty = wall[1][1]
            botMosty = wall[0][1]
        else:
            print("4")
            topMosty = wall[0][1]
            botMosty = wall[1][1]

        thiccCalc = ((topMosty - botMosty) / (rightMostx - leftMostx)) * thiccness
        inverseThiccCalc = (-1 * (rightMostx - leftMostx) / (topMosty - botMosty)) * thiccness

        cord1x = 0
        cord1y = 0
        cord2x = 0
        cord2y = 0
        cord3x = 0
        cord3y = 0
        cord4x = 0
        cord4y = 0

        if wall[0][0] <= wall[1][0]:
            if wall[0][1] >= wall[1][1]:
                print("meme")
                cord1x = wall[0][0] + thiccCalc
                cord1y = wall[0][1] + inverseThiccCalc
                cord2x = wall[0][0] - thiccCalc
                cord2y = wall[0][1] - inverseThiccCalc
                cord3x = wall[1][0] + thiccCalc
                cord3y = wall[1][1] + inverseThiccCalc
                cord4x = wall[1][0] - thiccCalc
                cord4y = wall[1][1] - inverseThiccCalc
            else:
                print("meme2")
                cord1x = wall[1][0] + thiccCalc
                cord1y = wall[1][1] + inverseThiccCalc
                cord2x = wall[1][0] - thiccCalc
                cord2y = wall[1][1] - inverseThiccCalc
                cord3x = wall[0][0] + thiccCalc
                cord3y = wall[0][1] + inverseThiccCalc
                cord4x = wall[0][0] - thiccCalc
                cord4y = wall[0][1] - inverseThiccCalc
        else:
            if wall[0][1] >= wall[1][1]:
                print("meme3")
                cord1x = wall[0][0] + thiccCalc
                cord1y = wall[0][1] + inverseThiccCalc
                cord2x = wall[0][0] - thiccCalc
                cord2y = wall[0][1] - inverseThiccCalc
                cord3x = wall[1][0] + thiccCalc
                cord3y = wall[1][1] + inverseThiccCalc
                cord4x = wall[1][0] - thiccCalc
                cord4y = wall[1][1] - inverseThiccCalc
            else:
                print("meme4")
                cord1x = wall[1][0] + thiccCalc
                cord1y = wall[1][1] + inverseThiccCalc
                cord2x = wall[1][0] - thiccCalc
                cord2y = wall[1][1] - inverseThiccCalc
                cord3x = wall[0][0] + thiccCalc
                cord3y = wall[0][1] + inverseThiccCalc
                cord4x = wall[0][0] - thiccCalc
                cord4y = wall[0][1] - inverseThiccCalc

        self.dot1.x = cord1x
        self.dot1.y = cord1y
        self.dot2.x = cord2x
        self.dot2.y = cord2y
        self.dot3.x = cord3x
        self.dot3.y = cord3y
        self.dot4.x = cord4x
        self.dot4.y = cord4y

        print(str(cord1x) + " " + str(cord1y) + " " +str(cord2x) + " " + str(cord2y) + " " + str(cord3x) + " " +str(cord3y) + " " + str(cord4x) + " " + str(cord4y))

        wallhitbox = hitbox(cord1x, cord1y, cord2x, cord2y, cord3x, cord3y, cord4x, cord4y)
        self.wallHitboxArr.append(wallhitbox)
