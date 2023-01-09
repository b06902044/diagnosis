import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

MAIN_PAGE = "http://wonder.vghtc.gov.tw:8100/SmartWonder.Verify/indexTEDPC.jsp"

class Protocol:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.contrast = ""
        
    def switch_frame(self, sel, str):
        element = self.driver.find_element(sel, str)
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(element))

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
    
    def get_contrast(self):
        self.switch_frame(By.NAME, "frameOrder")
        contrast = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "attentionData"))).text
        print(contrast)
        self.driver.switch_to.default_content()
        time.sleep(3)
    
    def get_patient(self):
        self.switch_frame(By.NAME, "frameQuery")
        self.wait.until(EC.frame_to_be_available_and_switch_to_it("frameWorklist"))
        
        self.wait.until(EC.element_to_be_clickable((By.ID,"lstBdyQuery")))
        # print(self.driver.page_source)
        patients = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"#lstBdyQuery tr")))
        for p in patients:
            actions = ActionChains(self.driver)
            actions.move_to_element(p).perform()
            time.sleep(3)
            p.click()
            self.get_contrast()

    def quit(self):
        time.sleep(5)
        self.driver.quit()