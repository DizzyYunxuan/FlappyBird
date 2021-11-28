import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image
from scipy import ndimage
import time
import os
from edge_detect_template_single_test import get_decisionMap



# def get_decisionMap(img_gray):
#     img = img_gray[34:434, 8:-8]
#     [h, w] = img.shape


#     # lap kernel
#     k = np.array([[-1, -1, -1],
#                     [-1, 8, -1],
#                     [-1, -1, -1]])

#     # remove holes in ob
#     s_k = np.ones([3, 3]) / 9
#     img_edge = cv2.filter2D(cv2.filter2D(img, -1, k), -1, s_k)
#     img_seg = img_edge != 0.0
#     img_seg = img_seg.astype(np.float64)
#     ls_k = np.ones([7, 7]) / 49
#     img_seg = cv2.copyMakeBorder(img_seg, 3, 3, 3, 3, borderType=cv2.BORDER_CONSTANT, value=1)
#     img_seg = cv2.filter2D(img_seg, -1, ls_k, borderType=cv2.BORDER_REFLECT)[3:-3, 3:-3]
#     img_seg = img_seg > 0
#     img_seg = img_seg.astype(np.float64)

#     # remove holes in bg
#     img_seg = cv2.filter2D(img_seg, -1, ls_k, borderType=cv2.BORDER_REFLECT)
#     img_seg = img_seg > 0.9
#     img_seg = img_seg.astype(np.float64)
#     ll_sk = np.ones([9, 9]) / 81
#     img_seg = cv2.filter2D(img_seg, -1, ll_sk, borderType=cv2.BORDER_REFLECT)
#     img_seg = img_seg > 0.999
#     img_seg = img_seg.astype(np.float64)

#     # shrink for edges
#     img_seg = cv2.filter2D(img_seg, -1, s_k)
#     img_seg = img_seg > 0.0
#     img_seg = img_seg.astype(np.float64)


#     decision_map = np.zeros_like(img_edge)

#     # get horizontal obs
#     h_strip = img_seg[16, :]
#     h_sePoints = h_strip[1:] - h_strip[:-1]
#     h_start_Points = np.argwhere(h_sePoints > 0).flatten()
#     h_end_Points = np.argwhere(h_sePoints < 0).flatten()




#     if h_end_Points.shape[0] < 1 and h_start_Points.shape[0] < 1:
#         num_ob = 0
#     elif h_start_Points.shape[0] < 1:
#         num_ob = 0
#     else:
#         num_ob = 1
#         h_end_Points = np.append(h_end_Points, w)

#     # get vertical space
#     # num_ob = h_start_Points.shape[0]
#     h_ob_lr_dict = {}
#     for i in range(num_ob):
#         h_ob_lr_dict[i] = [h_start_Points[i], h_end_Points[i]]
#         left, right = h_ob_lr_dict[i]
#         decision_map[:, left:right] = 1
#         v_strip = img_seg[:, np.int32((left + right) / 2)]
#         v_sePoints = v_strip[1:] - v_strip[:-1]
#         v_bot_Points = np.argwhere(v_sePoints < 0)
#         v_upper_Points = np.argwhere(v_sePoints > 0)
#         sps_upper = np.min(v_bot_Points)
#         sps_bot = np.max(v_upper_Points)
#         decision_map[sps_upper:sps_bot, left:right] = 0



#     bird_map = img_seg - decision_map
#     bird_map = (bird_map > 0).astype(np.float32)
#     bird_strip = bird_map[:, 50:100]
#     b_k = np.ones([10, 10])
#     bird_strip = cv2.filter2D(bird_strip, -1, b_k)
#     bird_loc = np.argwhere(bird_strip > 99)



#     # upper, bot, left, right
#     x_bird = bird_loc[0, 0]
#     bird_bounding_box = np.array([x_bird - 5, x_bird + 25, 50, 85])
#     decision_map[bird_bounding_box[0]:bird_bounding_box[1], bird_bounding_box[2]:bird_bounding_box[3]] = 1

#     return decision_map



if __name__ == '__main__':
    test_sequence_path = r'D:\anaconda\flappy_ai\FlapPyBird\datasets\test_png_5'
    res_path = r'D:\anaconda\flappy_ai\FlapPyBird\datasets\test_png_5_results'

    if not os.path.exists(res_path):
        os.mkdir(res_path)

    for i in os.listdir(test_sequence_path):
        img_path = os.path.join(test_sequence_path, i)
        img_gray = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        decision_map = get_decisionMap(img_gray)
        decision_map_uint8 = np.uint8(decision_map * 255)
        cv2.imwrite(os.path.join(res_path, i), decision_map_uint8)
        print("current frames: {}".format(i))


        # plt.figure()
        # plt.imshow(decision_map, 'gray')
        # plt.figure()
        # plt.imshow(img_gray, 'gray')

    # print()






