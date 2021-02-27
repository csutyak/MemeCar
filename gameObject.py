import pyglet

class GameObject:
	def __init__(self, posx, posy, rotation = 10,  image = None):
		self.posx = posx
		self.posy = posy
		self.direction = 0
		self.velx = 0
		self.vely = 0
		if image is not None:
			image = pyglet.image.load('Res/sprites/' + image)
            
			self.sprite = pyglet.sprite.Sprite(image, x=self.posx, y = self.posy)

	def draw(self):
		self.sprite.draw()

	def update(self, dt):
		self.sprite.x += self.velx * dt
		self.sprite.y += self.vely * dt