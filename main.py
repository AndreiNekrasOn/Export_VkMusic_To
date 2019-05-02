# -*- coding: utf-8 -*

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import codecs
from config import *

options = Options()
options.headless = True
prefs = {'profile.managed_default_content_settings.images': 2}  # no images loaded, similar to depreciated FantomJS
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=options)

driver.get(url_vk)

email_input = driver.find_element_by_id("email")
email_input.send_keys(vk_phone)
password_input = driver.find_element_by_id("pass")
password_input.send_keys(vk_pswd)
btn = driver.find_element_by_id("login_button")
btn.click()

lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);"
                                  "var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while not match:
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);"
                                          "var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount == lenOfPage:
            match = True
audios = driver.find_elements_by_css_selector(".audio_row_content")

songs = []
clear_reg = re.compile('[^a-zA-Zа-яА-Я \-]')
for audio in audios:
        author = audio.find_element_by_css_selector(".artist_link").text.rstrip()
        song = audio.find_element_by_css_selector(".audio_row__title_inner").text.rstrip()
        songs.append((clear_reg.sub('', author), clear_reg.sub('', song)))

driver.close()

file = codecs.open("song_list.txt", 'w', encoding="utf-8")
for song in songs:
    print(song[0], song[1], sep=' - ', file=file)
