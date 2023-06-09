import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self): 
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.browser = driver
        
    def test_a_success_login(self): 
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

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[1]/span/h6").text

        self.assertIn('Dashboard', response_data)
        self.assertEqual(browser.current_url, "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index") # cek url ke dashboard

    def test_a_failed_login_with_empty_password(self):
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,".orangehrm-login-button[data-v-358db50f]").click() # klik login
        time.sleep(1)

        # validasi
        response_data_password = browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span").text

        self.assertIn('Required', response_data_password)

    def test_a_failed_login_with_empty_username(self):
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,".orangehrm-login-button[data-v-358db50f]").click() # klik login

        # validasi
        response_data_username = browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span").text

        self.assertIn('Required', response_data_username)

    def test_a_failed_login_with_empty_username_and_password(self):
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,".orangehrm-login-button[data-v-358db50f]").click() # klik login
        time.sleep(1)

        # validasi
        response_data_username = browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/span").text
        response_data_password = browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span").text

        self.assertIn('Required', response_data_username)
        self.assertIn('Required', response_data_password)

    def test_a_failed_login_with_wrong_username_and_password(self):
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("addminn") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("321admmiinn") # isi password
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,".orangehrm-login-button[data-v-358db50f]").click() # klik login
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p").text

        self.assertIn('Invalid credentials', response_data)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__": 
    unittest.main()


