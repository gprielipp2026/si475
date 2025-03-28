# Spring 2024 SI 475
# GEORGE PRIELIPP, 265112

import numpy as np
import cv2 as cv
import math

# This function applys the brightness and contrast 
# settings to the provided image.  
# Input: 
#   I: an image as a Numpy N-dimensional array 
#   brightness: how much to change the brightness by
#       integer in the range [-255, 255] 
#   contrast: how much to change the contrast by 
#       floating point (a value of 1.0 will not change
#       the contrast 
# 
# Returns: 
#   a new image showing the results of applying the 
#       the supplied brightness and contrast settings 

def adjust_image(I, brightness, contrast): 
    # create a blank image to modify
    newimg = np.zeros(I.shape, I.dtype)

    # function to transform
    transform = lambda x: x * contrast + brightness
    
    # I.shape => (width, height, channels)
    cols, rows, channels = I.shape
    for col in range(cols):
        for row in range(rows):
            for channel in range(channels):
                newimg[col][row][channel] = np.clip(transform(I[col][row][channel]), a_min=0, a_max=255)

    return newimg

# This function applys a filter to an image 
# Input: 
#   I: an image as a Numpy N-dimensional array 
#   h: the filter (kernel) as a 2-D Numpy array 
#
# Returns: 
#   a new image showing the results of applying the 
#       the filter to the image I 
def apply_filter(I, h): 
    # create a blank image to modify
    newimg = np.zeros(I.shape, I.dtype)
   
    transform = lambda col, row, channel: sum([h[1 + offy][1 + offx] * I[col + offx][row + offy][channel] for offx, offy in zip([-1,0,1,-1,0,1,-1,0,1], [-1,-1,-1,0,0,0,1,1,1])])

    # I.shape => (width, height, channels)
    cols, rows, channels = I.shape
    for col in range(1, cols-1):
        for row in range(1, rows-1):
            for channel in range(channels):
                newimg[col][row][channel] = np.clip(transform(col, row, channel), a_min=0, a_max=255)
    

    return newimg

# This function rotates an image by theta 
# Input: 
#   I: an image as a Numpy N-dimensional array 
#   theta (integer): number of degrees to rotate the image 
#
# Returns: 
#   a new image which is the rotated version of I 

def rotate_image(I, theta): 
    # create a blank image to modify
    cols, rows, channels = I.shape

    theta = np.deg2rad(theta)
    rotmat = np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0,0,1]], dtype='float64')

    centerRow = rows // 2
    centerCol = cols // 2

    center = np.array([[1, 0, -centerCol], [0, 1, -centerRow], [0, 0, 1]], dtype='float64')
    topleft = np.array([[1, 0, centerCol], [0, 1, centerRow], [0, 0, 1]], dtype='float64')
    
    newimg = np.zeros([rows, cols, channels], I.dtype)
    
    # translate, rotate, translate
    matrix = np.matmul(topleft, np.matmul(center, rotmat))
    
    for col in range(cols):
        for row in range(rows):
            point = np.matmul(matrix, [col, row, 1])
            rotcol, rotrow = round(point[0]), round(point[1])
            
            if rotcol >= cols:
                rotcol = cols - 1
            if rotrow >= rows:
                rotrow = rows - 1
            
            newimg[rotcol][rotrow] = I[col][row]

    return newimg

# Compute the Differece of Gaussians on a single image
# Input: 
#   I: an image as a Numpy N-dimensional array 
#   sigma1: standard deviation of the first Gaussian 
#   sigma2: standard deviation of the second Gaussian 
#
# Returns: 
#   a new image showing the computed Difference of Gaussians 

def dog (I, sigma1, sigma2): 
    size = (5,5)
    blur1 = cv.GaussianBlur(I, size, sigma1) 
    blur2 = cv.GaussianBlur(I, size, sigma2)
    return blur1 - blur2
