import time
import patient

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

MAIN_PAGE = "http://wonder.vghtc.gov.tw:8100/SmartWonder.Verify/indexTEDPC.jsp"

class Protocol:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.contrast = ""
        
    def switch_frame(self, sel, str):
        element = self.driver.find_element(sel, str)
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(element))
    
    def switch_default(self):
        self.driver.switch_to.default_content()

    def login(self):
        self.driver.get(MAIN_PAGE)
        self.driver.find_element_by_name('WonderID').send_keys('G806')
        self.driver.find_element_by_name('WonderPassword').send_keys('G000000')
        self.driver.find_element_by_name('login').click()

        try:
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ENTER)
        except:
            print("got error from backend as expected")

    def switch_to_main_page(self):
        self.switch_frame(By.ID, "frameMenu")
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'menuBarText'))).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)
        
    def get_patient(self):
        self.switch_frame(By.NAME, "frameOrder")
        contrast = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "attentionData"))).text
        diagnosis = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "txtDiag"))).text
        self.switch_default()
        return patient.Patient(contrast=contrast, diagnosis=diagnosis)
        
    def has_patient(self):
        self.switch_frame(By.NAME, "frameQuery")
        self.wait.until(EC.frame_to_be_available_and_switch_to_it("frameWorklist"))
        
        exist = True
        try:
            self.driver.find_element(By.ID,"lstBdyQuery")
        except:
            exist = False
            
        self.switch_default()
        return exist
    
    def write_result(self, result):
        print("write reuslt = ", result)
        self.switch_frame(By.NAME, "frameInfo")
        self.wait.until(EC.presence_of_element_located((By.NAME, "Recommendation"))).send_keys(result)
        self.switch_default()
    
    def do(self):
        if self.has_patient(): # Todo: change to while
            p = self.get_patient()
            print("got patient with contrast = ", p.contrast)
            print("got patient with diag = ", p.diagnosis)
            
            result = p.get_result()
            if result != "":
                print("write and store result")
                self.write_result(result)
            
            time.sleep(3)
            
        print("there is no patient")

    def quit(self):
        time.sleep(5)
        self.driver.quit()