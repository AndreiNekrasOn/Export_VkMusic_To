import pyautogui


def clear_text():
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')


def type_line(line):
    pyautogui.typewrite(line, 0.1)
    pyautogui.press('enter')


def open_url(link, width, height):
    pyautogui.moveTo(width, height, 0.5)
    pyautogui.click()
    clear_text()
    type_line(link)


def navigate_to_find_bar(width, height):
    pyautogui.moveTo(width, height, 0.5)
    pyautogui.click()


def click_like(width, height):
    pyautogui.moveTo(width, height, 0.5)
    pyautogui.click()
