from selenium import webdriver
import time
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import allure



class TestExecution():

    @pytest.mark.run(order=5)
    def test_setUp(self):
        global driver
        driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
        driver.implicitly_wait(10)
        # driver.maximize_window()
        print("Maximized browser")

    @pytest.mark.timeout(10)
    @pytest.mark.run(order=2)
    def test_validlogin(self):
        driver.get("http://rentvehicles.multicompetition.com/")

        try:
            assert "Rent Vehicles Dashboard" in driver.title
            print("Assertion Test Pass")
        except Exception as e:
            print("Assertion test failed",format(e))

        assert "rentvehicles" in driver.current_url


    # @allure.description("Validates Rent-vehicle admin login")
    # @allure.severity(severity_level="CRITICAL")
    # @pytest.mark.skip(reason="no way of currently testing this")
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


    # @allure.description("Navigates into vehicle owner section")
    # @allure.severity(severity_level="Low")
    @pytest.mark.timeout(5)
    @pytest.mark.run(order=4)
    def test_vahiclePage_section(self):

        clickVehicleDropDown = driver.find_element(By.XPATH, "//p[contains(text(),'Vehicles')]")
        clickVehicleDropDown.click()
        time.sleep(2)

        clickVehicleOwner = driver.find_element_by_xpath("//p[contains(text(),'Vehicle Owners')]")
        clickVehicleOwner.click()
        time.sleep(2)

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


    @pytest.mark.timeput(3)
    def test_verify_ownerName(self):
        assert "vehicle-owners" in driver.current_url

        #Screenshot capture onlynfor failure scenario
        # try:
        #     assert "vehicle-owners" in driver.current_url
        # finally:
        #     if(AssertionError):
        #         allure.attach(driver.get_screenshot_as_png(),
        #                       name="Invalid URL",attachment_type=allure.attachment_type.PNG)

        verifyVehicleOwnerText = driver.find_element(By.XPATH, "//h1[@class='m-0 text-dark']")
        assert verifyVehicleOwnerText.text == 'Vehicle Owners'

        clickVehicleDropDown = driver.find_element(By.XPATH, "//p[contains(text(),'Vehicles')]")
        clickVehicleDropDown.click()
        time.sleep(3)

        clickVehicleOwner = driver.find_element_by_xpath("//p[contains(text(),'Vehicle Owners')]")
        clickVehicleOwner.click()
        time.sleep(5)

        #Verify owner name : method 1
        # verifyOwnerName = driver.find_element_by_xpath("//td[contains(text(),'milhan')]")
        # elementText = verifyOwnerName.text
        # print("Vehicle owner name is " + elementText)

        # Verify owner name : method 2
        verifyOwnerName = driver.find_element_by_xpath("//td[contains(text(),'milhan')]")
        assert verifyOwnerName.text == 'milhan'
        print("New vehicle owner name is "+str(verifyOwnerName))


    # @allure.description("Validating New Vehicle owner Phone Number")
    # @allure.severity(severity_level="Medium")
    def test_phone_number(self):
        verifyPhoneNumber = driver.find_element_by_xpath("//td[contains(text(),'0528542756')]")
        assert verifyPhoneNumber.text == '0528542756'
        print("New vehicle owner phonenumber is "+str(verifyPhoneNumber))
        time.sleep(3)


    # @allure.description("Validating New Vehicle owner NIC")
    # @allure.severity(severity_level="Medium")
    def test_verify_nic(self):
        verifynic = driver.find_element_by_xpath("//td[contains(text(),'920012214V')]")
        assert  verifynic.text == '920012214V'
        print("New hevicle owner nic number is "+str(verifynic))



    # @allure.step("Entering username as {0}")
    # def enter_username(username):
    #     driver.find_element_by_id("email").send_keys(username)
    #
    # @allure.step("Entering password as {0}")
    # def enter_password(password):
    #     driver.find_element_by_id("password").send_keys(password)



    def test_tearDown(self):
        driver.quit()














