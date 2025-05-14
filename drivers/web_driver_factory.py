from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class WebDriverFactory:
    """
    Factory class to create and return WebDriver instances based on browser type.
    """

    @staticmethod
    def get_driver(browser_name: str):
        """
        Initialize and return a WebDriver instance for the specified browser.

        Args:
            browser_name (str): Name of the browser (chrome, firefox, edge).

        Returns:
            WebDriver: Selenium WebDriver instance.

        Raises:
            Exception: If the browser is not supported.
        """
        if browser_name.lower() == "chrome":
            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser_name.lower() == "firefox":
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif browser_name.lower() == "edge":
            return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        else:
            raise Exception(f"Unsupported browser: {browser_name}")
