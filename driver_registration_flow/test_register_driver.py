from selenium import webdriver
import time
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class TestDrivers():

    @pytest.mark.run(order=1)
    def test_setUp(self):
        global driver
        driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
        driver.implicitly_wait(10)
        print("maximized browser")


    @pytest.mark.run(order=2)
    def test_verify_WebPage(self):
        driver.get("http://rentvehicles.multicompetition.com/login")

        try:
            assert "Rent Vehicles Dashboard" in driver.title
            print("Assertion Test Pass")
        except Exception as e:
            print("Assertion test failed", format(e))

        assert "rentvehicles" in driver.current_url



    @pytest.mark.run(order=3)
    def test_invalid_login(self):
        enterEmail = driver.find_element(By.ID, 'email')
        enterEmail.send_keys("admin@gmail.com")
        time.sleep(2)

        enterPassword = driver.find_element(By.ID, 'password')
        enterPassword.send_keys("admin@1234")

        enterLoginBtn = driver.find_element_by_id("btnLogin")
        enterLoginBtn.click()

        verifyWrongEmailErrorMessage = driver.find_element(By.XPATH, "//strong[contains(text(),'These credentials do not match our records.')]")
        assert verifyWrongEmailErrorMessage.text == "These credentials do not match our records."

        driver.refresh()
        time.sleep(2)

    @pytest.mark.run(order=4)
    # @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.timeout(20)
    def test_valid_login(self):
        enterEmail = driver.find_element(By.ID, 'email')
        enterEmail.send_keys("admin@gmail.com")

        enterPassword = driver.find_element(By.ID, 'password')
        enterPassword.send_keys("admin@123")

        enterLoginBtn = driver.find_element_by_id("btnLogin")
        enterLoginBtn.click()


    # @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.run(order=5)
    def test_navigate_driver_section(self):
        driver.find_element_by_xpath("/html/body/div[1]/aside[1]/div/div[4]/div/div/nav/ul/li[2]/a").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//p[contains(text(),'Register Drivers')]").click()
        time.sleep(2)






    def test_tearDown(self):
        driver.quit()