from drivers.web_driver_factory import WebDriverFactory
from config.config_manager import ConfigManager

config = ConfigManager.get_instance()
driver = WebDriverFactory.get_driver(config.browser)
driver.get("https://www.saucedemo.com")
print(driver.title)
driver.quit()
