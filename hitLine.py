from hitbox import hitbox
import math

class hitLine:
    def __init__(self, firstX, firstY, secondX, secondY):
        self.firstX = firstX
        self.firstY = firstY
        self.secondX = secondX
        self.secondY = secondY

        self.leftMostx = 0
        self.rightMostx = 0
        self.topMosty = 0
        self.botMosty = 0

        self.updateEdges()

        self.lauv = "meme"

    def updateHitBox(self, firstX, firstY, secondX, secondY):
        self.firstX = firstX
        self.firstY = firstY
        self.secondX = secondX
        self.secondY = secondY

        self.updateEdges()

    def setEdges(self, leftMostx, rightMostx, topMosty, botMosty):
        self.leftMostx = leftMostx
        self.rightMostx = rightMostx
        self.topMosty = topMosty
        self.botMosty = botMosty

    def updateEdges(self):
        #firstX, firstY, secondX, secondY
        if self.firstY > self.secondY:
            self.topMosty = self.firstY
            self.botMosty = self.secondY

        else:
            self.topMosty = self.secondY
            self.botMosty = self.firstY

        if self.firstX > self.secondX:
            self.leftMostx = self.secondX
            self.rightMostx = self.firstX

        else:
            self.leftMostx = self.firstX
            self.rightMostx = self.secondX

    def checkCollision(self, hitboxAdd):   
        if self.checkInRangex(hitboxAdd) and self.checkInRangey(hitboxAdd):
            return self.hitboxIntersect(hitboxAdd)
        else:
            return False

    def checkInRangex(self, hitboxAdd):

        if hitboxAdd.leftMostx >= self.leftMostx:
            #hitbox add is in the x of the wall
            if hitboxAdd.leftMostx <= self.rightMostx:
                return True
        elif hitboxAdd.rightMostx >= self.leftMostx:
            return True

        return False

    def checkInRangey(self, hitboxAdd):
        
        if hitboxAdd.botMosty >= self.botMosty:
            if hitboxAdd.botMosty <= self.topMosty:
                return True
        elif hitboxAdd.topMosty >= self.botMosty:
            return True

        return False

    def hitboxIntersect(self, hitboxAdd):   
        #top
        if self.lineIntersect(hitboxAdd.topLeftx, hitboxAdd.topLefty, hitboxAdd.topRightx, hitboxAdd.topRighty, self.firstX, self.firstY, self.secondX, self.secondY):
            return True
        #right
        elif self.lineIntersect(hitboxAdd.topRightx, hitboxAdd.topRighty, hitboxAdd.bottomRightx, hitboxAdd.bottomRighty, self.firstX, self.firstY, self.secondX, self.secondY):
            return True
        #left
        elif self.lineIntersect(hitboxAdd.topLeftx, hitboxAdd.topLefty, hitboxAdd.bottomLeftx, hitboxAdd.bottomLefty, self.firstX, self.firstY, self.secondX, self.secondY):
            return True
        #bottom
        elif self.lineIntersect(hitboxAdd.bottomLeftx, hitboxAdd.bottomLefty, hitboxAdd.bottomRightx, hitboxAdd.bottomRighty, self.firstX, self.firstY, self.secondX, self.secondY):
            return True
        

    def lineIntersect(self, line1firstx, line1firsty, line1secondx, line1secondy, line2firstx, line2firsty, line2secondx, line2secondy):
        #slope and b value of the first line
        devisor = line1firstx - line1secondx
        if devisor == 0:
            devisor = 0.00000001
        line1M = (line1firsty - line1secondy) / devisor
        line1B = (line1firsty - (line1M * line1firstx))

        #slope and b value of the second line
        devisor = line2firstx - line2secondx
        if devisor == 0:
            devisor = 0.00000001
        line2M = (line2firsty - line2secondy) / devisor
        line2B = (line2firsty - (line2M * line2firstx))

        #cordinates at which the lines intersect
        devisor = line2M - line1M
        if devisor == 0:
            devisor = 0.00000001
        intersectx = (line1B - line2B) / (devisor)
        intersecty = (line1M * intersectx) + line1B

        #check if in x range of first line
        if self.checkinRange(intersectx, line1firstx, line1secondx) and self.checkinRange(intersecty, line1firsty, line1secondy):
            if self.checkinRange(intersectx, line2firstx, line2secondx) and self.checkinRange(intersecty, line2firsty, line2secondy):
                return True

        return False

    def checkinRange(self, value, point1, point2):
        if point1 > point2:
            if value <= point1 and value >= point2:
                return True
        else:
            if value >= point1 and value <= point2:
                return True
        return False
    
    #only checks if its in range for the first Line :)
    #gets the distance from the intersecting point between the lines
    #add another 2 for the points of the back one and then use the distance between both of those to get orientation
    def getDistanceFromIntersect(self, line1firstx, line1firsty, line1secondx, line1secondy, line2firstx, line2firsty, line2secondx, line2secondy, frontPointx, frontPointy, backPointx, backPointy ):
        #slope and b value of the first line
        devisor = line1firstx - line1secondx
        if devisor == 0:
            devisor = 0.00000001
        line1M = (line1firsty - line1secondy) / devisor
        line1B = (line1firsty - (line1M * line1firstx))

        #slope and b value of the second line
        devisor = line2firstx - line2secondx
        if devisor == 0:
            devisor = 0.00000001
        line2M = (line2firsty - line2secondy) / devisor
        line2B = (line2firsty - (line2M * line2firstx))

        #cordinates at which the lines intersect
        devisor = line2M - line1M
        if devisor == 0:
            devisor = 0.00000001
        intersectx = (line1B - line2B) / (devisor)
        intersecty = (line1M * intersectx) + line1B

        #check if in x range of first line
        if self.checkinRange(intersectx, line1firstx, line1secondx) and self.checkinRange(intersecty, line1firsty, line1secondy):
            #frontPointx, frontPointy
            #intersectx 
            #intersecty 
            frontDistance = math.sqrt(((frontPointx - intersectx)*(frontPointx - intersectx)) + ((frontPointy - intersecty)*(frontPointy - intersecty)))
            backDistance = math.sqrt(((backPointx - intersectx)*(backPointx - intersectx)) + ((backPointy - intersecty)*(backPointy - intersecty)))
            if frontDistance < backDistance:
                return frontDistance

        return -1
    
    def findDistances(self, hitboxAdd):
        #self.middleLeftx = 0
        #self.middleLefty = 0
        #self.middleRightx = 0
        #self.middleRighty = 0
        #self.middleTopx = 0
        #self.middleTopy = 0
        #self.middleBottomx = 0
        #self.middleBottomy = 0
        return self.getDistanceFromIntersect(self.firstX, self.firstY, self.secondX, self.secondY, hitboxAdd.middleTopx, hitboxAdd.middleTopy, hitboxAdd.middleBottomx, hitboxAdd.middleBottomy, hitboxAdd.middleTopx, hitboxAdd.middleTopy, hitboxAdd.middleBottomx, hitboxAdd.middleBottomy)
    