from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability('unhandledPromptBehavior', 'accept')

driver = webdriver.Chrome(executable_path = "C:\\Users\\kumar\\PycharmProjects\\SaleniumPojects\\chromedriver.exe",options=chrome_options)

# driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
count = 0
while count<4:
    driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[1]/button').click()
    # dralert=driver.switch_to.alert
    # dralert.accept()
    time.sleep(10)
    count+=1



