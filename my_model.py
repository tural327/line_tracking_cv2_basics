#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 10:10:54 2021

@author: tural
"""

import cv2 
import numpy as np



def marked(img,vertices): # function for creating some triangle on picture
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv2.fillPoly(mask,vertices,match_mask_color)
    masked_image = cv2.bitwise_and(img,mask)
    return masked_image

def line(image):
    hegiht = image.shape[0]
    width = image.shape[1]
    region_of_intrest_vertices1 = [ #function for making triangle1 params 
            (0,hegiht),
            (width/6,hegiht/2),
            (width,hegiht)
            ]
    
    region_of_intrest_vertices2 = [ #triangle2 params
            (0,hegiht),
            (width/2,hegiht/2.2),
            (width,hegiht)
            ]
    
    

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # For shape detection we should conver to gray
    
    edges = cv2.Canny(gray,255,255) # image shape detected
    
   
    
    cropped_image1 = marked(edges,
                                      np.array([region_of_intrest_vertices1], np.int32)) #triangle1
    
    cropped_image2 = marked(edges,
                                      np.array([region_of_intrest_vertices2], np.int32)) # triangle2
    
    lines1 = cv2.HoughLinesP(cropped_image1,1,np.pi/180, 50,minLineLength=10,maxLineGap=300) #line for left side 
    
    lines2 = cv2.HoughLinesP(cropped_image2,1,np.pi/180, 50,minLineLength=10,maxLineGap=300) # line for right side
    # Then we are making lines for each section and apply on our frame
    for line1 in lines1:
        x1_1,y1_1,x2_1,y2_1 = line1[0]
        
        cv2.line(image,(x1_1,y1_1),(x2_1,y2_1),(0,255,0),3 )
        
        
    for line2 in lines2:
        x1_2,y1_2,x2_2,y2_2 = line2[0]
        cv2.line(image,(x1_2,y1_2),(x2_2,y2_2),(0,255,0),3 )
        
    
    return image
cap = cv2.VideoCapture("highway-401-toronto-canada-driving.mp4")

while True:
    ret, image = cap.read()
# while video starting some ADV. occurs and it made error while finding edge for avioding it i used try method
    try:
        frame = line(image)
        cv2.imshow("frame",frame)
    except:
        cv2.imshow("frame",image)
        
    

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
  
   
cap.release()
cv2.destroyAllWindows()
    
