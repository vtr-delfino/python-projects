from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys


fullName = "Teste"
email = "teste@gmail.com"
phone = "+00 00 0000 0000"
price = "150,00"


def fillForm_Demo():
    driver = webdriver.Firefox()
    driver.get("http://thedemosite.co.uk/")

    driver.implicitly_wait(5)

    driver.find_element(
        By.CSS_SELECTOR, "div.v-input:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)").send_keys(fullName)

    driver.find_element(
        By.CSS_SELECTOR, "div.v-input:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)").send_keys(email)

    driver.find_element(
        By.CSS_SELECTOR, "div.v-input:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)").send_keys(phone)

    driver.find_element(
        By.CSS_SELECTOR, "div.v-input:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(3)").send_keys(price)


fillForm_Demo(fullName)(fullName)
