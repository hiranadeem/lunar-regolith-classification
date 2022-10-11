import cv2
import os
from os import listdir


folder_dir = "/Users/hiranadeem/Documents/Research/Simulant Images/data/images/"
for file in os.listdir(folder_dir):

    # update filename
    filename = str(file_num) + ".jpeg"
    # print("file", filename)
    file_num+=1    

    os.rename(file,)



# f = open('/Users/hiranadeem/Documents/Research/Simulant Images/data/images.csv', 'w')
# writer= csv.writer(f)
# writer.writerow(images_num)