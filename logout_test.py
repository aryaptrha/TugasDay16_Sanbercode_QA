import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLogout(unittest.TestCase):

    def setUp(self): 
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser = driver

    def test_a_success_logut(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,".orangehrm-login-button[data-v-358db50f]").click() # klik login
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span").click() # klik panel
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a").click() # klik logout
        time.sleep(3)

        # verify
        self.assertEqual(browser.current_url, "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # cek url kembali ke halaman login

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__": 
    unittest.main()