import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by, keys
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By

op = Options()
op.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=op)

driver.maximize_window()

driver.get("https://www.myntra.com/")

act=ActionChains(driver)


k=driver.find_element(By.LINK_TEXT,"WOMEN")
act.move_to_element(k).pause(2).perform()
# act.move_to_element(k).pause(4).click().perform()
driver.find_element(By.LINK_TEXT,"Footwear").click()

time.sleep(5)
driver.quit()
