# This is for delaying press two hotkeys:Ctrl+F8 and then Ctrl+F9
# The hotkeys can be used for OBS screen recording start and stop.
import time
import win32api
import win32con
import sys
import pandas as pd

keymap = pd.read_csv('keymaps.csv')


def InputKeys():
    input_keys = []
    hotkeys1 = []
    key = ''
    print("input your hotkeys (one by one with order)")
    for i in range(int(input("How many keys you will input for the hotkey combination?"))):
        print("Input the ", i + 1, " key")
        key = input()
        while key not in keymap.Key.values:
            print("I don't understand your input. it must be 1-9, A-Z, Alt, Ctrl, F1-F12 etc.")
            print("Please input the ", i + 1, " key again")
            key = input()
        input_keys.append(key)
        hotkeys1.append(keymap[keymap['Key'] == key]['Key Value'].values[0])
    print("The hotkeys are", input_keys, hotkeys1)
    return hotkeys1

hotkeys1 = InputKeys()
hotkeys2 = InputKeys()

argvs = sys.argv

print("I will press the first hotkeys at",
      time.strftime("%H:%M:%S", time.localtime(time.time() + int(argvs[1]))),
      '. And press the second hotkeys at',
      time.strftime("%H:%M:%S", time.localtime(time.time() + int(argvs[1]) + int(argvs[2]))))
time.sleep(int(argvs[1]))
print('started at:', time.strftime("%H:%M:%S", time.localtime()))

def hotkey(keys: list):
    # press keys.
    for key in keys:
        win32api.keybd_event(key, 0, 0, 0)
    time.sleep(0.2)
    # release keys in reversed orders.
    for key in keys[::-1]:
        win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)

hotkey(hotkeys1)
time.sleep(int(argvs[2]))
hotkey(hotkeys2)
print('stopped at:', time.strftime("%H:%M:%S", time.localtime()))
