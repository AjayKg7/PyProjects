from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability('unhandledPromptBehavior', 'accept')
ser_obj = Service("C:\\Users\\kumar\\PycharmProjects\\SaleniumPojects\\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj,options=chrome_options)

# driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/demo-site/sliders/")
driver.maximize_window()

time.sleep(3)
f1=driver.find_element(By.XPATH,'//*[@id="post-2673"]/div[2]/div/div/div[1]/p/iframe')
driver.switch_to.frame(f1)

red=driver.find_element(By.XPATH,'//*[@id="red"]/span')
green = driver.find_element(By.XPATH,'//*[@id="green"]/span')
blue = driver.find_element(By.XPATH,'//*[@id="blue"]/span')
act = ActionChains(driver)
act.drag_and_drop_by_offset(red,-100,0).perform()
act.drag_and_drop_by_offset(green,50,0).perform()
act.drag_and_drop_by_offset(blue,100,0).perform()

