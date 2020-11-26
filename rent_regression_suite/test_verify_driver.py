from selenium import webdriver
import time
import pytest
import allure
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


class TestDrivers3():

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=27)
    def test_setUp(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        print("maximized browser")

    @allure.description("validate page title and current URL")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=28)
    def test_valid_login(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://rentvehicles.multicompetition.com/login")
        time.sleep(2)
        try:
            assert "Rent Vehicles" in driver.title
            print("Assertion Test Pass")
        except Exception as e:
            print("Assertion test failed", format(e))

        assert "rentvehicles" in driver.current_url

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


    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.run(order=29)
    def test_navigate_driver_section(self):
        driver.find_element_by_xpath("/html/body/div[1]/aside[1]/div/div[4]/div/div/nav/ul/li[2]/a").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//p[contains(text(),'Drivers List')]").click()
        time.sleep(2)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=30)
    def test_driver_list_view(self):
        click_action_view = driver.find_element_by_xpath("//tr[4]//td[6]//a[1]")
        click_action_view.click()
        time.sleep(3)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=31)
    def test_verify_driver_name(self):
        verify_drivername = driver.find_element_by_xpath("//label[contains(text(),'Driver Name : aadil')]")
        elementText = verify_drivername.text
        print("Text on element is " + elementText)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=32)
    def test_verify_driver_email(self):
        verify_email = driver.find_element_by_xpath("//label[contains(text(),'Email : aadil@gmail1.com')]")
        elementText = verify_email.text
        print("Text on element is " + elementText)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=33)
    def test_verify_nic_number(self):
        verify_nic = driver.find_element_by_xpath("//label[contains(text(),'NIC Number: 9200122134V')]")
        elementText = verify_nic.text
        print("Driver NIC is "+elementText)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=34)
    def test_verify_phonenumber(self):
        verify_phoneNumber = driver.find_element_by_xpath("//label[contains(text(),'Phone Number : 0528542762')]")
        elementText = verify_phoneNumber.text
        print("Driver Phone number is "+elementText)
        time.sleep(3)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=35)
    def test_logout_app(self):
        driver.find_element_by_xpath("//p[contains(text(),'Need to logout ?')]").click()
        time.sleep(2)
        driver.find_element_by_xpath("//p[contains(text(),'Logout')]").click()
        time.sleep(3)


    def test_tearDown(self):
        driver.quit()




