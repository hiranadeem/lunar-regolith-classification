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
h = 500
w = 500
file_num = 1

# cropped image directory
crop_dir = "/Users/hiranadeem/Documents/Research/Simulant Images/data/crop_square/"

# iterate through all images in order in the data folder and crop them. Output the cropped image
folder_dir = "/Users/hiranadeem/Documents/Research/Simulant Images/data/cropped/"
for file in os.listdir(folder_dir):
    if (file.endswith(".JPG")): # ensure only looping through JPG images
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
        img_shift = img_width/500.0
        print(img_shift)

        # for each image, crop to 500 by 500, shift x coordinate, crop again
        for i in range(0,round(img_shift)):
            crop_img = img[y:y+h, x:x+w]
            
            filename = "ob1-" + str(file_num) + ".JPG"
            cv2.imwrite(crop_dir + filename, crop_img)
            print("crop ", crop_img.shape)
            file_num+=1

            # if the final coordinate is less than 500 pixels to the end of the image, adjust
            # goal is to have 500x500 for all images
            if (img_width - (x+500))>500: 
                x=x+500
            else:
                x=x+(img_width - (x+500))
            i+=1
    
    
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