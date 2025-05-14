from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from utils.logger import Logger
from utils.retry import retry_on_exception
import allure

class BasePage:
    """
    BasePage provides reusable UI interaction methods for Web and Mobile with waits, logging, and retry.
    """

    def __init__(self, driver, timeout=10):
        """
        Initialize BasePage.

        Args:
            driver: Selenium or Appium driver.
            timeout (int): Default timeout for waiting on elements.
        """
        self.driver = driver
        self.timeout = timeout
        self.logger = Logger.get_logger()

    def wait_for_element(self, locator):
        """
        Wait until the element is visible.

        Args:
            locator (tuple): Locator tuple (By.ID, "value")

        Returns:
            WebElement: Found element.
        """
        try:
            self.logger.info(f"Waiting for element: {locator}")
            return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.error(f"Timeout waiting for element: {locator}")
            raise

    @retry_on_exception(retries=3, delay=1, exceptions=(NoSuchElementException, ElementClickInterceptedException))
    def click(self, locator):
        """
        Click an element with retry and logging.

        Args:
            locator (tuple): Locator tuple
        """
        element = self.wait_for_element(locator)
        self.logger.info(f"Clicking element: {locator}")
        allure.attach(body=f"Clicking: {locator}", name="Action", attachment_type=allure.attachment_type.TEXT)
        element.click()

    @retry_on_exception(retries=3, delay=1, exceptions=(NoSuchElementException,))
    def send_keys(self, locator, text):
        """
        Send text to an input field.

        Args:
            locator (tuple): Locator tuple
            text (str): Text to input
        """
        element = self.wait_for_element(locator)
        self.logger.info(f"Sending keys '{text}' to element: {locator}")
        allure.attach(body=f"Send keys: {text}", name="Action", attachment_type=allure.attachment_type.TEXT)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        Get text from an element.

        Args:
            locator (tuple): Locator tuple

        Returns:
            str: Text of element.
        """
        element = self.wait_for_element(locator)
        text = element.text
        self.logger.info(f"Text from {locator}: {text}")
        return text

    def is_displayed(self, locator):
        """
        Check if element is displayed.

        Args:
            locator (tuple): Locator tuple

        Returns:
            bool: True if displayed, False otherwise.
        """
        try:
            return self.driver.find_element(*locator).is_displayed()
        except Exception:
            return False
