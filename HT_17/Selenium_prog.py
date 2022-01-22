from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ParseSelenium(object):

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def parse():
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLScLhHgD5pMnwxl8JyRfXXsJekF8_pDG36XtSEwaGsFdU2egyw/viewform")
        input_form = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@class="quantumWizTextinputPaperinputInput exportInput"]')))
        # input_form = driver.find_element(By.CLASS_NAME, "quantumWizTextinputPaperinputInput exportInput")
        print(input_form)
        input_form.send_keys("Vlad")
        driver.save_screenshot("first.png")
        btn = driver.find_element(By.XPATH, '//span[text()="Отправить"]')
        btn.click()
        driver.save_screenshot("second.png")

if __name__ == '__main__':
    driver = webdriver.Chrome()
    parse = ParseSelenium(driver)
    ParseSelenium.parse()