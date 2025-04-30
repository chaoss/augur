import time
import functools
import logging
from typing import Type, Union, Tuple, Optional
import httpx

logger = logging.getLogger(__name__)

class RetryableError(Exception):
    """Base class for errors that can be retried"""
    pass

class RateLimitError(RetryableError):
    """Raised when GitHub API rate limit is exceeded"""
    def __init__(self, reset_time: Optional[int] = None):
        self.reset_time = reset_time
        super().__init__(f"Rate limit exceeded. Reset at {reset_time}")

class AuthenticationError(Exception):
    """Raised when GitHub API authentication fails"""
    pass

def retry_on_exception(
    retries: int = 3,
    delay: float = 1.0,
    backoff: float = 2.0,
    exceptions: Union[Type[Exception], Tuple[Type[Exception], ...]] = RetryableError
):
    """
    Decorator that retries a function on specified exceptions
    
    Args:
        retries: Number of retries
        delay: Initial delay between retries in seconds
        backoff: Multiplier for delay after each retry
        exceptions: Exception types to retry on
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            current_delay = delay

            for attempt in range(retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    
                    if attempt == retries:
                        logger.error(f"Failed after {retries} retries: {str(e)}")
                        raise

                    if isinstance(e, RateLimitError) and e.reset_time:
                        wait_time = max(0, e.reset_time - time.time())
                        logger.warning(f"Rate limit exceeded, waiting {wait_time:.1f}s until reset")
                        time.sleep(wait_time)
                    else:
                        logger.warning(f"Attempt {attempt + 1}/{retries} failed: {str(e)}")
                        logger.warning(f"Retrying in {current_delay:.1f}s")
                        time.sleep(current_delay)
                        current_delay *= backoff

            raise last_exception
        return wrapper
    return decorator 