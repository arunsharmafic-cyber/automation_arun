import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import by, keys
from selenium.webdriver.common.by import By

op = Options()
op.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=op)

driver.maximize_window()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Chrome()
act = ActionChains(driver)

driver.get("https://www.plus2net.com/javascript_tutorial/ondblclick-demo2.php")

# # Switch to iframe (required)
# fr = driver.find_element(By.CSS_SELECTOR, "[class='demo-frame ']")
# driver.switch_to.frame(fr)
# time.sleep(1)
#
#
# image_to_drag = driver.find_element(
#     By.XPATH, "//img[@alt='The peaks of High Tatras']")
#
#
# place_to_drop = driver.find_element(By.ID, "trash")
#
#
# act.drag_and_drop(image_to_drag, place_to_drop).perform()

box=driver.find_element(By.ID,"box")
act.double_click(box).perform()
time.sleep(2)
act.click(box).perform()
time.sleep(2)



