#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 11:51:16 2017

@author: bingfei
"""

import cv2

img1 = cv2.imread("/Users/bingfei/project/worker/left/1.jpg")

height , width , layers =  img1.shape

video = cv2.VideoWriter('video.mp4',-1,1,(width,height))


for i in range(240):
    img=cv2.imread("/Users/bingfei/project/worker/left/"+str(i+1)+".jpg" )
    video.write(img)


cv2.destroyAllWindows()
video.release()