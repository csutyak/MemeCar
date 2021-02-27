import pyglet
from pyglet.window import key
from memeCar import memeCar
from gameObject import GameObject 
from walls import walls

class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(0, 0)
        self.frame_rate = 1/60.0

        self.player = memeCar(500, 100, 0, 'nyoom.png')
        self.wallPosArr = [[[17, 1080 - 991],[24, 1080 - 98]],
        	[[24, 1080 - 95],[216, 1080 - 36]],
        	[[220, 1080 - 36],[1669, 1080 - 37]],
        	[[1669, 1080 - 37],[1819, 1080 - 89]],
        	[[1819, 1080 - 89],[1872, 1080 - 153]],
        	[[1872, 1080 - 153],[1876, 1080 - 954]],
        	[[1876, 1080 - 954],[1655, 1080 - 1046]],
        	[[1655, 1080 - 1046],[683, 1080 - 1052]],
        	[[683, 1080 - 1052],[603, 1080 - 999]],
        	[[603, 1080 - 999],[611, 1080 - 564]],
        	[[611, 1080 - 564],[1250, 1080 - 534]],
        	[[1250, 1080 - 534],[1341, 1080 - 686]],
        	[[1341, 1080 - 686],[1517, 1080 - 704]]
        	]

        self.collision = False
        self.labelBatch = pyglet.graphics.Batch()
       	self.inRangeLabel = pyglet.text.Label("Collision: ", x= 1650, y =600, batch=self.labelBatch)
        self.inRangeValue = pyglet.text.Label(str(self.collision), x= 1750, y =600, batch=self.labelBatch)

        self.wallImageArr = []
        self.wallObj = walls(self.wallPosArr)

        trackimage = pyglet.image.load('Res/sprites/Track.png')
        self.trackbackground = pyglet.sprite.Sprite(trackimage, x=0, y = 0)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.player.keyUP = True
        if symbol == key.DOWN:
            self.player.keyDOWN = True
        if symbol == key.LEFT:
            self.player.keyLEFT = True
        if symbol == key.RIGHT:
            self.player.keyRIGHT = True
        if symbol == key.SPACE:
            self.player.keySPACE = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.player.keyUP = False
        if symbol == key.DOWN:
            self.player.keyDOWN = False
        if symbol == key.LEFT:
            self.player.keyLEFT = False
        if symbol == key.RIGHT:
            self.player.keyRIGHT = False
        if symbol == key.SPACE:
            self.player.keySPACE = False

    def on_draw(self):
        self.clear()
        self.trackbackground.draw()
        self.wallObj.draw()
        self.player.draw()
        self.labelBatch.draw()

    def update(self, dt):
        self.player.update(dt)
        if self.wallObj.checkCollision(self.player.carHitbox):
        	self.collision = True
        else:
        	self.collision = False
        self.inRangeValue.text = str(self.collision)



if __name__ == "__main__":
    window = GameWindow(1920, 1080, "meme car", resizable=True, fullscreen=False)
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()