import cv2
import numpy as np
import pyautogui
import time

def find_and_click_image(image_path, region,flag):
    target_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    while True:
        # Capture the screen region
        screenshot = pyautogui.screenshot(region=region)
        screen_gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
        
        # Perform template matching
        result = cv2.matchTemplate(screen_gray, target_image, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        
        if max_val > 0.8:  # Adjust threshold as needed
            return 1
        else:
            print("Image not found, continuing search...")
            time.sleep(1)
        if flag:
            break

def Move_Click(x,y):
    pyautogui.moveTo(x,y)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.3)
# Example usage
time.sleep(2)
while True:

    Move_Click(2065,1267)

    if find_and_click_image('2.png',(667, 454,1500,600),1):
        Move_Click(1277, 1109)
        pyautogui.click()
        time.sleep(0.2)
        if find_and_click_image('2.png',(667,454,1500,600,1)):
            print("Shortage of money!")
            exit()

    Move_Click(2065,1267)
    pyautogui.click()

    if find_and_click_image('1.png',(1028, 589, 600, 500),0):
        pyautogui.click()

    Move_Click(1266, 1363)
    

