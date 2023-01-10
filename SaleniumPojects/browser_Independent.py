import time

from selenium import webdriver
import os

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


location = os.getcwd()

class Browsers:
    def chrome_setup(self):
        from selenium.webdriver.chrome.service import Service

        service_obj = Service(executable_path="C:\\Users\\kumar\\PycharmProjects\\SaleniumPojects\\chromedriver.exe")
        preferences = {"download.default_directory":location}
        ops = webdriver.ChromeOptions()
        ops.add_experimental_option("prefs",preferences)
        driver = webdriver.Chrome(service=service_obj, options=ops)
        return driver

    def edge_setup(self):
        from selenium.webdriver.edge.service import Service
        # sscap = DesiredCapabilities.EDGE()
        # sscap.setCapability(.ACCEPT_SSL_CERTS, True)

        service_obj = Service(executable_path="C:\\Users\\kumar\\PycharmProjects\\SaleniumPojects\\msedgedriver.exe")
        preferences = {"download.default_directory": location,"webdriver.load.strategy":"unstable"}
        ops = webdriver.EdgeOptions()
        ops.add_experimental_option("prefs", preferences)
        driver = webdriver.Chrome(service=service_obj, options=ops)
        return driver



driver = Browsers().edge_setup()
driver.get("https://filesamples.com/formats/doc")
driver.maximize_window()
ele = driver.find_element(By.XPATH,"//main[@class='col-12 main-content rounded-bg marg-top padd-top']//div[1]//a[1]")
driver.execute_script("arguments[0].scrollIntoView();",ele)
sel = Select(webelement=ele)
lst = sel.options
time.sleep(10)
driver.save
wait = WebDriverWait(driver, 30).until((EC.element_to_be_clickable(driver.find_element(By.XPATH,"//main[@class='col-12 main-content rounded-bg marg-top padd-top']//div[1]//a[1]"))))
wait.click()
driver.switch_to.frame(driver.find_element(By.ID,'ad_iframe'))
WebDriverWait(driver,30).until((EC.presence_of_element_located(driver.find_element(By.XPATH,'//*[@id="dismiss-button"]')))).click()


