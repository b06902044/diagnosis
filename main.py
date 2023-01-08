import time
import os
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

MAIN_PAGE = "http://wonder.vghtc.gov.tw:8100/SmartWonder.Verify/indexTEDPC.jsp"

def get_firefox_driver():
    cwd = os.getcwd()
    driver = webdriver.Firefox(executable_path = cwd + "/geckodriver")
    driver.get(MAIN_PAGE)
    return driver

def login(driver):
    driver.find_element_by_name('WonderID').send_keys('G806')
    driver.find_element_by_name('WonderPassword').send_keys('G000000')
    driver.find_element_by_name('login').click()

    try:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ENTER)
    except:
        print("got error from backend as expected")

def quit(driver):
    time.sleep(5)
    driver.quit() 

if __name__ == '__main__':
    driver = get_firefox_driver()
    login(driver)
    # quit(driver)



