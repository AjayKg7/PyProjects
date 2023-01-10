from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


ser_obj = Service("C:\\Users\\kumar\\PycharmProjects\\SaleniumPojects\\chromedriver.exe")
driver = webdriver.Chrome(service=ser_obj)

# driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//form[@class='_9vtf']/div[2]/button").is_selected()
ele = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//form[@class='_9vtf']/div[2]/button1")))
ele.click()

