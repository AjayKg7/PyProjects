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
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
driver.maximize_window()

time.sleep(3)
f1=driver.find_element(By.XPATH,'//*[@id="post-2669"]/div[2]/div/div/div[1]/p/iframe')
driver.switch_to.frame(f1)
act = ActionChains(driver)
srcs = driver.find_elements(By.XPATH,'//ul[@id="gallery"]/li/img')
tgt = driver.find_element(By.ID,'trash')
for i in srcs:
    act.drag_and_drop(i, tgt).perform()
    time.sleep(2)
    




time.sleep(3)



