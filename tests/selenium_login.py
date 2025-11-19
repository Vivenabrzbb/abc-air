from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://abc-air.pythonanywhere.com/accounts/login/")
driver.find_element("id", "id_username").send_keys("admin")
driver.find_element("id", "id_password").send_keys("password")
driver.find_element("id", "login-btn").click()
time.sleep(2)
assert "Aircrafts" in driver.page_source
driver.quit()