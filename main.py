import protocol
import utils
import os
from selenium import webdriver

def getProtocol():
    cwd = os.getcwd()
    driver = webdriver.Firefox(executable_path = cwd + "/geckodriver")
    return protocol.Protocol(driver)

if __name__ == '__main__':
    utils.init()
    # p = getProtocol()    

    # p.login()
    # p.switch_to_main_page()
    # p.get_contrast()

    # p.quit()
    
    