import pygame, sys
from classes import *
from process import *

pygame.init()
SCREENWIDTH, SCREENHEIGHT = 640, 360
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)
clock = pygame.time.Clock()
FPS = 25
total_frames = 0
background = pygame.image.load("images/forest.jpg")
bug = Bug(0, SCREENHEIGHT - 40, "images/bug.png")
while True:
	pygame.display.set_caption('Fly Swatter Game')
	process(bug, FPS, total_frames)
	bug.motion(SCREENWIDTH, SCREENHEIGHT)
	Fly.update_all(SCREENWIDTH, SCREENHEIGHT)
	BugProjectile.movement()
	total_frames += 1
	screen.blit(background, (0, 0))
	BaseClass.allsprites.draw(screen)
	BugProjectile.List.draw(screen)
	pygame.display.flip()
	clock.tick(FPS)
