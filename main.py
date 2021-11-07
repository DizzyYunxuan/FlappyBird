from time import sleep
import numpy as np
from PIL import Image
from PIL import ImageGrab
import win32gui, win32con
import keyboard as kb

def cmd_exec():
    for i in range(5):
        kb.press_and_release('space')
        sleep(0.8)


def get_img():
    img = ImageGrab.grab(bbox=bbox)
    return img


if __name__ == '__main__':
    window_str = 'Flappy Bird'
    handle = win32gui.FindWindow(0, window_str)
    bbox = win32gui.GetWindowRect(handle)
    text = win32gui.SetForegroundWindow(handle)
    win32gui.SendMessage(handle, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
    img = get_img()
    cmd_exec()
