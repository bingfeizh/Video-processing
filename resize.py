#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 18:32:16 2017

@author: bingfei
"""

from PIL import Image

for i in range(1491):
    img=Image.open('/Users/bingfei/project/Trajectory/Exca Traj/Trajectory/'+str(i)+'.jpg')
    region = (900,600,900+1278,600+718)
    cropImg = img.crop(region)
    cropImg.save(r'/Users/bingfei/project/Trajectory/Exca Traj/rezise/'+str(i)+'.jpg')
    print(i)
