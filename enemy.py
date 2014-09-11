import pygame
import math
from Vector import Vector
from bullet import *

class Tracers:
	def __init__(self, game, enemy, player, count, frameOffset, speed, spriteName):
		self.name = 'Tracers'
		self.game = game
		game.gameObjects.append(self)
		self.enemy = enemy
		self.player = player
		self.count = count
		self.frameOffset = frameOffset
		self.speed = speed
		self.spriteName = spriteName
		self.frame = 0
		
	def update(self):
		if(self.frame%self.frameOffset == 0):
			LinearBullet(self.enemy.position, self.player.getPosition(), self.speed, self.game, self.spriteName)
			self.count-= 1
			if(self.count == 0):
				self.__del()
		self.frame+=1
	
	def draw(self, screen):
		return
		
	def flag(self):
		self.game.flag(self)

class TracersOffset:
	def __init__(self, game, enemy, player, offset, count, frameOffset, speed, spriteName):
		self.name = 'TracersOffset'
		self.game = game
		game.gameObjects.append(self)
		self.enemy = enemy
		self.player = player
		self.count = count
		self.frameOffset = frameOffset
		self.speed = speed
		self.spriteName = spriteName
		self.frame = 0
		self.offset = offset
		
	def update(self):
		if(frame%frameOffset == 0):
			LinearBullet(self.enemy.position, self.player.getPosition() + self.offset, self.speed, self.game, self.spriteName)
			self.count-=1
			if(self.count == 0):
				self.__del()
		self.frame+=1
	
	def draw(self, screen):
		return
		
	def flag(self):
		self.game.flag(self)
	
def BuckTarget(game, enemy, target, count, spread, speed, spriteName):
	t = target.copy()
	t.RotateAround(enemy.position, spread * (count - 1)/ 2)
	for n in range(count):
		b = LinearBullet(enemy.position, t, speed, game, spriteName)
		t.RotateAround(enemy.position, -spread)

def BuckDown(game, enemy, count, spread, speed, spriteName):
	BuckTarget(game, enemy, Vector(enemy.position.x, 10000) ,count, spread, speed, spriteName)

class Enemy:
	def __init__(self, init, game, player):
		self.name = 'Enemy'
		self.game = game
		game.gameObjects.append(self)
		self.player = player
		self.frame = 0
		self.position = init.copy()

	def draw(self, screen):
		if screen.get_rect().inflate(300,300).collidepoint(self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2):
			screen.blit(self.image, (self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2))
		else:
			self.flag()
			
	def get_rect(self):
		return self.image.get_rect().move(self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2)
			
	def flag(self):
		self.game.flag(self)
	
class SeagullA(Enemy):
	def __init__(self, init, game, player,count):
		Enemy.__init__(self, init, game, player)
		self.image = pygame.image.load("Art Stuff\\seagull.png").convert_alpha()
		self.count=count
	def update(self):
		if self.frame < 20:
			self.position.Add((0, 2))
		elif self.frame == 25:
			BuckTarget(self.game, self, self.player.getPosition(), self.count, math.radians(7.5), 5, "seashell")
		elif self.frame > 40:
			self.position.Add((0, -2))
		self.frame+=1
	
	def draw(self, screen):
		Enemy.draw(self, screen)
		
	def get_rect(self):
		return self.image.get_rect().move(self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2)
			
	def flag(self):
		Enemy.flag(self)
		
class SeagullB(Enemy):
	def __init__(self, init, game, player,count):
		Enemy.__init__(self, init, game, player)
		self.image = pygame.image.load("Art Stuff\\seagull.png").convert_alpha()
		self.count=count
	def update(self):
		if self.frame < 20:
			self.position.Add((0, -2))
		elif self.frame == 25:
			BuckTarget(self.game, self, self.player.getPosition(), self.count, math.radians(7.5), 5, "seashell")
		elif self.frame > 40:
			self.position.Add((0, 2))
		self.frame+=1
	
	def draw(self, screen):
		Enemy.draw(self, screen)
		
	def get_rect(self):
		return self.image.get_rect().move(self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2)
			
	def flag(self):
		Enemy.flag(self)
	
class PelicanA(Enemy):
	def __init__(self, init, game, player,timebetween,speed):
		Enemy.__init__(self, init, game, player)
		self.image = pygame.image.load("Art Stuff\\pelican.png").convert_alpha()
		self.t = None
		self.timebetween=timebetween
		self.speed=speed
	def update(self):
		self.position.Add((0, 5))
		if self.frame == 25:
			self.t = Tracers(self.game, self, self.player, 40, self.timebetween, self.speed, "rock")
		self.frame+=1
	
	def draw(self, screen):
		Enemy.draw(self, screen)
		
	def get_rect(self):
		return self.image.get_rect().move(self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2)
			
	def flag(self):
		Enemy.flag(self)
		if self.t != None:
			self.t.flag()
			
