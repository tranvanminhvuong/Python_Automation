from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    """
    Page Object for the Login Page.
    """

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def login(self, username, password):
        """
        Perform login with provided credentials.
        """
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def load(self):
        """
        Load the login page.
        """
        self.driver.get("https://www.saucedemo.com")
