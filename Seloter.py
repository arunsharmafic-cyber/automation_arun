import time

from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by, keys
from selenium.webdriver.common.by import By

op = Options()
op.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=op)

driver.maximize_window()

driver.maximize_window()
driver.get("https://www.flipkart.com/")

search_box=driver.find_element(By.LINK_TEXT,"Login")

search_box.send_keys(Keys.ENTER)


time.sleep(3)
search_box_1=driver.find_element(By.CSS_SELECTOR,"c3Bd2c")


search_box_1.send_keys("7037189677")
search_box.send_keys(Keys.ENTER)