class PelicanB(Enemy):
	def __init__(self, init, game, player,timebetween,speed):
		Enemy.__init__(self, init, game, player)
		self.image = pygame.image.load("Art Stuff\\pelican.png").convert_alpha()
		self.t = None
		self.timebetween=timebetween
		self.speed=speed
	def update(self):
		self.position.Add((0, -5))
		if self.frame == 25:
			self.t = Tracers(self.game, self, self.player, 40, self.timebetween, self.speed, "rock")
		self.frame+=1
	
	def draw(self, screen):
		Enemy.draw(self, screen)
		
	def get_rect(self):
		return self.image.get_rect().move(self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2)
			
	def flag(self):
		Enemy.flag(self)
		if self.t != None:
			self.t.flag()
						
class PelicanC(Enemy):
	def __init__(self, init, game, player,timebetween,speed):
		Enemy.__init__(self, init, game, player)
		self.image = pygame.image.load("Art Stuff\\pelican.png").convert_alpha()
		self.timebetween=timebetween
		self.speed=speed;
	def update(self):
		self.position.Add((0, 5))
		if self.frame%self.timebetween==0:
			LinearBullet(self.position,Vector(400-self.position.x,self.position.y),self.speed,self.game,"rock");
		self.frame+=1
	
	def draw(self, screen):
		Enemy.draw(self, screen)
		
	def get_rect(self):
		return self.image.get_rect().move(self.position.x - self.image.get_width()/2, self.position.y - self.image.get_height()/2)
			
	def flag(self):
		Enemy.flag(self)

class HummingbirdA(Enemy):
	def __init__(self, init,game,player,direction,buck,timebetween):
		Enemy.__init__(self,init,game,player)
		self.image=pygame.image.load("Art Stuff\\hummingbird.png").convert_alpha()
		self.direction=direction
		self.buck=buck
		self.timebetween=timebetween
	def update(self):
		if self.frame<25:
			self.position.Add((0,2))
		else:
			self.position.Add((self.direction*4,0))
		if self.position.x>=570:
			self.direction=-1
		if self.position.x<=30:
			self.direction=1
		if (self.frame-25)%self.timebetween==0:
			BuckTarget(self.game,self,Vector(self.position.x,99999),self.buck,math.radians(7.5),5,"seashell")
		self.frame+=1
	
	def draw(self, screen):
		Enemy.draw(self, screen)
	
	def get_rect(self):
		return self.image.get_rect().move(self.position.x-self.image.get_width()/2,self.position.y-self.image.get_height()/2)
		
class HummingbirdB(Enemy):
	def __init__(self, init,game,player,direction,buck,timebetween):
		Enemy.__init__(self,init,game,player)
		self.image=pygame.image.load("Art Stuff\\hummingbird.png").convert_alpha()
		self.direction=direction
		self.buck=buck
		self.timebetween=timebetween
	def update(self):
		if self.frame<25:
			self.position.Add((0,2))
		else:
			self.position.Add((self.direction*4,0))
		if self.position.x>=570:
			self.direction=-1
		if self.position.x<=30:
			self.direction=1
		if (self.frame-25)%self.timebetween==0:
			BuckTarget(self.game,self,self.player.getPosition(),self.buck,math.radians(7.5),5,"seashell")
		self.frame+=1
	
	def draw(self, screen):
		Enemy.draw(self, screen)
	
	def get_rect(self):
		return self.image.get_rect().move(self.position.x-self.image.get_width()/2,self.position.y-self.image.get_height()/2)

class HummingbirdC(Enemy):
	def __init__(self, init,game,player,direction,buck,timebetween):
		Enemy.__init__(self,init,game,player)
		self.image=pygame.image.load("Art Stuff\\hummingbird.png").convert_alpha()
		self.direction=direction
		self.buck=buck
		self.timebetween=timebetween
	def update(self):
		if self.frame<25:
			self.position.Add((0,2))
		else:
			self.position.Add((self.direction*4,2))
		if self.position.x>=570:
			self.direction=-1
		if self.position.x<=30:
			self.direction=1
		if (self.frame-25)%self.timebetween==0:
			BuckTarget(self.game,self,self.player.getPosition(),self.buck,math.radians(7.5),5,"seashell")
		self.frame+=1
	
	def draw(self, screen):
		Enemy.draw(self, screen)
	
	def get_rect(self):
		return self.image.get_rect().move(self.position.x-self.image.get_width()/2,self.position.y-self.image.get_height()/2)
		
class DoveA(Enemy):
	def __init__(self,init,game,player):
		Enemy.__init__(self,init,game,player)
		self.image=pygame.image.load("Art Stuff\\dove.png").convert_alpha()
	def update(self):
		if self.frame<25:
			self.position.Add((0,2))
		else:
			if self.position.x<self.player.rect.x+16:
				self.position.Add((2,0))
			if self.position.x>self.player.rect.x+16:
				self.position.Add((-2,0))
			if self.position.y<self.player.rect.y+24:
				self.position.Add((0,2))
			if self.position.y>self.player.rect.y+24:
				self.position.Add((0,-2))
		self.frame+=1
			
	def draw(self,screen):
		Enemy.draw(self,screen)
	
	def get_rect(self):
		return self.image.get_rect().move(self.position.x-self.image.get_width()/2,self.position.y-self.image.get_height()/2)