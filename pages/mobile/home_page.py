from pages.mobile.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class HomePage(BasePage):
    """
    Mobile Home Page (YouTube App)
    """

    SEARCH_BUTTON = (AppiumBy.ID, "com.google.android.youtube:id/menu_search")
    ACCOUNT_ICON = (AppiumBy.ID, "com.google.android.youtube:id/avatar")

    def open_search(self):
        """
        Tap on the search icon.
        """
        self.click(self.SEARCH_BUTTON)

    def is_logged_in(self):
        """
        Check if the account icon is visible.
        """
        return self.is_displayed(self.ACCOUNT_ICON)
