from PIL import ImageGrab
import win32gui, win32con
import time
import os


handle = win32gui.FindWindow(0, 'Flappy Bird')
bbox = win32gui.GetWindowRect(handle)
text = win32gui.SetForegroundWindow(handle)
win32gui.SendMessage(handle, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)

time.sleep(0)

test_img = []

for i in range(180):
    img = ImageGrab.grab(bbox=bbox)
    time.sleep(1/180)
    test_img.append(img)


save_path = r'./datasets\test_png_5'
if not os.path.exists(save_path):
    os.mkdir(save_path)

for i in range(len(test_img)):
    img = test_img[i]
    img.save(os.path.join(save_path, 'frames_{}.png'.format(i)))
