import pyglet
from hitLine import hitLine

class lineWalls:
    def __init__(self, wallsArr):
        self.wallCtr = 0
        self.wallsArr = wallsArr

        self.wallHitboxArr = []

        self.inRange = False

        for wall in wallsArr:
            self.calcWallHitbox(wall)

            self.wallCtr += 1           

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
    
    
