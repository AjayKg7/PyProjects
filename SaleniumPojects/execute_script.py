from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability('unhandledPromptBehavior', 'accept')
ser_obj = Service("C:\\Users\\kumar\\PycharmProjects\\SaleniumPojects\\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj,options=chrome_options)

# driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Flag#:~:text=A%20flag%20is%20a%20piece,signalling%20device%2C%20or%20for%20decoration.")
driver.maximize_window()

time.sleep(2)
# loc = driver.execute_script("return window.document.body.scrollHeight;")
# value = int(loc)//2
# driver.execute_script("window.scrollBy(0,"+ str(value*2)+")")
# loc = driver.execute_script("return window.pageYOffset;")

#method2
ele = driver.find_element(By.XPATH, '//div[22]//div[1]//a[1]//img[1]')
driver.execute_script("arguments[0].scrollIntoView();", ele)
loc = driver.execute_script("return window.pageYOffset;")
print(loc)

time.sleep(5)

