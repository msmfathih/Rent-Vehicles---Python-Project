from selenium import webdriver
import time
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


class TestDrivers3():

    def setUp(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)


    @pytest.mark.run(order=7)
    def test_valid_login(self):
        driver.get("http://rentvehicles.multicompetition.com/login")
        enterEmail = driver.find_element(By.ID, 'email')
        enterEmail.send_keys("admin@gmail.com")
        time.sleep(2)

        enterPassword = driver.find_element(By.ID, 'password')
        enterPassword.send_keys("admin@123")

        enterLoginBtn = driver.find_element_by_id("btnLogin")
        enterLoginBtn.click()
        time.sleep(3)



