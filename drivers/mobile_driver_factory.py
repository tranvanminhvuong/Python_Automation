from appium import webdriver

class MobileDriverFactory:
    """
    Factory class to create and return Appium WebDriver instances for mobile platforms.
    """

    @staticmethod
    def get_driver(platform_name: str, device_name: str, app_package: str, app_activity: str):
        """
        Initialize and return an Appium driver for Android or iOS.

        Args:
            platform_name (str): Mobile platform name (Android or iOS).
            device_name (str): Device name or ID.
            app_package (str): App package name (for Android).
            app_activity (str): App activity name (for Android).

        Returns:
            WebDriver: Appium WebDriver instance.
        """
        desired_caps = {
            "platformName": platform_name,
            "deviceName": device_name,
            "appPackage": app_package,
            "appActivity": app_activity,
            "automationName": "UiAutomator2" if platform_name.lower() == "android" else "XCUITest",
        }
        return webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
