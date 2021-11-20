import numpy as np
from PIL import Image
from PIL import ImageGrab
import win32gui, win32con
import time


handle = win32gui.FindWindow(0, 'Flappy Bird')
bbox = win32gui.GetWindowRect(handle)
text = win32gui.SetForegroundWindow(handle)
win32gui.SendMessage(handle, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)

time.sleep(3)

for i in range(10):
    img = ImageGrab.grab(bbox=bbox)
    img.save('./test_{}.png'.format(i))
