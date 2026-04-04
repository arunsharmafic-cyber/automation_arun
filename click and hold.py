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

driver.get("https:/www.kirupa.com/html5/press_and_hold.htm")

act=ActionChains(driver)

circle=driver.find_element(By.ID,"item")
print(circle.location)

act.click_and_hold(circle).perform()

time.sleep(2)

act.release(circle).perform()
# act.scroll_by_amount(0,200).perform()
link=driver.find_element(By.XPATH,"//a[text()='CSS transition']")
act.move_to_element(link).perform()
#
# act.scroll_to_element(link).perform()


sco=ScrollOrigin.from_element(link)
act.scroll_from_origin(sco,0,4500).perform()

time.sleep(5)

driver.quit()