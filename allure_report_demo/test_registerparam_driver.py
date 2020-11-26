from allure_commons.types import AttachmentType
from selenium import webdriver
import time
import pytest
import allure
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestDrivers():

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=1)
    def test_setUp(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        print("maximized browser")
        #https://confident-dijkstra-ca012d.netlify.app/

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.run(order=2)
    def test_verify_WebPage(self):
        driver.get("http://rentvehicles.multicompetition.com/login")

        status=driver.find_element_by_xpath("//a[@class='navbar-brand']").is_displayed()
        if status==True:
            assert True
        else:
            allure.attach(driver.get_screenshot_as_png(),name="testLoginScreen",
                          attachment_type=AttachmentType.PNG)
            assert False

        try:
            assert "Rent Vehicles Dashboard" in driver.title
            print("Assertion Test Pass")
        except Exception as e:
            print("Assertion test failed", format(e))

        assert "rentvehicles" in driver.current_url


    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.run(order=3)
    def test_invalid_login(self):

        enter_username("admin@gmail.com")

        enter_username("admin@123")

        enterLoginBtn = driver.find_element_by_id("btnLogin")
        enterLoginBtn.click()

        verifyWrongEmailErrorMessage = driver.find_element(By.XPATH, "//strong[contains(text(),'These credentials do not match our records.')]")
        assert verifyWrongEmailErrorMessage.text == "These credentials do not match our records."

        time.sleep(2)


    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.run(order=4)
    # @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.timeout(20)
    def test_valid_login(self):
        driver.refresh()

        enter_username("admin@gmail.com")

        enter_username("admin@1234")

        enterLoginBtn = driver.find_element_by_id("btnLogin")
        enterLoginBtn.click()

    @allure.step("Entering username as {0}")
    def enter_username(self, username):
        driver.find_element(By.ID, 'email').send_keys(username)

    @allure.step("Entering password as {0}")
    def enter_password(self, password):
        driver.find_element(By.ID, 'password').send_keys(password)


    @allure.severity(allure.severity_level.NORMAL)
    # @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.run(order=5)
    def test_navigate_driver_section(self):
        driver.find_element_by_xpath("/html/body/div[1]/aside[1]/div/div[4]/div/div/nav/ul/li[2]/a").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//p[contains(text(),'Register Drivers')]").click()
        time.sleep(2)



    def test_tearDown(self):
        driver.quit()