import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
from scipy import ndimage

img = r"D:\anaconda\flappy_ai\FlapPyBird\datasets\start_night.jpg"
img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
# img = np.mean(img, axis=2) / 255.
img = img[34:434, 8:-8]
[h, w] = img.shape


# lap egdes
k = np.array([[-1, -1, -1],
                [-1, 8, -1],
                [-1, -1, -1]])
# k = np.array([[0, -1, 0],
#                 [-1, 4, -1],
#                 [0, -1, 0]])


s_k = np.ones([3, 3]) / 9
img_edge = cv2.filter2D(cv2.filter2D(img, -1, k), -1, s_k)
img_seg = img_edge != 0.0
img_seg = img_seg.astype(np.float64)
ls_k = np.ones([7, 7]) / 49
img_seg = cv2.filter2D(img_seg, -1, ls_k)
img_seg = img_seg > 0
img_seg = img_seg.astype(np.float64)

decision_map = np.zeros_like(img_edge)


h_strip = img_seg[16, :]
# h_strip_shuffle  = np.pad(h_strip, pad_width=((0, 1)), mode='constant')
h_sePoints = h_strip[1:] - h_strip[:-1]
h_start_Points = np.argwhere(h_sePoints > 0).flatten() + 3
h_end_Points = np.argwhere(h_sePoints < 0).flatten() - 3

if h_end_Points[0] < h_start_Points[0]:
    h_end_Points = h_end_Points[1:]
h_ob_lr_tuple = np.array(list(zip(h_start_Points, h_end_Points)))

num_ob = h_ob_lr_tuple.shape[0]

for i in range(num_ob):
    s, e = h_ob_lr_tuple[i, :]
    decision_map[:, s:e] = 1



v_strip = img_seg[:, np.int32((h_ob_lr_tuple[:, 0] + h_ob_lr_tuple[:, 1]) / 2)]
# v_strip_shuffle = np.pad(v_strip, pad_width=((1, 0)), mode='constant')
v_sePoints = v_strip[1:, :] - v_strip[:-1, :]
v_upper_Points = np.argwhere(v_sePoints < 0)
v_upper_Points[:, 0] -= 3
v_bot_Points = np.argwhere(v_sePoints > 0)
v_bot_Points[:, 0] += 3

v_sps_tb_tuple  = np.zeros([num_ob, 2], dtype=np.int32)

for i in range(num_ob):
    up_idx = np.argwhere(v_upper_Points == i)[:, 0]
    ob_v_upper_group = v_upper_Points[up_idx, 0]
    ob_v_bot_group = v_bot_Points[up_idx, 0]
    current_space = np.array([ob_v_upper_group.min(), ob_v_bot_group.max()])
    v_sps_tb_tuple[i, :] = np.int32(current_space)

for i in range(num_ob):
    l, r = h_ob_lr_tuple[i, :]
    t, b = v_sps_tb_tuple[i, :]
    decision_map[t:b, l:r] = 0



print()






