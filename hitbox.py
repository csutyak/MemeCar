

class hitbox:
    def __init__(self, topLeftx, topLefty, topRightx, topRighty, bottomLeftx, bottomLefty, bottomRightx, bottomRighty):
        self.topLeftx = topLeftx
        self.topLefty = topLefty
        self.topRightx = topRightx
        self.topRighty = topRighty
        self.bottomLeftx = bottomLeftx
        self.bottomLefty = bottomLefty
        self.bottomRightx = bottomRightx
        self.bottomRighty = bottomRighty

        self.leftMostx = 0
        self.rightMostx = 0 
        self.topMosty = 0
        self.botMosty = 0

        self.topx = 0
        self.topy = 0

        self.updateEdges()

        self.lauv = "meme"

    def updateHitBox(self, topLeftx, topLefty, topRightx, topRighty, bottomLeftx, bottomLefty, bottomRightx, bottomRighty):
        self.topLeftx = topLeftx
        self.topLefty = topLefty
        self.topRightx = topRightx
        self.topRighty = topRighty
        self.bottomLeftx = bottomLeftx
        self.bottomLefty = bottomLefty
        self.bottomRightx = bottomRightx
        self.bottomRighty = bottomRighty

        self.updateEdges()

    def setEdges(self, leftMostx, rightMostx, topMosty, botMosty):
        self.leftMostx = leftMostx
        self.rightMostx = rightMostx
        self.topMosty = topMosty
        self.botMosty = botMosty

    def updateEdges(self):
        if self.topLeftx <= self.topRightx:
            if self.topLeftx <= self.bottomLeftx:
                #top left
                self.leftMostx = self.topLeftx
                self.rightMostx = self.bottomRightx
                self.botMosty = self.bottomLefty
                self.topMosty = self.topRighty
            else:
                #top right
                self.topMosty = self.topLefty
                self.leftMostx = self.bottomLeftx
                self.rightMostx = self.topRightx
                self.botMosty = self.bottomRighty
        else:
            if self.topRightx <= self.bottomRightx:
                #bot left
                self.rightMostx = self.bottomLeftx
                self.botMosty = self.topLefty
                self.leftMostx = self.topRightx
                self.topMosty = self.bottomRighty
            else:
                #bot right
                self.rightMostx = self.topLeftx
                self.leftMostx = self.bottomRightx
                self.topMosty = self.bottomLefty
                self.botMosty = self.topRighty

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
        #top and top
        if self.lineIntersect(self.topLeftx, self.topLefty, self.topRightx, self.topRighty, hitboxAdd.topLeftx, hitboxAdd.topLefty, hitboxAdd.topRightx, hitboxAdd.topRighty):
            return True
        #right and top
        elif self.lineIntersect(self.topRightx, self.topRighty, self.bottomRightx, self.bottomRighty, hitboxAdd.topLeftx, hitboxAdd.topLefty, hitboxAdd.topRightx, hitboxAdd.topRighty):
            return True
        #left and top
        elif self.lineIntersect(self.topLeftx, self.topLefty, self.bottomLeftx, self.bottomLefty, hitboxAdd.topLeftx, hitboxAdd.topLefty, hitboxAdd.topRightx, hitboxAdd.topRighty):
            return True
        #bottom and top
        elif self.lineIntersect(self.bottomLeftx, self.bottomLefty, self.bottomRightx, self.bottomRighty, hitboxAdd.topLeftx, hitboxAdd.topLefty, hitboxAdd.topRightx, hitboxAdd.topRighty):
            return True

        #top and right
        elif self.lineIntersect(self.topLeftx, self.topLefty, self.topRightx, self.topRighty, hitboxAdd.topRightx, hitboxAdd.topRighty, hitboxAdd.bottomRightx, hitboxAdd.bottomRighty):
            return True
        #right and right
        elif self.lineIntersect(self.topRightx, self.topRighty, self.bottomRightx, self.bottomRighty, hitboxAdd.topRightx, hitboxAdd.topRighty, hitboxAdd.bottomRightx, hitboxAdd.bottomRighty):
            return True
        #left and right
        elif self.lineIntersect(self.topLeftx, self.topLefty, self.bottomLeftx, self.bottomLefty, hitboxAdd.topRightx, hitboxAdd.topRighty, hitboxAdd.bottomRightx, hitboxAdd.bottomRighty):
            return True
        #bottom and right
        elif self.lineIntersect(self.bottomLeftx, self.bottomLefty, self.bottomRightx, self.bottomRighty, hitboxAdd.topRightx, hitboxAdd.topRighty, hitboxAdd.bottomRightx, hitboxAdd.bottomRighty):
            return True

        #top and left
        elif self.lineIntersect(self.topLeftx, self.topLefty, self.topRightx, self.topRighty, hitboxAdd.topLeftx, hitboxAdd.topLefty, hitboxAdd.bottomLeftx, hitboxAdd.bottomLefty):
            return True
        #right and left
        elif self.lineIntersect(self.topRightx, self.topRighty, self.bottomRightx, self.bottomRighty, hitboxAdd.topLeftx, hitboxAdd.topLefty, hitboxAdd.bottomLeftx, hitboxAdd.bottomLefty):
            return True
        #left and left
        elif self.lineIntersect(self.topLeftx, self.topLefty, self.bottomLeftx, self.bottomLefty, hitboxAdd.topLeftx, hitboxAdd.topLefty, hitboxAdd.bottomLeftx, hitboxAdd.bottomLefty):
            return True
        #bottom and left
        elif self.lineIntersect(self.bottomLeftx, self.bottomLefty, self.bottomRightx, self.bottomRighty, hitboxAdd.topLeftx, hitboxAdd.topLefty, hitboxAdd.bottomLeftx, hitboxAdd.bottomLefty):
            return True

        #top and bottom
        elif self.lineIntersect(self.topLeftx, self.topLefty, self.topRightx, self.topRighty, hitboxAdd.bottomLeftx, hitboxAdd.bottomLefty, hitboxAdd.bottomRightx, hitboxAdd.bottomRighty):
            return True
        #right and bottom
        elif self.lineIntersect(self.topRightx, self.topRighty, self.bottomRightx, self.bottomRighty, hitboxAdd.bottomLeftx, hitboxAdd.bottomLefty, hitboxAdd.bottomRightx, hitboxAdd.bottomRighty):
            return True
        #left and bottom
        elif self.lineIntersect(self.topLeftx, self.topLefty, self.bottomLeftx, self.bottomLefty, hitboxAdd.bottomLeftx, hitboxAdd.bottomLefty, hitboxAdd.bottomRightx, hitboxAdd.bottomRighty):
            return True
        #bottom and bottom
        elif self.lineIntersect(self.bottomLeftx, self.bottomLefty, self.bottomRightx, self.bottomRighty, hitboxAdd.bottomLeftx, hitboxAdd.bottomLefty, hitboxAdd.bottomRightx, hitboxAdd.bottomRighty):
            return True

        return False
        

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