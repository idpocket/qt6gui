import time

import pyautogui

kg = True


def one():
    while kg:

        x, y = pyautogui.position()
        print(f'x:{x} y:{y}')


def t():
    pyautogui.click(x=x, y=y)
    kg = True

    i = 1
    while kg:

        pyautogui.click(x=x, y=y)

        time.sleep(0.5)
        pyautogui.click(x=x2, y=y2)
        time.sleep(0.5)
        i = i + 1
        print(f'点击了{i}次')
        if i == 9000:
            kg = False
        x3, y3 = pyautogui.position()
        if x3 not in [x, x2]:
            kg = False


if __name__ == '__main__':
    # one()
    x, y = 738, 732
    x2, y2 = 1405, 206
    t()