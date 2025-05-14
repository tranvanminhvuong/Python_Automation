import logging
from config.config_manager import ConfigManager

class Logger:
    """
    Singleton Logger utility class for consistent log formatting and usage.
    """
    _logger = None

    @staticmethod
    def get_logger(name="AUT"):
        """
        Create or return a singleton logger instance.

        Args:
            name (str): Name of the logger.

        Returns:
            Logger: Configured logger instance.
        """
        if Logger._logger:
            return Logger._logger

        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')

        # Console handler
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)

        Logger._logger = logger
        return logger
