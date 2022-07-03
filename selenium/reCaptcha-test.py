from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.google.com/recaptcha/api2/demo")

driver.implicitly_wait(1)

WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "/html/body/div[1]/form/fieldset/ul/li[5]/div/div/div/div/iframe")))
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".recaptcha-checkbox-border"))).click()
