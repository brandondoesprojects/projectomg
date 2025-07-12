import subprocess
import time
import pyautogui

# Open Notepad
subprocess.Popen('notepad.exe')

# Wait for Notepad to open
time.sleep(1)

# Type "hi"
pyautogui.write('hi', interval=0.1)
