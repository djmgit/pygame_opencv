import pygame
import numpy as np
import cv2

import random

pygame.init()
clock = pygame.time.Clock()



white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

display_width = 800
display_height = 600

line = []

gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(white)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

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

def draw_line():
    if len(line) <= 1:
        return
    prev = line[0]
    for point in line[1:]:
        curr = point
        pygame.draw.line(gameDisplay, blue, prev, curr, 5)
        prev = curr



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #line_x = random.randrange(0, display_width)
    #line_y = random.randrange(0, display_height)

    res = getface()
   
    if res:
        line_x, line_y = res
        line.append((line_x, line_y))
        draw_line()
    #print (len(line))

    pygame.display.update()
    clock.tick(30)

