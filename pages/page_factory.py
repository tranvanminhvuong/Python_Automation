from pages.web.login_page import LoginPage as WebLoginPage
from pages.mobile.home_page import HomePage as MobileHomePage

# 👉 Nếu sau này bạn có thêm MobileLoginPage, thì thêm vào như sau:
# from pages.mobile.login_page import LoginPage as MobileLoginPage

class PageFactory:
    """
    Factory class to instantiate Page Objects for Web and Mobile platforms.
    """

    def __init__(self, driver, platform="web", timeout=10):
        """
        Initialize PageFactory.

        Args:
            driver: WebDriver or AppiumDriver.
            platform (str): 'web', 'android', 'ios'
            timeout (int): Default timeout
        """
        self.driver = driver
        self.platform = platform.lower()
        self.timeout = timeout

    def get_login_page(self):
        """
        Get Login Page instance based on platform.

        Returns:
            Page Object instance
        """
        if self.platform == "web":
            return WebLoginPage(self.driver, self.timeout)
        # Nếu bạn có MobileLoginPage sau này
        # elif self.platform in ["android", "ios"]:
        #     return MobileLoginPage(self.driver, self.timeout)
        else:
            raise Exception(f"LoginPage not implemented for platform: {self.platform}")

    def get_mobile_home_page(self):
        """
        Get Mobile Home Page (used for Android/iOS).

        Returns:
            MobileHomePage instance
        """
        if self.platform in ["android", "ios"]:
            return MobileHomePage(self.driver, self.timeout)
        else:
            raise Exception("MobileHomePage is only available on mobile platforms")
