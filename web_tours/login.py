from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(20)
print("maximized browser")


driver.get("http://localhost:1080/WebTours/")

driver.find_element(By.XPATH, '/html/body/form/table/tbody/tr[6]/td[2]/input').send_keys("fathih")
time.sleep(2)

driver.find_element(By.NAME, 'password').send_keys("1234")

# driver.find_element_by_css_selector("#btnLogin").is_enabled()
# print("Login button is enabled")
#
# driver.find_element_by_xpath("//a[@class='btn btn-link']").is_displayed()
# print("Forgot Password link is Displayed")
#
# enterLoginBtn = driver.find_element_by_id("btnLogin")
# enterLoginBtn.click()
# time.sleep(3)

