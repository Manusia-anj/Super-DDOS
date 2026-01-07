import pyautogui
import random
import time

pyautogui.FAILSAFE = True

while True:
    x = random.randint(0, pyautogui.size().width)
    y = random.randint(0, pyautogui.size().height)
    
    pyautogui.moveTo(x, y, duration=0.1)
    
    if random.random() < 0.1:
        pyautogui.click()
        
    if random.random() < 0.05:
        pyautogui.typewrite(random.choice("abcdefghijklmnopqrstuvwxyz"))
        
    time.sleep(0.01)
