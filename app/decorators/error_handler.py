"""
Error Handler Decorator for Async Functions
Provides centralized exception handling with retry mechanisms
"""

import asyncio
import functools
from typing import Callable, Any, Dict, Optional
from app.handlers.error_handler import error_handler
from app.utils.logger import emoji_logger

def async_handle_errors(retry_policy: str = 'generic', max_retries: int = 3, delay: float = 1.0):
    """
    Decorator for handling exceptions in async functions with retry mechanism
    
    Args:
        retry_policy: Policy name for retry (see ErrorHandler.retry_policies)
        max_retries: Maximum number of retry attempts
        delay: Initial delay between retries (seconds)
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            # Prepare context for error handler
            context = {
                'operation': func,
                'args': args,
                'kwargs': kwargs,
                'function_name': func.__name__,
                'module': func.__module__
            }
            
            last_exception = None
            
            # Try original function
            for attempt in range(max_retries + 1):
                try:
                    # Execute the original function
                    result = await func(*args, **kwargs)
                    return result
                    
                except Exception as e:
                    last_exception = e
                    
                    # If this is the last attempt, don't retry
                    if attempt == max_retries:
                        break
                    
                    # Log retry attempt
                    emoji_logger.system_warning(
                        f"Retry Attempt {attempt + 1}/{max_retries + 1} for {func.__name__}: {str(e)}"
                    )
                    
                    # Calculate delay with exponential backoff
                    retry_delay = delay * (2 ** attempt)
                    
                    # Wait before retry
                    await asyncio.sleep(retry_delay)
            
            # If we get here, all retries failed
            # Use centralized error handler
            error_result = await error_handler.handle_exception(last_exception, context)
            
            # If error handler suggests retry, try one more time with its policy
            if error_result.get('retry_suggested'):
                retry_context = {
                    'operation': func,
                    'args': args,
                    'kwargs': kwargs,
                    'function_name': func.__name__,
                    'module': func.__module__
                }
                return await error_handler._retry_operation(retry_context, retry_policy)
            
            # Return error result if handler couldn't resolve it
            return error_result
            
        return wrapper
    return decorator

def async_handle_errors_with_fallback(fallback_func: Callable = None):
    """
    Decorator for handling exceptions in async functions with fallback mechanism
    
    Args:
        fallback_func: Function to call if original function fails
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            try:
                # Execute the original function
                return await func(*args, **kwargs)
                
            except Exception as e:
                # Log the error
                emoji_logger.system_error(
                    "ErrorHandler", 
                    f"Function {func.__name__} failed: {str(e)}"
                )
                
                # Try fallback function if provided
                if fallback_func:
                    try:
                        emoji_logger.system_warning(
                            "ErrorHandler", 
                            f"Using fallback for {func.__name__}"
                        )
                        return await fallback_func(*args, **kwargs)
                    except Exception as fallback_error:
                        emoji_logger.system_error(
                            "ErrorHandler", 
                            f"Fallback for {func.__name__} also failed: {str(fallback_error)}"
                        )
                        # Re-raise the original exception if fallback also fails
                        raise e
                
                # Re-raise if no fallback
                raise e
                
        return wrapper
    return decorator

# Specific decorators for common error types
def handle_kommo_errors(max_retries: int = 3, delay: float = 10.0):
    """Decorator specifically for handling Kommo API errors"""
    return async_handle_errors(retry_policy='kommo_api', max_retries=max_retries, delay=delay)

def handle_google_calendar_errors(max_retries: int = 3, delay: float = 10.0):
    """Decorator specifically for handling Google Calendar API errors"""
    return async_handle_errors(retry_policy='google_calendar', max_retries=max_retries, delay=delay)

def handle_network_errors(max_retries: int = 3, delay: float = 5.0):
    """Decorator specifically for handling network errors"""
    return async_handle_errors(retry_policy='network', max_retries=max_retries, delay=delay)

def handle_rate_limit_errors(max_retries: int = 5, delay: float = 30.0):
    """Decorator specifically for handling rate limit errors"""
    return async_handle_errors(retry_policy='rate_limit', max_retries=max_retries, delay=delay)