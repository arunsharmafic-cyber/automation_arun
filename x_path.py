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

driver.get("https://www.myntra.com/")

act=ActionChains(driver)

act.scroll_by_amount(0,1800).perform()
img=driver.find_element(By.XPATH,"//img[contains(@src,'f50011b40062e12')]")

img.click()
time.sleep(2)

driver.find_element(By.XPATH, "//h4[contains(text(),'Women Analogue')]").click()








# print(img.location)
# print(img.size)



