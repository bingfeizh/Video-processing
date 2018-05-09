#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 14:43:04 2017

@author: bingfei
"""

import cv2
vidcap = cv2.VideoCapture('/Users/bingfei/project/Trajectory/Hong Kong/result.mp4')
success,image = vidcap.read()
count = 0
i=0
success = True
while success:
  success,image = vidcap.read()
  count += 1
  if count%24!=0:
      continue
  i=i+1
  print 'Read a new frame: '+str(count), success
  cv2.imwrite("/Users/bingfei/project/Trajectory/Hong Kong/resultvideo/"+str(count)+".jpg", image)     # save frame as JPEG file
  
  #if count==2333:
      #break