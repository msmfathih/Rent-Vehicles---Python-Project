from selenium import webdriver
import time
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


class TestDrivers2():

    @pytest.mark.run(order=6)
    def test_setUp(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
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

    @pytest.mark.timeout(10)
    @pytest.mark.run(order=10)
    def test_upload_licenece_copy_file(self):
        uploadFile = driver.find_element_by_id("name")
        uploadFile.send_keys("C://Users//fathih//PycharmProjects//RentVehicles//driver_registration_flow//Image//python.png")
        time.sleep(3)

    @pytest.mark.skip(reason="licence backcopy is not mendatory")
    @pytest.mark.run(order=11)
    def test_upload_licenece_backcopy_file(self):
        uploadFile2 = driver.find_element_by_name("licence_copy")
        uploadFile2.send_keys("C://Users//fathih//PycharmProjects//RentVehicles//driver_registration_flow//Image//python.png")
        time.sleep(3)

    @pytest.mark.run(order=12)
    def test_enter_vehicle_number(self):
        enterVehicleNumber = driver.find_element_by_xpath("//input[@name='vehicle_number']")
        enterVehicleNumber.send_keys("6655663265")

    @pytest.mark.run(order=13)
    def test_vehicle_owner_radiobtn(self):
        element = driver.find_element_by_css_selector("input.is_vehicle_owner:nth-child(4)")
        driver.execute_script("arguments[0].click();", element)

    def test_select_values(self):
        element = driver.find_element_by_id("owner_id")



    # @pytest.mark.run(order=14)
    # def test_select_owner_name(self):
    #     selectOwnerName = driver.find_elements_by_id("owner_id")
    #     select = Select(selectOwnerName)
    #     select.select_by_value("milhan")
    #     time.sleep(2)






    #
    # def test_tearDown(self):
    #     driver.quit()