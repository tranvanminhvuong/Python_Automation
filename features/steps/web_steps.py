from behave import given, when, then
from pages.web.login_page import LoginPage
from config.config_manager import ConfigManager
from drivers.web_driver_factory import WebDriverFactory
from selenium.webdriver.common.by import By
from utils.logger import Logger
from utils.screenshot import capture_screenshot

logger = Logger.get_logger()

@given("the user opens the SauceDemo website")
def step_open_website(context):
    """
    Step to initialize the driver and open the login page.
    """
    config = ConfigManager.get_instance()
    context.driver = WebDriverFactory.get_driver(config.browser)
    context.driver.maximize_window()
    context.login_page = LoginPage(context.driver)
    context.login_page.load()

@when('the user logs in with username "{username}" and password "{password}"')
def step_login(context, username, password):
    """
    Step to perform login on the login page.
    """
    context.login_page.login(username, password)

@then("the user should be redirected to the products page")
def step_verify_login_success(context):
    """
    Step to verify that the user is redirected to the products page.
    """
    try:
        assert "inventory.html" in context.driver.current_url
        product_title = context.driver.find_element(By.CLASS_NAME, "title").text
        assert "Products" in product_title
        logger.info("Login successful. User is on the products page.")
    except Exception as e:
        logger.error(f"Login failed: {str(e)}")
        capture_screenshot(context.driver, "login_failure")
        raise
    finally:
        context.driver.quit()