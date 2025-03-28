#!/usr/bin/env python3

from lab01 import *

import numpy as np
import cv2 as cv
import random

sharpen = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]], dtype='float64')
blur    = np.array([[1/9.0]*3]*3, dtype='float64')
edges   = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]], dtype='float64')

#img = cv.imread('usna_small.jpg')

#cv.imshow('My First Image', img)

#img2 = adjust_image(img, 0, 0.5)

#cv.imshow('My Second Image', img2)

#img3 = apply_filter(img, edges)

#cv.imshow('My Third Image', img3)

#img = cv.imread('osprey_square.jpg')


#for angle in range(0,360, 90):
    #img4 = rotate_image(img, angle)
    #cv.imshow(f'Rotated {angle} degrees', img4)

sigmas = [(x, y) for x in range(3) for y in range(3)]
img = cv.imread('usna_small.jpg')
for s1, s2 in sigmas:
    cv.imshow(f'Blurs: ({s1}, {s2})', dog(img, s1, s2))

k = cv.waitKey(0)

