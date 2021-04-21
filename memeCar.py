import pyglet
import math
from hitbox import hitbox

class memeCar:
    def __init__(self, posx, posy, rotation, image = None):
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0
        self.rotation =  rotation

        self.labelBatch = pyglet.graphics.Batch()
        self.dotBatch = pyglet.graphics.Batch()

        self.rotationNameLabel = pyglet.text.Label("rotation: ", x= 1650, y =1000, batch=self.labelBatch)
        self.rotationValue = pyglet.text.Label(str(rotation), x= 1750, y =1000, batch=self.labelBatch)

        self.yposNameLabel = pyglet.text.Label("x pos: ", x= 1650, y =950, batch=self.labelBatch)
        self.yposValue = pyglet.text.Label(str(posy), x= 1750, y =950, batch=self.labelBatch)

        self.xposNameLabel = pyglet.text.Label("y pos: ", x= 1650, y =900, batch=self.labelBatch)
        self.xposValue = pyglet.text.Label(str(posx), x= 1750, y =900, batch=self.labelBatch)

        self.centripitalAcceleration = 5
        self.centripitalDeceleration = 10
        self.leftMaxDriftVelocity = 200

        self.rightDriftVelocity = 0
        self.leftDriftVelocity = 0
        self.driftTurnRate = 400

        self.carHitbox = hitbox(posx, posy + 17, posx, posy, posx, posy, posx + 17, posy)

        self.hitBoxTopLeft = [posx, posy + 17]
        self.hitBoxTopRight = [posx, posy]
        self.hitBoxBottomLeft = [posx, posy]
        self.hitBoxBottomRight = [posx + 17, posy]

        self.hitboxTopLeftNameLabel = pyglet.text.Label("Top Left: ", x= 1500, y =850, batch=self.labelBatch)
        self.hitboxTopLeftLabel = pyglet.text.Label(str(posx), x= 1600, y =850, batch=self.labelBatch)
        self.hitboxTopLeftLabel1 = pyglet.text.Label(str(posx), x= 1800, y =850, batch=self.labelBatch)

        self.hitboxTopRightNameLabel = pyglet.text.Label("Top Right: ", x= 1500, y =800, batch=self.labelBatch)
        self.hitboxTopRightLabel = pyglet.text.Label(str(posx), x= 1600, y =800, batch=self.labelBatch)
        self.hitboxTopRightLabel1 = pyglet.text.Label(str(posx), x= 1800, y =800, batch=self.labelBatch)

        self.hitboxBottomLeftNameLabel = pyglet.text.Label("Bottom Left: ", x= 1500, y =750, batch=self.labelBatch)
        self.hitboxBottomLeftLabel = pyglet.text.Label(str(posx), x= 1600, y =750, batch=self.labelBatch)
        self.hitboxBottomLeftLabel1 = pyglet.text.Label(str(posx), x= 1800, y =750, batch=self.labelBatch)

        self.hitboxBottomRightNameLabel = pyglet.text.Label("Bottom Right: ", x= 1500, y =700, batch=self.labelBatch)
        self.hitboxBottomRightLabel = pyglet.text.Label(str(posx), x= 1600, y =700, batch=self.labelBatch)
        self.hitboxBottomRightLabel1 = pyglet.text.Label(str(posx), x= 1800, y =700, batch=self.labelBatch)

        self.keyUP = False
        self.keyDOWN = False
        self.keyLEFT = False
        self.keyRIGHT = False
        self.keySPACE = False

        if image is not None:
            image = pyglet.image.load('Res/sprites/' + image)
            image.anchor_x = 8
            image.anchor_y = 20
            self.sprite = pyglet.sprite.Sprite(image, x=self.posx, y = self.posy)

        image = pyglet.image.load('Res/sprites/dot.png')
        self.dot1 = pyglet.sprite.Sprite(image, x=self.carHitbox.topLeftx, y = self.carHitbox.topLefty, batch = self.dotBatch)
        self.dot2 = pyglet.sprite.Sprite(image, x=self.carHitbox.topRightx, y = self.carHitbox.topRighty, batch = self.dotBatch)
        self.dot3 = pyglet.sprite.Sprite(image, x=self.carHitbox.bottomLeftx, y = self.carHitbox.bottomLefty, batch = self.dotBatch)
        self.dot4 = pyglet.sprite.Sprite(image, x=self.carHitbox.bottomRightx, y = self.carHitbox.bottomRighty, batch = self.dotBatch)

        self.image_hyp = 22

        self.forwardVel = 0
        self.maxForwardVel = 500
        self.maxBackwardVel = -300
        self.acceleration = 5
        self.deceleration = 10
        self.driftDeceleration = 5

        self.maxRightVel = 200
        self.maxLeftVel = 200

        
        self.rotationSpeed = 200
        self.rotationSpeedSet = 150

    def draw(self):
        self.sprite.draw()
        self.labelBatch.draw()   
        self.dotBatch.draw()

    def update(self, dt):
        if self.keyUP and not self.keySPACE:
            self.forwardMotion(True)
        elif self.forwardVel > 0:
            self.forwardMotion(False)

        if self.keyDOWN:
            self.backwardMotion(True)
        elif self.forwardVel < 0:
            self.backwardMotion(False)

        if self.keySPACE:
            self.rotationSpeed = self.driftTurnRate
        else:
            self.rotationSpeed = self.rotationSpeedSet

        if self.forwardVel >= 0 or self.leftDriftVelocity >= 0:
            if self.keyLEFT:
                self.rotate(True, dt)
                if self.forwardVel >= 0:
                    if self.keySPACE or self.forwardVel >= 900:
                        self.accelerateLeft(True)
            else:
                self.accelerateLeft(False)
            if self.keyRIGHT:
                self.rotate(False, dt)
                if self.forwardVel >= 0:
                    if self.keySPACE or self.forwardVel >= 900:
                        self.accelerateRight(True)
            else:
                self.accelerateRight(False)

        elif self.forwardVel < 0:
            if self.keyLEFT:
                self.rotate(False, dt)
            if self.keyRIGHT:
                self.rotate(True, dt)

        if self.velx < 10 and self.velx > -10:
            self.velx = 0
        if self.vely < 10 and self.vely > -10:
            self.vely = 0

        self.calculateVelocity()
        calculatedVelx = self.velx * dt
        calculatedVely = self.vely * dt
        self.sprite.x += self.velx * dt
        self.sprite.y += calculatedVely

        self.rotationValue.text = (str(self.rotation))
        self.xposValue.text = (str(self.sprite.y))
        self.yposValue.text = (str(self.sprite.x))

        radians = math.radians(self.rotation + 90)
        self.carHitbox.topLeftx = self.sprite.x - (self.image_hyp * math.sin(-1 * (math.radians(self.rotation - 22))))          
        self.carHitbox.topLefty = self.sprite.y + (self.image_hyp * math.cos(math.radians(self.rotation - 22))) 
        self.carHitbox.topRightx = self.sprite.x + (self.image_hyp * math.sin(math.radians(self.rotation + 22)))        
        self.carHitbox.topRighty = self.sprite.y + (self.image_hyp * math.cos(-1 * math.radians(self.rotation + 22))) 
        self.carHitbox.bottomLeftx = self.sprite.x - (self.image_hyp * math.sin(math.radians(self.rotation + 22)))       
        self.carHitbox.bottomLefty = self.sprite.y - (self.image_hyp * math.cos(-1 * math.radians(self.rotation + 22)))  
        self.carHitbox.bottomRightx = self.sprite.x + (self.image_hyp * math.sin(-1 * (math.radians(self.rotation - 22))))       
        self.carHitbox.bottomRighty = self.sprite.y - (self.image_hyp * math.cos ((math.radians(self.rotation - 22))))     

        self.hitboxTopLeftLabel.text = str(self.carHitbox.topLeftx) 
        self.hitboxTopLeftLabel1.text = str(self.carHitbox.topLefty) 
        self.hitboxTopRightLabel.text = str(self.carHitbox.topRightx)
        self.hitboxTopRightLabel1.text = str(self.carHitbox.topRighty)
        self.hitboxBottomLeftLabel.text = str(self.carHitbox.bottomLeftx)
        self.hitboxBottomLeftLabel1.text = str(self.carHitbox.bottomLefty)
        self.hitboxBottomRightLabel.text = str(self.carHitbox.bottomRightx)
        self.hitboxBottomRightLabel1.text = str(self.carHitbox.bottomRighty)

        self.dot1.x = self.carHitbox.topLeftx
        self.dot1.y = self.carHitbox.topLefty
        self.dot2.x = self.carHitbox.topRightx
        self.dot2.y = self.carHitbox.topRighty
        self.dot3.x = self.carHitbox.bottomLeftx
        self.dot3.y = self.carHitbox.bottomLefty
        self.dot4.x = self.carHitbox.bottomRightx
        self.dot4.y = self.carHitbox.bottomRighty

        self.carHitbox.updateEdges()

        self.sprite.update(rotation = self.rotation)

    def forwardMotion(self, accelerate):
        if accelerate:
            if self.forwardVel < self.maxForwardVel:
                self.forwardVel += self.acceleration
        else:
            if self.forwardVel > 0:
                if self.keySPACE:
                    self.forwardVel -= self.driftDeceleration
                else:
                    self.forwardVel -= self.deceleration
                

    def backwardMotion(self, accelerate):
        if accelerate:
            if self.forwardVel > self.maxBackwardVel:
                self.forwardVel -= self.acceleration
        else:
            if self.forwardVel < 0:
                self.forwardVel += self.acceleration

    def rotate(self, leftRight, dt):
        if leftRight:
            self.rotation -= dt * self.rotationSpeed 
        else:
            self.rotation += dt * self.rotationSpeed 
        if self.rotation >= 360 or self.rotation <= -360:
            self.rotation = 0

    def accelerateLeft(self, accelerate):
        if accelerate:
            if self.leftDriftVelocity < self.leftMaxDriftVelocity:
                self.leftDriftVelocity += self.centripitalAcceleration
        else:
            if self.leftDriftVelocity > 0:
                self.leftDriftVelocity -= self.centripitalAcceleration

    def accelerateRight(self, accelerate):
        if accelerate:
            if self.leftDriftVelocity > (-1 * self.leftMaxDriftVelocity):
                self.leftDriftVelocity -= self.centripitalAcceleration
        else:
            if self.leftDriftVelocity < 0:
                self.leftDriftVelocity += self.centripitalAcceleration

    

    def calculateVelocity(self):
        radians = math.radians(self.rotation)
        radians90 = math.radians(self.rotation + 90)
        self.velx = (self.forwardVel * math.sin(radians)) + (self.leftDriftVelocity * math.sin(radians90))
        self.vely = (self.forwardVel * math.cos(radians)) + (self.leftDriftVelocity * math.cos(radians90))