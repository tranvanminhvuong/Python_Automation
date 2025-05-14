import time
from functools import wraps

def retry_on_exception(retries=3, delay=1, exceptions=(Exception,)):
    """
    Decorator to retry a function upon specific exceptions.

    Args:
        retries (int): Number of retries.
        delay (int): Delay between retries (in seconds).
        exceptions (tuple): Tuple of exceptions to catch.

    Returns:
        function: Decorated function with retry logic.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for _ in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    time.sleep(delay)
            raise last_exception
        return wrapper
    return decorator
