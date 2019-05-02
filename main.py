# -*- coding: utf-8 -*

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import codecs
from config import vk_login, vk_pswd, url_vk


def auth(id, data):
    driver.find_element_by_id(id).send_keys(data)


def set_options():
    options = Options()
    options.headless = True
    prefs = {'profile.managed_default_content_settings.images': 2}  # no images loaded, similar to depreciated FantomJS
    options.add_experimental_option("prefs", prefs)
    return options


def scroll_down(script):
    len_of_page = driver.execute_script(script)
    match = False
    while not match:
        last_count = len_of_page
        time.sleep(1)
        len_of_page = driver.execute_script(script)
        if last_count == len_of_page:
            match = True


def parse_audio_div(div, selector):
    return div.find_element_by_css_selector(selector).text


def write_songs(_songs):
    file = codecs.open("song_list.txt", 'w', encoding="utf-8")
    for s in _songs:
        print(s[0], s[1], sep=' - ', file=file)


driver = webdriver.Chrome(options=set_options())
driver.get(url_vk)

auth("email", vk_login)
auth("pass", vk_pswd)
driver.find_element_by_id("login_button").click()

scroll_script = "window.scrollTo(0, document.body.scrollHeight);"\
                "var lenOfPage=document.body.scrollHeight;return lenOfPage;"

scroll_down(scroll_script)

audios = driver.find_elements_by_css_selector(".audio_row_content")

songs = []
clear_reg = re.compile('[^a-zA-Zа-яА-Я \-]')
for audio in audios:
        author = parse_audio_div(audio, ".artist_link")
        song = parse_audio_div(audio, ".audio_row__title_inner")
        songs.append((author, song))

map(clear_reg.sub, ('', songs))
driver.close()

