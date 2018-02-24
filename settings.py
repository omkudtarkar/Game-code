import pygame

player_acc= 0.5
player_friction = -0.1
player_grav = 0.8


Title = 'Game'
width = 480
height = 600
fps = 60
Font_name = 'freesansbold.ttf'
Hs_file = "highschore.txt"

platform_list =[(0, height - 40, width, 40), 
				(width /2 - 50, height *3 / 4, 100, 20),
				(125, height -350, 100, 20),
				(350, 200, 100, 20),
				(175, 100, 50, 20)]


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)