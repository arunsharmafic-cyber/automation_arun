import time

import sct
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

driver.get("https://demoqa.com/select-menu")

cars=driver.find_element(By.ID,"cars")

# cars.send_keys("volvo")
# cars.send_keys(Keys.ENTER)

# sct=Select(cars)

# op=sct.options
#
# print(len(op))
#
# print(sct.is_multiple)

# for dropdown in op:
#     print(dropdown.text)
#     time.sleep(2)
#     # dropdown.click()
# # sct.deselect_all()
# sct.select_by_index(0)
# sct.select_by_index(1)
#
# all_selected=sct.all_selected_options
# for selected in all_selected:
#     print(selected.text)
#
# print("the frist selected option is:::",sct.first_selected_option,)
#
# # sct.deselect_all()

