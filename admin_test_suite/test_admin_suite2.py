from selenium import webdriver
import time
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By



class TestExecution2():

    @pytest.mark.run(order=6)
    def test_setUp(self):
        global driver
        driver = webdriver.Chrome(executable_path="E:\\Automation\\Webdrivers\\chromedriver\\chromedriver.exe")
        driver.implicitly_wait(10)
        # driver.maximize_window()
        print("Maximized browser")


    @pytest.mark.run(order=7)
    def test_invalidlogin(self):
        driver.get("http://rentvehicles.multicompetition.com/")
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

    @pytest.mark.run(order=8)
    def test_vahiclePage_section(self):

        clickVehicleDropDown = driver.find_element(By.XPATH, "//p[contains(text(),'Vehicles')]")
        clickVehicleDropDown.click()
        time.sleep(2)

        clickVehicleOwner = driver.find_element_by_xpath("//p[contains(text(),'Vehicle Owners')]")
        clickVehicleOwner.click()
        time.sleep(2)


    @pytest.mark.run(order=9)
    def test_verify_ownerName(self):

        assert "vehicle-owners" in driver.current_url

        verifyVehicleOwnerText = driver.find_element(By.XPATH, "//h1[@class='m-0 text-dark']")
        assert verifyVehicleOwnerText.text == 'Vehicle Owners'

        clickVehicleDropDown = driver.find_element(By.XPATH, "//p[contains(text(),'Vehicles')]")
        clickVehicleDropDown.click()
        time.sleep(3)

        clickVehicleOwner = driver.find_element_by_xpath("//p[contains(text(),'Vehicle Owners')]")
        clickVehicleOwner.click()
        time.sleep(5)


        # Verify owner name : method 2
        verifyOwnerName = driver.find_element_by_xpath("//td[contains(text(),'milhan')]")
        assert verifyOwnerName.text == 'milhan'
        print("New vehicle owner name is "+str(verifyOwnerName))

    @pytest.mark.run(order=10)
    def test_phone_number(self):
        verifyPhoneNumber = driver.find_element_by_xpath("//td[contains(text(),'0528542756')]")
        assert verifyPhoneNumber.text == '0528542756'
        print("New vehicle owner phonenumber is "+str(verifyPhoneNumber))
        time.sleep(3)

    @pytest.mark.run(order=11)
    def test_verify_nic(self):
        verifynic = driver.find_element_by_xpath("//td[contains(text(),'920012214V')]")
        assert verifynic.text == '920012214V'
        print("New hevicle owner nic number is "+str(verifynic))


    def test_tearDown(self):
        driver.quit()














