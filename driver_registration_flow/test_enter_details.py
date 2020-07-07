from selenium import webdriver
import time
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class TestDrivers2():

    @pytest.mark.run(order=6)
    def test_setUp(self):
        global driver
        driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
        driver.implicitly_wait(10)


    @pytest.mark.run(order=7)
    def test_valid_login2(self):
        driver.get("http://rentvehicles.multicompetition.com/login")
        enterEmail = driver.find_element(By.ID, 'email')
        enterEmail.send_keys("admin@gmail.com")
        time.sleep(2)

        enterPassword = driver.find_element(By.ID, 'password')
        enterPassword.send_keys("admin@123")

        enterLoginBtn = driver.find_element_by_id("btnLogin")
        enterLoginBtn.click()
        time.sleep(3)


    @pytest.mark.run(order=8)
    def test_navigate_driver_section2(self):
        driver.find_element_by_xpath("/html/body/div[1]/aside[1]/div/div[4]/div/div/nav/ul/li[2]/a").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//p[contains(text(),'Register Drivers')]").click()
        time.sleep(2)


    @pytest.mark.run(order=9)
    def test_fill_formSection1(self):
        driverName = driver.find_element_by_xpath("//input[@name='name']")
        driverName.send_keys("testuser")

        phoneNumber = driver.find_element(By.NAME, 'mobile_number')
        phoneNumber.send_keys("0528542762")

        emailID = driver.find_element(By.XPATH, "//input[@name='email']")
        emailID.send_keys("user@gmail.com")

        password = driver.find_element_by_xpath("//input[@name='password']")
        password.send_keys("12346556")

        enterNIC = driver.find_element_by_xpath("//input[@name='nic']")
        enterNIC.send_keys("9200122134V")

    @pytest.mark.run(order=9)
    def test_upload_licenece_copy_file(self):
        uploadFile = driver.find_element_by_id("name")
        uploadFile.send_keys("C://Users//fathih//PycharmProjects//RentVehicles//driver_registration_flow//Image//python.png")
        time.sleep(5)

    @pytest.mark.run(order=9)
    def test_upload_licenece_backcopy_file(self):
        uploadFile2 = driver.find_element_by_id("name")
        uploadFile2.send_keys("C://Users//fathih//PycharmProjects//RentVehicles//driver_registration_flow//Image//python.pngs")
        time.sleep(5)




    def test_tearDown(self):
        driver.quit()