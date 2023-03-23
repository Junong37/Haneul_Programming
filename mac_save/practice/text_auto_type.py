import pyautogui
import time

time.sleep(3)

text = """test"""

pyautogui.write(text, interval=0.005)