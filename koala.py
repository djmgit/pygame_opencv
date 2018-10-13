import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

pygame.display.set_caption('koala')
clock = pygame.time.Clock()

carImg = pygame.image.load('images/race_car.png')
carImg = pygame.transform.scale(carImg, (100, 100))
