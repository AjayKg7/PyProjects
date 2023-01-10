from selenium.webdriver.support.ui import Select
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
driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
driver.maximize_window()

time.sleep(2)
d1 = driver.find_element(By.XPATH, '//*[@id="post-2646"]/div[2]/div/div/div/p/select')
sel = Select(d1)
sel.select_by_visible_text("New Zealand")
