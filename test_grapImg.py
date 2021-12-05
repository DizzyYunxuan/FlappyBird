from PIL import ImageGrab
import win32gui, win32con
import time
import os
import keyboard as kb

handle = win32gui.FindWindow(0, 'Flappy Bird')
bbox = win32gui.GetWindowRect(handle)
text = win32gui.SetForegroundWindow(handle)
win32gui.SendMessage(handle, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)

time.sleep(0)

test_img = []
s = time.time()
for i in range(50):
    
    img = ImageGrab.grab(bbox=bbox)
    kb.press_and_release('space')
    time.sleep(0.3)
    e = time.time()
    print(e - s)
    test_img.append(img)


save_path = r'./datasets\test_png_8'
if not os.path.exists(save_path):
    os.mkdir(save_path)

for i in range(len(test_img)):
    img = test_img[i]
    img.save(os.path.join(save_path, 'frames_{}.png'.format(i)))
