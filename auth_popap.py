import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by, keys
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

op = Options()
op.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=op)

driver.maximize_window()

# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.get("https://the-internet.herokuapp.com/basic_auth")


pyautogui.write("admin")
pyautogui.press("tab")
pyautogui.write("admin")
pyautogui.press("enter")

