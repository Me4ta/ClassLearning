from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import string
import random

#generating random user name
generated_user_name = "test_user" + "".join(random.choice(string.digits) for i in range(12))
test_user_name = generated_user_name
test_user_email = generated_user_name + "@example.com"
test_user_password = "112233"

driver = webdriver.Chrome()
driver.get("https://secure.sigfig.com/auth/#/signup")

wait = WebDriverWait(driver, 10)
user_name_field = wait.until(EC.element_to_be_clickable((By.NAME, "username")))\
    .send_keys(test_user_name)

driver.find_element_by_name("password")\
    .send_keys(test_user_password)

driver.find_element_by_name("email")\
    .send_keys(test_user_email)

driver.find_element_by_name("agree").click()

driver.find_element_by_css_selector("button.submit-button").click()

try:
    wait = WebDriverWait(driver, 10)
    loggedin_user = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "username")))

    assert test_user_name in loggedin_user.text

    print("Test complete successfully")

finally:
    driver.quit()







