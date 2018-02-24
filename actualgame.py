import pygame as pg
import random

from settings import *
from sprites import *
from os import path 
from var import *

class Game: 
	def __init__(self):
		pg.init()
		pg.mixer.init()
		self.screen = pg.display.set_mode((width, height))
		pg.display.set_caption(Title)
		self.clock = pg.time.Clock()
		self.running = True
		self.font_name = pg.font.match_font(Font_name)


	def new(self):
		self.score = 0
		self.all_sprites = pg.sprite.Group()
		self.platforms = pg.sprite.Group()
		self.player = Player(self)
		self.all_sprites.add(self.player)
		for plat in platform_list:
			p = Platform(*plat)
			self.all_sprites.add(p)
			self.platforms.add(p)
		self.run()

	def run(self):
		self.playing = True
		while self.playing:
			self.clock.tick(fps)
			self.events()
			self.update()
			self.draw()

	def update(self):
		self.all_sprites.update() 
		if self.player.vel.y > 0:
			hits = pg.sprite.spritecollide(self.player , self.platforms, False)
			if hits:
				self.player.pos.y = hits[0].rect.top +1
				self.player.vel.y = 0
		if self.player.rect.top <= height / 4 :
			self.player.pos.y += abs(self.player.vel.y)
			for plat in self.platforms:
				plat.rect.y += abs (self.player.vel.y)
				if plat.rect.top >= height:
					plat.kill()
					self.score += 10

		if self.player.rect.bottom> height:
			for sprite in self.all_sprites:
				sprite.rect.y -= max(self.player.vel.y, 10)
				if sprite.rect.bottom<0:
					sprite.kill()
		if len(self.platforms) == 0:
			self.playing = False

		while len(self.platforms) < 6:
			Width = random.randrange(50, 100)
			p = Platform(random.randrange(0, width- Width), random.randrange(-75, -30), Width, 20)
			self.platforms.add(p)
			self.all_sprites.add(p)

	def events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				if self.playing:
					self.playing = False
				self.running = False
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_SPACE:
					self.player.jump()

	def draw(self):
		self.screen.fill(black)
		self.all_sprites.draw(self.screen)
		self.draw_text(str(self.score),22, white, width/2, 20)
		pg.display.update()

	def show_start_screen(self):
		self.screen.fill(red)
		self.draw_text(Title, 90, black, width /2, 4)
		self.draw_text('Press any key to go to the tutorial', 22, white, width /2, height *3/4)
		pg.display.update()
		self.wait_for_key()


	def tutorial(self):
		self.screen.fill(blue)
		self.draw_text('Tutorial', 90, white, width/2, 10)
		self.draw_text('Arrows to move left and right', 22, white, width/2, height *3/8)
		self.draw_text('Space bar to jump', 22, white, width /2, height* 1/2)
		self.draw_text('Press any key to begin your journey', 22, white, width/2, height *3/4)
		pg.display.update()
		self.wait_for_key()



	def show_go_screen(self):
		if not self.running:
			return
		self.screen.fill(red)
		self.draw_text('Gameover', 90, black, width /2, 10)
		self.draw_text('Your score was '+ str(self.score), 30, black, width /2, height *1/2 )
		self.draw_text('Press any key to play again', 30, black, width /2, height *3/4)
		pg.display.update()
		self.wait_for_key()

	def wait_for_key(self):
		waiting = True
		while waiting:
			self.clock.tick(fps)
			for event in pg.event.get():
				if event.type == pg.QUIT:
					waiting = False
					self.running = False
				if event.type == pg.KEYUP:
					waiting = False


	def draw_text(self, text, size, color, x, y):
		font = pg.font.Font('freesansbold.ttf',size)
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect()
		text_rect.midtop = (x, y)
		self.screen.blit(text_surface, text_rect)

g = Game()
g.show_start_screen()
g.tutorial()
while g.running :
	g.new()
	g.show_go_screen()
pg.quit()

