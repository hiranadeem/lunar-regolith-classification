'''This program augments images from the ALSCC dataset '''
import cv2 as cv
import os
import pandas as pd

import imgaug.augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage

seq = iaa.Sequential([
    iaa.Fliplr(0.5),
    iaa.Flipud(0.2),
    iaa.Crop(percent=(0, 0.3)),

    iaa.Sometimes(
        0.5,
        iaa.GaussianBlur(sigma=(0, 0.05))
    ),

    iaa.LinearContrast((0.95, 1.05)),

    iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5),

    iaa.Multiply((0.95, 1.05), per_channel=0.25),

    iaa.Affine(
        # scale={"x": (1, 1.5), "y": (1, 1.5)},
        # translate_percent={"x": (-0.05, 0.05), "y": (-0.05, 0.05)},
        rotate=(-3,3),
    )],
    random_order=True)

def aug_image(filename: str, df: pd.DataFrame, folder: str, augmentations: int) -> (list, list):
    # load image
    img = cv.imread(os.path.join(folder, filename))

    bbs = list()

    for _, row in df[df.filename == filename].iterrows():
        x1 = row.xmin
        y1 = row.ymin
        x2 = row.xmax
        y2 = row.ymax
        bbs.append(BoundingBox(x1=x1, y1=y1, x2=x2, y2=y2, label=row['class']))

    bbs = BoundingBoxesOnImage(bbs, shape=img.shape[:-1])

    images = [img for _ in range(augmentations)]

    bbss = [bbs for _ in range(augmentations)]

    image_aug, bbs_aug = seq(images=images, bounding_boxes=bbss)

    return image_aug, bbs_aug

def save_augmentations(images: list, bbs: list, df: pd.DataFrame, filename: str, folder: str) -> pd.DataFrame: 
    
    for [i, img_a], bb_a in zip(enumerate(images), bbs):

        aug_img_name = f'{filename}_{i}.jpg'

        bb_a = bb_a.remove_out_of_image().clip_out_of_image()

        at_least_one_box = False
        for bbs in bb_a:
            arr = bbs.compute_out_of_image_fraction(img_a)
            if arr < 0.8:
                at_least_one_box = True
                x1 = bbs.x1
                y1 = bbs.y1
                x2 = bbs.x2
                y2 = bbs.y2
                c = bbs.label

                height, width = img_a.shape[:-1]
                df = df.append(pd.DataFrame(data=[aug_img_name, width, height, c, x1, y1, x2, y2], index=df.columns.tolist()).T)

        if at_least_one_box:
            cv.imwrite(os.path.join(folder, aug_img_name), img_a)
        
    return df

if __name__ == '__main__':

    folder = 'valid'

    augmentations = 10

    input_folder = os.path.join('..', 'preprocess\\test_images\\', folder)
   
    output_folder = os.path.join('..', 'preprocess\\test_images\\', f'{folder}_aug')
    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)

    print(os.listdir(input_folder))

    img_list = [img for img in os.listdir(input_folder) if img.endswith('.JPG')]
    print(img_list)

    df = pd.read_csv(os.path.join('..', 'preprocess\\', 'labels.csv'))
    # print(df.head())
    
    aug_df = pd.DataFrame(columns=df.columns.tolist())


    for filename in img_list:

        print("Augmenting images")

        aug_images, aug_bbs = aug_image(filename, df, input_folder, augmentations)
        
        print("Saving images")


        aug_df = save_augmentations(aug_images,aug_bbs, aug_df, filename, output_folder)

        print("Adding to df")
        
        aug_df.to_csv(os.path.join('..', 'preprocess\\annotations_imgaug\\', f'{folder}_aug.csv'))
        print("aug_df = ", aug_df.head())