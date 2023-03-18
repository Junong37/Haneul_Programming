import pyautogui
import time

time.sleep(3)

text = """Hello World"""

pyautogui.write(text, interval=0.1)