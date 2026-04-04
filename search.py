from selenium import webdriver
from selenium.webdriver import Keys

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

op = Options()
op.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=op)

driver.maximize_window()

driver.get("https://google.com")
search_box=driver.find_element(By.ID, "APjFqb")

search_box.send_keys("motherson")
search_box.send_keys(Keys.ENTER)



