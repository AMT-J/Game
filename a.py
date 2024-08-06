import pyautogui
import time

def print_mouse_position():
    try:
        while True:
            # 获取当前鼠标位置
            x, y = pyautogui.position()
            # 打印鼠标位置
            print(f"Mouse Position: ({x}, {y})")
            # 每秒更新一次
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped.")

# 运行函数
print_mouse_position()
