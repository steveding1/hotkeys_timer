# This is for delaying press two hotkeys:Ctrl+F8 and then Ctrl+F9
# The hotkeys can be used for OBS screen recording start and stop.
import time
import win32api
import win32con
import sys

argvs = sys.argv
print("I will press the first hotkeys at",
      time.strftime("%H:%M:%S", time.localtime(time.time() + int(argvs[1]))),
      '. And press the second hotkeys at',
      time.strftime("%H:%M:%S", time.localtime(time.time() + int(argvs[1]) + int(argvs[2]))))

def hotkey(keys: list):
    # press keys.
    for key in keys:
        win32api.keybd_event(key, 0, 0, 0)
    time.sleep(0.2)
    # release keys in reversed orders.
    for key in keys[::-1]:
        win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)

time.sleep(int(argvs[1]))
print('started at:', time.strftime("%H:%M:%S", time.localtime()))
hotkey([17, 119])  # Crl+F8
time.sleep(int(argvs[2]))
hotkey([17, 120])  # Crl+F9
print('stopped at:', time.strftime("%H:%M:%S", time.localtime()))
