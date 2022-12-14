'''
This code is used to run the inference from the trained model
'''
import time
import os
import tensorflow as tf
from os import listdir
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as viz_utils

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'    # Suppress TensorFlow logging (1)
import pathlib
import tensorflow as tf

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')   # Suppress Matplotlib warnings

import csv

PATH_TO_MODEL_DIR = "C:/Users/hnadeem5/Documents/VSCode/auto-particle-classification/tensorflow/workspace2/training/exported-models/my_faster_rcnn_2"
PATH_TO_SAVED_MODEL = PATH_TO_MODEL_DIR + "/saved_model"
PATH_TO_LABELS = "C:/Users/hnadeem5/Documents/VSCode/auto-particle-classification/tensorflow/workspace2/training/annotations/label_map.pbtxt" # update this line
IMAGE_PATHS= ["C:/Users/hnadeem5/Documents/VSCode/auto-particle-classification/tensorflow/workspace2/inference/imgs/apollo11_A_48_3.JPG"] # update this line

def load_image_into_numpy_array(path):
    """Load an image from file into a numpy array.

    Puts image into numpy array to feed into tensorflow graph.
    Note that by convention we put it into a numpy array with shape
    (height, width, channels), where channels=3 for RGB.

    Args:
      path: the file path to the image

    Returns:
      uint8 numpy array with shape (img_height, img_width, 3)
    """
    return np.array(Image.open(path))

print('Loading model...', end='')
start_time = time.time()

# Load saved model and build the detection function
model = tf.saved_model.load(PATH_TO_SAVED_MODEL)
detect_fn = model.signatures['serving_default']

end_time = time.time()
elapsed_time = end_time - start_time
print('Done! Took {} seconds'.format(elapsed_time))

category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)


for image_path in IMAGE_PATHS:

  print('Running inference for {}... '.format(image_path), end='')

  image_np = load_image_into_numpy_array(image_path)

  # Things to try:
  # Flip horizontally
  # image_np = np.fliplr(image_np).copy()

  # Convert image to grayscale
  # image_np = np.tile(
  #     np.mean(image_np, 2, keepdims=True), (1, 1, 3)).astype(np.uint8)

  # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
  input_tensor = tf.convert_to_tensor(image_np)
  # The model expects a batch of images, so add an axis with `tf.newaxis`.
  input_tensor = input_tensor[tf.newaxis, ...]

  detections = detect_fn(input_tensor)

  # All outputs are batches tensors.
  # Convert to numpy arrays, and take index [0] to remove the batch dimension.
  # We're only interested in the first num_detections.
  num_detections = int(detections.pop('num_detections'))
  detections = {key: value[0, :num_detections].numpy()
                for key, value in detections.items()}
  detections['num_detections'] = num_detections

  # detection_classes should be ints.
  detections['detection_classes'] = detections['detection_classes'].astype(np.int64)

  image_np_with_detections = image_np.copy()

  viz_utils.visualize_boxes_and_labels_on_image_array(
        image_np_with_detections,
        detections['detection_boxes'],
        detections['detection_classes'],
        detections['detection_scores'],
        category_index,
        use_normalized_coordinates=True,
        max_boxes_to_draw=100,
        min_score_thresh=.30,
        agnostic_mode=False)
  plt.figure()
  plt.imshow(image_np_with_detections)
  print('image displayed')

      # # output bounding box coords
      # # print(detections['detection_boxes'])
      # dict = detections['detection_boxes']
      # x=0
      # for i in dict:
      #   # writer.writerow(dict[i])  
      #   writer.writerow(dict[x])
      #   x+=1
      # print("Number of objects: ", x)

plt.show()
print("image plotted")
plt.savefig('pred3.png') # update this line
print("image saved")

# sphinx_gallery_thumbnail_number = 2
