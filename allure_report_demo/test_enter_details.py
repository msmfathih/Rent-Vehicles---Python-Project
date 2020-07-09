from selenium import webdriver
import time
import pytest
import allure
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager


class TestDrivers2():

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=6)
    def test_setUp(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        driver.implicitly_wait(10)

    @allure.severity(allure.severity_level.CRITICAL)
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

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=8)
    def test_navigate_driver_section2(self):
        driver.find_element_by_xpath("/html/body/div[1]/aside[1]/div/div[4]/div/div/nav/ul/li[2]/a").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//p[contains(text(),'Register Drivers')]").click()
        time.sleep(2)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=9)
    def test_fill_formSection1(self):
        driverName = driver.find_element_by_xpath("//input[@name='name']")
        driverName.send_keys("testuser")


        phoneNumber = driver.find_element(By.NAME, 'mobile_number')
        phoneNumber.send_keys("0528542762")
        # email = ""
        # for x in range(1,5):
        #     email = "ijaz"+str(x)+'@gmail.com'

        emailID = driver.find_element(By.XPATH, "//input[@name='email']")
        emailID.send_keys("user1@gmail1.com")
        #emailID.send_keys(email)

        password = driver.find_element_by_xpath("//input[@name='password']")
        password.send_keys("12346556")

        enterNIC = driver.find_element_by_xpath("//input[@name='nic']")
        enterNIC.send_keys("9200122134V")

    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.timeout(10)
    @pytest.mark.run(order=10)
    def test_upload_licenece_copy_file(self):
        uploadFile = driver.find_element_by_id("name")
        uploadFile.send_keys(
            "C://Users//fathih//PycharmProjects//RentVehicles//driver_registration_flow//Image//python.png")
        time.sleep(3)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.skip(reason="licence backcopy is not mendatory")
    @pytest.mark.run(order=11)
    def test_upload_licenece_backcopy_file(self):
        uploadFile2 = driver.find_element_by_name("licence_copy")
        uploadFile2.send_keys(
            "C://Users//fathih//PycharmProjects//RentVehicles//driver_registration_flow//Image//python.png")
        time.sleep(3)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=12)
    def test_enter_vehicle_number(self):
        enterVehicleNumber = driver.find_element_by_xpath("//input[@name='vehicle_number']")
        enterVehicleNumber.send_keys("6655663265")
        time.sleep(3)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=13)
    def test_vehicle_owner_radiobtn(self):
        element = driver.find_element_by_css_selector("input.is_vehicle_owner:nth-child(4)")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(3)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=14)
    def test_select_vehicle_ownername(self):
        element1 = driver.find_element_by_xpath("//select[@name='owner_id']")
        sel = Select(element1)
        sel.select_by_index(2)
        time.sleep(3)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=15)
    def test_select_vehicle_type(self):
        element2 = driver.find_element_by_xpath("//select[@name='vehicle_type_id']")
        sel2 = Select(element2)
        sel2.select_by_index(2)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=16)
    def test_upload_vehicle_picture(self):
        uploadFile = driver.find_element_by_xpath("//input[@name='vehicle_picture']")
        uploadFile.send_keys(
            "C://Users//fathih//PycharmProjects//RentVehicles//driver_registration_flow//Image//python.png")
        time.sleep(2)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=17)
    def test_enter_engine_number(self):
        engine_number = driver.find_element_by_xpath("//input[@name='engine_number']")
        engine_number.send_keys("EP-HQ8165")

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=18)
    def test_enter_chassis_number(self):
        engine_number = driver.find_element_by_xpath("//input[@name='chassis_number']")
        engine_number.send_keys("EP-HQ8165645")

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.timeout(19)
    @pytest.mark.run(order=18)
    def test_upload_vehicle_regcopy(self):
        uploadFile = driver.find_element_by_xpath("//input[@name='vehicle_registration_copy']")
        uploadFile.send_keys(
            "C://Users//fathih//PycharmProjects//RentVehicles//driver_registration_flow//Image//python.png")
        time.sleep(2)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.timeout(10)
    @pytest.mark.run(order=20)
    def test_upload_driver_photo(self):
        uploadFile = driver.find_element_by_xpath("//input[@name='photo']")
        uploadFile.send_keys(
            "C://Users//fathih//PycharmProjects//RentVehicles//driver_registration_flow//Image//python.png")
        time.sleep(2)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=21)
    def test_upload_driver_photo(self):
        uploadFile = driver.find_element(By.XPATH, "//input[@name='photo']")
        uploadFile.send_keys(
            "C://Users//fathih//PycharmProjects//RentVehicles//driver_registration_flow//Image//python.png")
        time.sleep(2)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=22)
    def test_parking_location(self):
        uploadFile = driver.find_element(By.XPATH, "//input[@name='parking_location']")
        uploadFile.send_keys("Abu Dhabi parking-01")
        time.sleep(2)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=23)
    def test_prefer_timingfrom(self):
        uploadFile = driver.find_element(By.XPATH, "//input[@name='prefer_time_from']")
        uploadFile.send_keys("12:10 PM")
        time.sleep(2)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=24)
    def test_prefer_timingfrom2(self):
        uploadFile = driver.find_element(By.XPATH, "//input[@name='prefer_time_to']")
        uploadFile.send_keys("5:00 PM")
        time.sleep(2)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=25)
    def test_prefer_location(self):
        prefer_location = driver.find_element_by_xpath("//select[@name='prefer_location_to_hire']")
        select = Select(prefer_location)
        select.select_by_index(0)
        time.sleep(3)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.run(order=26)
    def test_submit_details(self):
        element = driver.find_element_by_id("submitBtn")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(10)


    def test_tearDown(self):
        driver.quit()