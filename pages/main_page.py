from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver


class MainPage(BasePage):
    browser: object
    url: str

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")

