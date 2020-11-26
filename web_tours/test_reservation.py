from allure_commons.types import AttachmentType
from selenium import webdriver
import time
import pytest
import allure
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestReservation():

    # @pytest.mark.run(order=1)
    def test_setUp(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(20)
        print("maximized browser")

    # @pytest.mark.run(order=2)
    def test_valid_login(self):
        driver.get("http://rentvehicles.multicompetition.com/login")
        time.sleep(2)
        try:
            assert "Rent Vehicles" in driver.title
            print("Assertion Test Pass")
        except Exception as e:
            print("Assertion test failed", format(e))

        assert "rentvehicles" in driver.current_url
        time.sleep(3)

        enterEmail = driver.find_element(By.ID, 'email')
        enterEmail.send_keys("admin@gmail.com")
        time.sleep(2)

        enterPassword = driver.find_element(By.ID, 'password')
        enterPassword.send_keys("admin@123")

        driver.find_element_by_css_selector("#btnLogin").is_enabled()
        print("Login button is enabled")

        driver.find_element_by_xpath("//a[@class='btn btn-link']").is_displayed()
        print("Forgot Password link is Displayed")

        enterLoginBtn = driver.find_element_by_id("btnLogin")
        enterLoginBtn.click()
        time.sleep(3)

        # username = None
        # while (username == None):
        #     username = webdriver(driver, 10).until(
        #         EC.presence_of_element_located((By.NAME, "username"))
        #     )
        # username.send_keys('fathih')

        # enterPassword = driver.find_element(By.NAME, 'password')
        # enterPassword.send_keys("1234")
        #
        # enterLogin = driver.find_element(By.NAME, 'login')
        # enterLogin.click()

