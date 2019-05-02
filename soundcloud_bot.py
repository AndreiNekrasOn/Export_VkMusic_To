# -*- coding: utf-8 -*

import pyautogui
import time
import keyboard


def navigate_to_find_bar(width, height):
    pyautogui.moveTo(width / 2, height / 10)
    pyautogui.click()


def clear_text():
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')


def type_line(line):
    pyautogui.typewrite(line, 0.1)
    pyautogui.press('enter')


def click_like(width, height):
    pyautogui.moveTo(width * 0.4, height * 0.42)
    pyautogui.click()
    pyautogui.moveTo(width * 0.4, height * 0.47)  # he's drunk and can't push like at the first try
    pyautogui.click()


if __name__ == '__main__':
    pyautogui.FAILSAFE = True
    screenWidth, screenHeight = pyautogui.size()
    pyautogui.hotkey('alt', 'Tab')
    for song in open('song_list.txt', 'r', encoding='utf-8'):
        navigate_to_find_bar(screenWidth, screenHeight)
        clear_text()
        type_line(song)
        time.sleep(3)
        click_like(screenWidth, screenHeight)

