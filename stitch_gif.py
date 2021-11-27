import os
import cv2
import numpy as np
import imageio


imgs_path = r'D:\anaconda\flappy_ai\FlapPyBird\datasets\test_png_4'
decision_map_path = r'D:\anaconda\flappy_ai\FlapPyBird\datasets\test_png_4_results'
target_gif_path = r'D:\anaconda\flappy_ai\FlapPyBird\datasets\gifs\res_cat_4.gif'

img_list = sorted(os.listdir(imgs_path), key=lambda x:int(x.split('_')[1][:-4]))
decision_map_list = sorted(os.listdir(decision_map_path), key=lambda x:int(x.split('_')[1][:-4]))

frames = []
for i in range(len(img_list)):
    img_path = os.path.join(imgs_path, img_list[i])
    decision_map = os.path.join(decision_map_path, decision_map_list[i])
    img = cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2RGB) 
    
    decision_map = cv2.cvtColor(cv2.imread(decision_map, cv2.COLOR_GRAY2BGR), cv2.COLOR_BGR2RGB) 
    decision_map = np.pad(decision_map, ((34, 117), (8, 8), (0, 0)), mode='constant')
    res = np.concatenate([img, decision_map], axis=1)
    frames.append(res)

imageio.mimsave(target_gif_path, frames)

