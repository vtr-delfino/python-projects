from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys


def googleTest():
    driver = webdriver.Firefox()
    driver.get("https://google.com.br")

    title = driver.title
    assert title == "Google"

    driver.implicitly_wait(0.5)

    searchBox = driver.find_element(by=By.NAME, value="q")
    searchButton = driver.find_element(by=By.NAME, value="btnK")

    searchBox.send_keys("matchpoint real estate")
    # searchBox.send_keys(Keys.TAB)
    searchButton.location_once_scrolled_into_view
    searchButton.click()

    driver.quit()


googleTest()
