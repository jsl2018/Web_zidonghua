from selenium import webdriver


def get_driver():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1/")
    return driver