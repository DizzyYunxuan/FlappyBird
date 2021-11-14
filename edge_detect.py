import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
from scipy import ndimage

img = r"D:\anaconda\flappy_ai\FlapPyBird\datasets\1636268284.jpg"
img = cv2.imread(img)
img = np.mean(img, axis=2) / 255.
img = img[34:434, 4:-4]
[h, w] = img.shape


# lap egdes
k = np.array([[-1, -1, -1],
                [-1, 8, -1],
                [-1, -1, -1]])

s_k = np.ones([3, 3]) / 9
img_edge = cv2.filter2D(cv2.filter2D(img, -1, k), -1, s_k)
img_seg = img_edge != 0.0
img_seg = img_seg.astype(np.float64)


decision_map = np.zeros_like(img_edge)


h_strip = img_seg[16, :]
h_strip_shuffle  = np.pad(h_strip, pad_width=((0, 1)), mode='constant')
h_sePoints = h_strip_shuffle[1:] - h_strip
h_sePoints = np.argwhere(h_sePoints != 0).flatten()
h_start_points = h_sePoints[::2]
h_start_points -= 2
h_end_points = h_sePoints[1::2]
h_end_points += 2
if len(h_end_points) - len(h_start_points) == 1:
    end_points = h_end_points + [len(h_strip) - 1]
h_ob_lr_tuple = np.array(list(zip(h_start_points, h_end_points)))

v_strip = img_seg[:, np.int((h_ob_lr_tuple[:, 0] + h_ob_lr_tuple[:, 1]) / 2)]
v_strip_shuffle = np.pad(v_strip, pad_width=((1, 0)), mode='constant')
v_sePoints = v_strip_shuffle[:-1] - v_strip
v_sepoints = np.argwhere(v_sePoints != 0)

print()





