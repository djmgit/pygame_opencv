import pygame
import time
import random
import cv2

pygame.init()

display_width = 800
display_height = 600

# some colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# setup pygame display
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('koala')
clock = pygame.time.Clock()

# load image
koala_img = pygame.image.load('images/koala.png')
koala_img = pygame.transform.scale(koala_img, (100, 100))

trophies_img = [
    'images/trophy1.jpg',
    'images/trophy2.png',
    'images/trophy3.jpeg',
    'images/trophy4.png'
]

trohpies = []
for img in trophies_img:
    trophy = pygame.image.load(img)
    trophy = pygame.transform.scale(trophy, (100, 100))
    trohpies.append(trophy)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

# nethod to get face boundary
def getface():
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print (faces)
    
    if len(faces) != 0:
        face = faces[0]
        x, y, w, h = face
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('img',img)
        k = cv2.waitKey(30) & 0xff
        face_x = x + (w / 2)
        face_y = y + (h / 2)

        return (face_x, face_y)
    else:
        cv2.imshow('img',img)
        k = cv2.waitKey(30) & 0xff
        return None

# draw image asset
def koala(x,y):
    gameDisplay.blit(koala_img,(x,y))

def draw_trophy(trophy_img, x, y):
    gameDisplay.blit(trophy_img,(x,y))

# main game loop
def game_loop():

    koala_x = display_width / 2
    koala_y = display_height / 2

    trophy = trohpies[random.randrange(0, 4)]
    trophy_x = random.randrange(0, display_width)
    trophy_y = random.randrange(0, display_height)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        res = getface()
   
        if res:
            koala_x, koala_y = res

        draw_trophy(trophy, trophy_x, trophy_y)
        koala(koala_x,koala_y)
            
        
        pygame.display.update()
        clock.tick(60)



game_loop()
pygame.quit()
quit()
