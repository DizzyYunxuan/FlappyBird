import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
from scipy import ndimage

img = r"D:\anaconda\flappy_ai\FlapPyBird\datasets\1636268284.jpg"
img = cv2.imread(img)
img = np.mean(img, axis=2)
img = img[30:436, :]

# gradient
# img_pad = np.pad(img, pad_width=((0, 0), (1, 0)), mode='edge')
# img_g_h = img_pad[:,:-1] - img
# img_g_h[img_g_h<0] = 0
# img_g_h[img_g_h>0] = 1

# img_pad = np.pad(img, pad_width=((1, 0), (0, 0)), mode='edge')
# img_g_v = img_pad[:-1,:] - img
# img_g_v[img_g_v<0] = 0
# img_g_v[img_g_v>0] = 1

# img_edge = img_g_h + img_g_v
# print()

# wavelet
# print()
# k = np.array([1, 1,-1, -1])
# img_blur_v = cv2.filter2D(src=img, ddepth=-1, kernel=k)
# img_blur_h = cv2.filter2D(src=img.T, ddepth=-1, kernel=k).T
# print()
# edges = img - img_blur


# lap egdes
# k = np.array([[-1, -1, -1],
#                 [-1, 8, -1],
#                 [-1, -1, -1]])
k = np.array([[0, -1, 0],
                [-1, 4, -1],
                [0, -1, 0]])
img_edge = cv2.filter2D(img, -1, k)
img_edge[img_edge<20] = 0
img_edge[img_edge>=20] = 255

nb_obj, img_label = cv2.connectedComponents(np.uint8(img_edge), connectivity=4)

print()

# OSTU
# hist = np.histogram(img, bins=255)
# print(hist)

# print(edges.min(), edges.max())





