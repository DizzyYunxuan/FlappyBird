import time
import numpy as np
from PIL import ImageGrab
import win32gui, win32con
import keyboard as kb
from edge_detect_template_single_test import get_decisionMap
import matplotlib.pyplot as plt
import cv2
import os

from send_cmd import send_cmd


def cmd_exec():
    for i in range(5):
        kb.press_and_release('space')
        time.sleep(0.8)


def get_img(bbox):
    img = np.array(ImageGrab.grab(bbox=bbox))
    return img


def init_window_monitor():
    handle = win32gui.FindWindow(0, 'Flappy Bird')
    bbox = win32gui.GetWindowRect(handle)
    text = win32gui.SetForegroundWindow(handle)
    win32gui.SendMessage(handle, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
    return bbox, text



def send_cmd(bird_x, bird_y, h_ob_dict, v_sps_dict, status):
    # cmd_dict: 
    #     0 : keep height
    #     1 : raise
    #     2 : dive 
    #     3 : rapid raise

    # status_dict = {
    #         0: 'up',
    #         1: 'down',
    #         2: 'keep'
    #     }

    if status == 0:
        bird_x -= 3
    elif status == 1:
        bird_x += 3


    left, right = -1, -1
    for key in h_ob_dict:
        left, right = h_ob_dict[key]
        upper, bot = v_sps_dict[key]
        if bird_y < right:
            break

    if left < 0 or right < 0:
        print('Keep')
        if status >= 0:
            sleep_time = 0.5
            kb.press_and_release('space')
            time.sleep(sleep_time)
        cmd = 0
        
    else:
        if bird_x > (upper + bot) / 2 + 18:
            print('raise')
            cmd, sleep_time = 0, 0.25
            kb.press_and_release('space')
            time.sleep(sleep_time)
            
        elif bird_x < (upper + bot) / 2 + 18:
            print('Dive')
            cmd, sleep_time = 2, 0.0
        else:
            print('Keep')
            if status >= 0:
                sleep_time = 0.5
                kb.press_and_release('space')
                time.sleep(sleep_time)
            cmd = 0

        return cmd
if __name__ == '__main__':
    save_frames_path = r'D:\anaconda\flappy_ai\FlapPyBird\datasets\test_png_7'
    save_dm_path = r'D:\anaconda\flappy_ai\FlapPyBird\datasets\test_png_7_decision'
    cmd_txt = r'D:\anaconda\flappy_ai\FlapPyBird\datasets\test_png_7_decision\cmd.txt'

    if not os.path.exists(save_frames_path):
        os.mkdir(save_frames_path)

    if not os.path.exists(save_dm_path):
        os.mkdir(save_dm_path)

    bbox, text = init_window_monitor()

    # Start
    kb.press_and_release('space')

    f = open(cmd_txt, 'w')
    i = 0
    # for i in range(20):
    pre_bird_x = 200

    


    while i< 150:
        img = get_img(bbox)
        current_decision_map, bird_x, bird_y, h_ob_dict, v_sps_dict = get_decisionMap(img)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_save = img[34:434, 8:-8]
        current_decision_map = np.uint8(current_decision_map * 255)
        status = bird_x - pre_bird_x
        cmd = send_cmd(bird_x, bird_y, h_ob_dict, v_sps_dict, status)
        pre_bird_x = bird_x

        i += 1
        cv2.imwrite(os.path.join(save_frames_path, 'frames_{}.png'.format(i)), img_save)
        cv2.imwrite(os.path.join(save_dm_path, 'decisionMap_{}.png'.format(i)), current_decision_map)
        f.write("frame {}, cmd: {}\n".format(i, cmd))
        # time.sleep(0.3)

    
    f.close()
        
        # frames.append(img) 
        # decision_maps.append(decision_maps)
    
    
    
    # cmd_exec()
