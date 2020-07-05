from selenium import webdriver
import time
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import allure
"""
RUN TEST SUITE IN TERMINAL
py.test -v -s C:\Users\fathih\PycharmProjects\PHPTravel\admin_test_suite

"""

class TestExecution():

    @pytest.mark.run(order=1)
    def test_setUp(self):
        global driver
        driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
        driver.implicitly_wait(10)
        # driver.maximize_window()
        print("Maximized browser")

    @pytest.mark.run(order=2)
    def test_validlogin(self):
        driver.get("http://rentvehicles.multicompetition.com/")

        try:
            assert "Rent Vehicles Dashboard" in driver.title
            print("Assertion Test Pass")
        except Exception as e:
            print("Assertion test failed",format(e))

        assert "rentvehicles" in driver.current_url


    @pytest.mark.run(order=3)
    def test_invalidlogin(self):
        enterEmail = driver.find_element_by_id("email")
        enterEmail.send_keys("admin@gmail.com")
        time.sleep(3)

        enterPassword = driver.find_element_by_id("password")
        enterPassword.send_keys("admin@123")
        time.sleep(3)

        while True:
            try:
                driver.find_element_by_id("btnLogin").click()
            except:
                break
        time.sleep(2)

    @pytest.mark.run(order=4)
    @pytest.mark.timeout(10)
    def test_vahiclePage_section(self):

        clickVehicleDropDown = driver.find_element(By.XPATH, "//p[contains(text(),'Vehicles')]")
        clickVehicleDropDown.click()
        time.sleep(2)

        clickVehicleOwner = driver.find_element_by_xpath("//p[contains(text(),'Vehicle Owners')]")
        clickVehicleOwner.click()
        time.sleep(2)

    @pytest.mark.run(order=5)
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_add_vehicleOwner(self):

        while True:
            try:
                driver.find_element_by_xpath("//a[@class='btn btn-success']").click()
            except:
                break

        time.sleep(3)

        enterOwnerName = driver.find_element_by_id("name")
        enterOwnerName.send_keys("milhan")
        time.sleep(3)

        enterNIC = driver.find_element_by_name("nic")
        enterNIC.send_keys("920012214V")
        time.sleep(3)

        enterPhoneNumber = driver.find_element_by_name("phone_number")
        enterPhoneNumber.send_keys("0528542756")

        performSubmitBtn = driver.find_element_by_xpath("//button[@class='btn btn-primary btn-submit']")
        performSubmitBtn.click()
        time.sleep(3)





    def test_tearDown(self):
        driver.quit()














