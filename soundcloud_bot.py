# -*- coding: utf-8 -*

from search_functions import *
from config import url_sc
import time

pyautogui.FAILSAFE = True
screenWidth, screenHeight = pyautogui.size()
pyautogui.hotkey('alt', 'Tab')
open_url(url_sc, screenWidth * 0.2, screenHeight / 0.06)
time.sleep(5)

for song in open('song_list.txt', 'r', encoding='utf-8'):
    navigate_to_find_bar(screenWidth * 0.5, screenHeight * 0.11)
    clear_text()
    type_line(song)
    time.sleep(2)
    click_like(screenWidth * 0.4, screenHeight * 0.42)
    click_like(screenWidth * 0.4, screenHeight * 0.47)  # he's drunk and can't push like at the first try
