import time

from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

op = Options()
op.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=op)

driver.maximize_window()
driver.get("https://www.myntra.com/")

search_box=driver.find_element(By.CLASS_NAME,"desktop-searchBar")


search_box.send_keys("man tshirt")
search_box.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()