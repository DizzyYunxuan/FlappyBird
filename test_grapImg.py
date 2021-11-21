import numpy as np
from PIL import Image
from PIL import ImageGrab
import win32gui, win32con
import time


handle = win32gui.FindWindow(0, 'Flappy Bird')
bbox = win32gui.GetWindowRect(handle)
text = win32gui.SetForegroundWindow(handle)
win32gui.SendMessage(handle, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)

time.sleep(1)

test_img = []

for i in range(20):
    img = ImageGrab.grab(bbox=bbox)
    time.sleep(0.1)
    test_img.append(img)




for i in range(len(test_img)):
    img = test_img[i]
    img.save(r'./datasets\test_png_2\test_{}.png'.format(i))
