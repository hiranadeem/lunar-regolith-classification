'''
This code is used to crop rectangular images that are height 500 to squaers of 
500x500.

Source:
https://www.geeksforgeeks.org/how-to-iterate-through-images-in-a-folder-python/
'''

import cv2
import os
from os import listdir

SCALE = 512 # change to 512 or 1024
NUM_CROP_X = 5 # 3 for 1024, 5 for 512
NUM_CROP_Y = 4 # 2 for 1024, 4 for 512
MISSION = "apollo14_"
PAIR = "B_"

# variables for crop dimension
y = 0
x = 0
h = SCALE
w = SCALE
file_num = 1

# cropped image directory
# crop_dir = "/Users/hiranadeem/Documents/Thesis/apollo_imgs/apollo_11/test/test_crop/"
# crop_dir = "/Users/hiranadeem/Documents/Thesis/apollo_imgs/apollo_14/crop_a_512/"
crop_dir = "/Users/hiranadeem/Documents/Thesis/apollo_imgs/test/"

# iterate through all images in order in the data folder and crop them. Output the cropped image
# folder_dir = "/Users/hiranadeem/Documents/Thesis/apollo_imgs/apollo_11/test/"
# folder_dir = "/Users/hiranadeem/Documents/Thesis/apollo_imgs/apollo_14/A/"
folder_dir = "/Users/hiranadeem/Documents/Thesis/apollo_imgs/test/"

img_num = 0 # count number of images 
count = 0
for file in os.listdir(folder_dir):
    if (file.endswith(".tif")): # ensure only looping through .tif images
        x=0 #reset horizontal direction pan

        # image file path
        image = folder_dir + file
        # print(image)
    
        # read file
        img = cv2.imread(image)
        #cv2.imshow("orig_image", img)
        #cv2.waitKey(0)
        
        #print(img.shape) # output dimensions of image
        img_width = img.shape[1]
        # img_shift = img_width/SCALE
        # print(img_shift)

        # STUFF
        img_num+=1
        print(str(img_num) + "-" + file)

        # for each image, crop to 512 by 512, shift x coordinate, crop again
        for j in range(0,NUM_CROP_Y):
            for i in range(0,NUM_CROP_X):
                crop_img = img[y:y+h, x:x+w]
                
                filename = MISSION + PAIR + str(file_num) + ".JPG" 
                
                cv2.imwrite(crop_dir + filename, crop_img)
                # print("crop ", crop_img.shape)
                file_num+=1

                count+=1
                
                # if the final coordinate is less than 512 pixels to the end of the image, adjust
                # goal is to have 512x512 for all images
                if (img_width - (x+SCALE))>SCALE: 
                    x=x+SCALE
                else:
                    x=x+(img_width - (x+SCALE))
                i+=1
            x=0
            y=y+SCALE
        print("Images generated from " + file + ": " + str(count))  
        print(" ")  
    y = 0
