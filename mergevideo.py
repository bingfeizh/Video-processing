#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 11:06:19 2017

@author: bingfei
"""

from moviepy.editor import VideoFileClip, clips_array,vfx


clip1 = VideoFileClip("/Users/bingfei/project/Trajectory/Exca Traj/Result/result.mp4",10)
clip2 = VideoFileClip("/Users/bingfei/project/Trajectory/Exca Traj/rezise/Map.mp4")
#clip3 = VideoFileClip("/Users/bingfei/project/Matching/Fairbank/Tracking/3/tracking 3.mp4")


final_clip = clips_array([[clip1],[clip2]])
final_clip.write_videofile("/Users/bingfei/project/Trajectory/Exca Traj/Result.mp4", fps=24)