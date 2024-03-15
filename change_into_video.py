

import cv2
import os
import re


def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

folder_path = 'processed_source'

output_video_path = 'processed_source/single.avi'


files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
files.sort(key=natural_sort_key)  # Sorted in natural sorting order

# Read the first image to get the resolution of the video
frame = cv2.imread(os.path.join(folder_path, files[0]))
height, width, layers = frame.shape


fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # 'DIVX'AVI
video = cv2.VideoWriter(output_video_path, fourcc, 20.0, (width, height))

for file in files:
    img = cv2.imread(os.path.join(folder_path, file))
    video.write(img)
video.release()
