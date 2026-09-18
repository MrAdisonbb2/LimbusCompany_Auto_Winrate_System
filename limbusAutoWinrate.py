import pyautogui
import pygetwindow as gw
import keyboard
import time

count = 0

while not keyboard.is_pressed("ctrl+d"):
    window = gw.getWindowsWithTitle("LimbusCompany")[0]

    window.activate()
    time.sleep(0.5)
    
    pyautogui.press("p")
    pyautogui.press("enter")
    print(f"round : {count}")
    pyautogui.hotkey("alt", "tab")
    
    time.sleep(60)