from drivers.driver_factory import DriverFactory

def before_all(context):
    """
    Setup platform and driver before all tests.
    """
    context.platform = context.config.userdata.get("PLATFORM", "web").lower()
    context.driver = DriverFactory.get_driver(context.platform)
    context.driver.implicitly_wait(10)

def after_all(context):
    """
    Cleanup after all tests.
    """
    if context.driver:
        context.driver.quit()