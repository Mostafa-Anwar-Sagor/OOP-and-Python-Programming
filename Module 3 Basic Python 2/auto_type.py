import pyautogui
from time import sleep
sleep(5)
for i in range(0,3):
 pyautogui.write('Hello world!', interval=0.25)
 pyautogui.press('Enter')




