'''
This code is used to crop rectangular images that are height 500 to squaers of 
500x500.

Source:
https://www.geeksforgeeks.org/how-to-iterate-through-images-in-a-folder-python/
'''

import cv2
import os
from os import listdir

# variables for crop dimension
y = 0
x = 0
h = 512
w = 512
file_num = 1

# cropped image directory
crop_dir = "/Users/hiranadeem/Documents/Thesis/apollo_imgs/apollo_11/B/crop_b/"

# iterate through all images in order in the data folder and crop them. Output the cropped image
folder_dir = "/Users/hiranadeem/Documents/Thesis/apollo_imgs/apollo_11/B/"
for file in os.listdir(folder_dir):
    if (file.endswith(".tif")): # ensure only looping through .tif images
        x=0 #reset horizontal direction pan

        # image file path
        image = folder_dir + file
        print(image)
    
        # read file
        img = cv2.imread(image)
        #cv2.imshow("orig_image", img)
        #cv2.waitKey(0)
        
        print(img.shape) # output dimensions of image
        img_width = img.shape[1]
        img_shift = img_width/512.0
        print(img_shift)

        # for each image, crop to 512 by 512, shift x coordinate, crop again
        for j in range(0,4):
            for i in range(0,round(img_shift)):
                crop_img = img[y:y+h, x:x+w]
                
                filename = "moon-" + str(file_num) + ".JPG"
                cv2.imwrite(crop_dir + filename, crop_img)
                print("crop ", crop_img.shape)
                file_num+=1

                # if the final coordinate is less than 512 pixels to the end of the image, adjust
                # goal is to have 512x512 for all images
                if (img_width - (x+512))>512: 
                    x=x+512
                else:
                    x=x+(img_width - (x+512))
                i+=1
            x=0
            y=y+512
    y = 0
    
    
    # #### CROP IMAGE 1 ####
    # crop_img = img[y:y+h, x:x+w]
    # # cv2.imshow("cropped", crop_img)
    # #cv2.waitKey(0)

    # # update filename
    # filename = str(file_num) + ".jpeg"
    # # print("file", filename)
    # file_num+=1

    # # write cropped image to file and save in cropped image directory
    # cv2.imwrite(crop_dir + filename, crop_img)

    # #### CROP IMAGE 2 ####
    # x = x+400
    # crop_img = img[y:y+h, x:x+w]
    # # cv2.imshow("cropped", crop_img)
    # #cv2.waitKey(0)

    # # update filename
    # filename = str(file_num) + ".jpeg"
    # # print("file", filename)
    # file_num+=1

    # # write cropped image to file and save in cropped image directory
    # cv2.imwrite(crop_dir + filename, crop_img)

    # #### CROP IMAGE 3 ####
    # x = x+400
    # crop_img = img[y:y+h, x:x+w]
    # # cv2.imshow("cropped", crop_img)
    # #cv2.waitKey(0)

    # # update filename
    # filename = str(file_num) + ".jpeg"
    # # print("file", filename)
    # file_num+=1

    # # write cropped image to file and save in cropped image directory
    # cv2.imwrite(crop_dir + filename, crop_img)