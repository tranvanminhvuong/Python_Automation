import os
from dotenv import load_dotenv
from threading import Lock

class ConfigManager:
    """
    Singleton class to manage environment configurations loaded from .env file.
    """

    _instance = None
    _lock = Lock()

    def __init__(self):
        """
        Load environment variables from .env file and set configuration attributes.
        """
        load_dotenv()
        self.env = os.getenv("ENV", "dev")
        self.browser = os.getenv("BROWSER", "chrome")
        self.platform = os.getenv("PLATFORM", "web")
        self.device = os.getenv("DEVICE", "emulator-5554")

    @classmethod
    def get_instance(cls):
        """
        Get the singleton instance of ConfigManager.

        Returns:
            ConfigManager: The singleton instance.
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance
