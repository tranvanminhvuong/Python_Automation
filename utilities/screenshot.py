import os
from datetime import datetime
from PIL import ImageGrab
import allure

def capture_screenshot(driver, name="screenshot"):
    """
    Capture and attach a screenshot to Allure report.

    Args:
        driver: Selenium WebDriver instance.
        name (str): Optional name for the screenshot.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{name}_{timestamp}.png"
    file_path = os.path.join("reports", "screenshots", file_name)

    # Ensure directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Capture and save
    driver.save_screenshot(file_path)

    # Attach to Allure report
    allure.attach.file(file_path, name=name, attachment_type=allure.attachment_type.PNG)
