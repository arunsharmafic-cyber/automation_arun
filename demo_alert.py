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

driver.get("https://demo.automationtesting.in/Alerts.html")

driver.find_element(By.XPATH,"//button[contains(text(),'click the button to display an  alert box')]").click()
time.sleep(2)
driver.switch_to.alert.accept()

time.sleep(4)
driver.find_element(By.XPATH,"//a[text()='Alert with Textbox ']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[text()='click the button to demonstrate the prompt box ']").click()

al=driver.switch_to.alert
al.send_keys("Arun")
al.accept()



