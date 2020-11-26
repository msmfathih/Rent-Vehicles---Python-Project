from selenium import webdriver
import time
import pytest
import allure
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains


class TestDrivers():
    def test_setUp(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)


    def test_invalid_login(self):
        driver.get("https://admin-demo.nopcommerce.com/")

        try:
            assert "Your store. Login" in driver.title
            print("Assertion Test Pass")
        except Exception as e:
            print("Assertion test failed", format(e))

        assert "nopcommerce" in driver.current_url

        enterEmail = driver.find_element(By.ID, 'Email').clear()
        enterEmail = driver.find_element(By.ID, 'Email')
        enterEmail.send_keys("admin@yourstore123.com")
        time.sleep(3)

        enterPassword = driver.find_element(By.ID, 'Password').clear()
        enterPassword = driver.find_element(By.ID, 'Password')
        enterPassword.send_keys("admin123")

        pressLogin = driver.find_element(By.XPATH, "//input[@class='button-1 login-button']").click()

        # verifyWrongEmailErrorMessage = driver.find_element(By.XPATH,
        #                                                    "//li[contains(text(),'The credentials provided are incorrect')]")
        # assert verifyWrongEmailErrorMessage.text == "The credentials provided are incorrect"


        driver.refresh()

    def test_valid_login(self):
        enterEmail = driver.find_element(By.ID, 'Email').clear()
        enterEmail = driver.find_element(By.ID, 'Email')
        enterEmail.send_keys("admin@yourstore.com")
        time.sleep(3)

        enterPassword = driver.find_element(By.ID, 'Password').clear()
        enterPassword = driver.find_element(By.ID, 'Password')
        enterPassword.send_keys("admin")

        pressLogin = driver.find_element(By.XPATH, "//input[@class='button-1 login-button']").click()


    def test_select_dropdown_menu(self):
        selectCustomer_Dropdown = driver.find_element(By.XPATH, "//a[@href='#']//span[contains(text(),'Customers')]").click()
        time.sleep(3)
        select_sub_customer_option = driver.find_element(By.XPATH, "//span[@class='menu-item-title'][contains(text(),'Customers')]").click()

    def test_add_new_customer(self):
        addnew_customer = driver.find_element(By.XPATH, "//a[@class='btn bg-blue']").click()
        enter_email = driver.find_element(By.ID, 'Email').send_keys("fathih@gmail.com")
        enter_password = driver.find_element(By.ID, 'Password').send_keys("abc123")
        enter_firstname = driver.find_element(By.ID, "FirstName").send_keys("aadil")
        enter_lastname = driver.find_element(By.ID, "LastName").send_keys("ahamed")
        select_gender = driver.find_element(By.XPATH, "//div[@class='col-md-1']//label[1]").click()
        date_of_birth = driver.find_element(By.ID, "DateOfBirth").send_keys("8/11/1992")
        company_name = driver.find_element(By.ID, "Company").send_keys("ABC Pvt Ltd")
        tax_exampt = driver.find_element(By.ID, "IsTaxExempt").click()

        driver.find_element(By.CSS_SELECTOR, 'k-widget k-multiselect')
        drop_list = driver.find_elements(By.CSS_SELECTOR, 'k-multiselect-wrap')

        value_list = ['Administrators', 'Guests']
        select_values(drop_list, value_list)


    #
    # def test_tearDown(self):
    #     driver.quit()

