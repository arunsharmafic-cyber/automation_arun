import time

# from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

op = Options()
op.add_experimental_option("detach", True)
driver= webdriver.Chrome(options=op)

driver.maximize_window()
driver.get("https://www.sleepwellfoundation.com/about.php")

print("the tittle of sleepwell foundation is :",driver.title)

print("the current url is :",driver.current_url)
#
time.sleep(5)
# driver.close()

driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(6)
driver.fullscreen_window()
time.sleep(7)
# driver.quit()
driver.minimize_window()

s= driver.get_window_size()

print("hight and width of the windos is ",s)

driver.set_window_size( 300, 400)
print("the x cordinate and y of the windos::",driver.get_window_position())

driver.set_window_position(50,70)
# driver.close()

print(driver.current_window_handle)
print(driver.window_handles)


