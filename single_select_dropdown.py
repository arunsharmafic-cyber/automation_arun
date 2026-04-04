import time

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

driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/#google_vignette")

act=ActionChains(driver)

driver.find_element(By.TAG_NAME,"select")
drop=driver.find_element(By.TAG_NAME,"select")

sct=Select(drop)
print(sct.is_multiple)

opt=sct.options
print(len(opt))



# for country_name in opt:
# print(country_name.text)
#   country_name.click()
sct.select_by_value("ASM")
time.sleep(1)
sct.select_by_index(25)
time.sleep(2)
sct.select_by_visible_text("Zimbabwe")
time.sleep(1)


# driver.quit()
# select class se drop down ko locate kr sakte h
