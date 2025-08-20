"""
Centralized Error Handler for SDR IA SolarPrime System
Handles different types of exceptions with appropriate responses
"""

import traceback
import asyncio
from typing import Dict, Any, Optional
from app.exceptions import (
    BaseSDRException,
    KommoAPIException,
    GoogleCalendarException,
    NetworkException,
    DatabaseException,
    RateLimitException,
    AuthenticationException,
    ValidationException,
    HandoffException,
    ConversationException
)
from app.utils.logger import emoji_logger

class ErrorHandler:
    """Centralized error handler for the SDR IA SolarPrime system"""
    
    def __init__(self):
        self.retry_policies = {
            'network': {'max_retries': 3, 'delay': 5},
            'rate_limit': {'max_retries': 5, 'delay': 30},
            'kommo_api': {'max_retries': 3, 'delay': 10},
            'google_calendar': {'max_retries': 3, 'delay': 10}
        }
    
    async def handle_exception(self, exception: Exception, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Handle exception with appropriate response based on exception type
        
        Args:
            exception: The exception to handle
            context: Additional context information
            
        Returns:
            Dict with error handling result
        """
        context = context or {}
        
        try:
            # Handle specific exception types
            if isinstance(exception, KommoAPIException):
                return await self._handle_kommo_exception(exception, context)
            elif isinstance(exception, GoogleCalendarException):
                return await self._handle_google_calendar_exception(exception, context)
            elif isinstance(exception, NetworkException):
                return await self._handle_network_exception(exception, context)
            elif isinstance(exception, RateLimitException):
                return await self._handle_rate_limit_exception(exception, context)
            elif isinstance(exception, AuthenticationException):
                return await self._handle_authentication_exception(exception, context)
            elif isinstance(exception, DatabaseException):
                return await self._handle_database_exception(exception, context)
            elif isinstance(exception, ValidationException):
                return await self._handle_validation_exception(exception, context)
            elif isinstance(exception, HandoffException):
                return await self._handle_handoff_exception(exception, context)
            elif isinstance(exception, ConversationException):
                return await self._handle_conversation_exception(exception, context)
            elif isinstance(exception, BaseSDRException):
                return await self._handle_base_exception(exception, context)
            else:
                # Handle generic exceptions
                return await self._handle_generic_exception(exception, context)
                
        except Exception as handler_error:
            # If error handler itself fails, log and return generic response
            emoji_logger.system_error("ErrorHandler", f"Error handler failed: {handler_error}")
            return {
                "success": False,
                "error": "INTERNAL_ERROR",
                "message": "An unexpected error occurred",
                "details": {"original_error": str(exception)}
            }
    
    async def _handle_kommo_exception(self, exception: KommoAPIException, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle Kommo API exceptions"""
        error_details = exception.details or {}
        status_code = error_details.get('status_code', 0)
        
        emoji_logger.system_error("KommoAPI", f"Kommo API error: {exception.message}")
        
        # Specific handling based on status code
        if status_code == 401:
            return {
                "success": False,
                "error": "KOMMO_AUTH_ERROR",
                "message": "Authentication failed with Kommo API",
                "details": error_details,
                "requires_action": "reauthenticate"
            }
        elif status_code == 403:
            return {
                "success": False,
                "error": "KOMMO_PERMISSION_ERROR",
                "message": "Insufficient permissions for Kommo API operation",
                "details": error_details,
                "requires_action": "check_permissions"
            }
        elif status_code == 429:
            # Rate limited
            return await self._handle_rate_limit_exception(
                RateLimitException("Kommo API rate limit exceeded", details=error_details),
                context
            )
        elif status_code >= 500:
            # Server error - retry with exponential backoff
            return await self._retry_operation(context, 'kommo_api')
        else:
            return {
                "success": False,
                "error": "KOMMO_API_ERROR",
                "message": f"Kommo API error: {exception.message}",
                "details": error_details
            }
    
    async def _handle_google_calendar_exception(self, exception: GoogleCalendarException, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle Google Calendar API exceptions"""
        error_details = exception.details or {}
        status_code = error_details.get('status_code', 0)
        
        emoji_logger.system_error("GoogleCalendar", f"Google Calendar error: {exception.message}")
        
        # Specific handling based on status code
        if status_code == 401:
            return {
                "success": False,
                "error": "GOOGLE_AUTH_ERROR",
                "message": "Authentication failed with Google Calendar API",
                "details": error_details,
                "requires_action": "reauthenticate"
            }
        elif status_code == 403:
            return {
                "success": False,
                "error": "GOOGLE_PERMISSION_ERROR",
                "message": "Insufficient permissions for Google Calendar operation",
                "details": error_details,
                "requires_action": "check_permissions"
            }
        elif status_code == 409:
            return {
                "success": False,
                "error": "GOOGLE_CONFLICT_ERROR",
                "message": "Conflict detected in Google Calendar (double booking prevented)",
                "details": error_details,
                "requires_action": "resolve_conflict"
            }
        elif status_code == 429:
            # Rate limited
            return await self._handle_rate_limit_exception(
                RateLimitException("Google Calendar API rate limit exceeded", details=error_details),
                context
            )
        elif status_code >= 500:
            # Server error - retry with exponential backoff
            return await self._retry_operation(context, 'google_calendar')
        else:
            return {
                "success": False,
                "error": "GOOGLE_CALENDAR_ERROR",
                "message": f"Google Calendar error: {exception.message}",
                "details": error_details
            }
    
    async def _handle_network_exception(self, exception: NetworkException, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle network connectivity exceptions"""
        emoji_logger.system_error("Network", f"Network error: {exception.message}")
        
        # Retry with exponential backoff
        return await self._retry_operation(context, 'network')
    
    async def _handle_rate_limit_exception(self, exception: RateLimitException, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle rate limit exceptions"""
        error_details = exception.details or {}
        retry_after = error_details.get('retry_after', 60)  # Default to 60 seconds
        
        emoji_logger.system_warning("RateLimit", f"Rate limit exceeded, waiting {retry_after}s before retry")
        
        # Wait for rate limit to reset
        await asyncio.sleep(retry_after)
        
        # Retry with exponential backoff
        return await self._retry_operation(context, 'rate_limit')
    
    async def _handle_authentication_exception(self, exception: AuthenticationException, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle authentication exceptions"""
        emoji_logger.system_error("Auth", f"Authentication error: {exception.message}")
        
        return {
            "success": False,
            "error": "AUTHENTICATION_ERROR",
            "message": f"Authentication failed: {exception.message}",
            "details": exception.details or {},
            "requires_action": "reauthenticate"
        }
    
    async def _handle_database_exception(self, exception: DatabaseException, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle database exceptions"""
        emoji_logger.system_error("Database", f"Database error: {exception.message}")
        
        return {
            "success": False,
            "error": "DATABASE_ERROR",
            "message": f"Database operation failed: {exception.message}",
            "details": exception.details or {}
        }
    
    async def _handle_validation_exception(self, exception: ValidationException, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle data validation exceptions"""
        emoji_logger.system_error("Validation", f"Validation error: {exception.message}")
        
        return {
            "success": False,
            "error": "VALIDATION_ERROR",
            "message": f"Data validation failed: {exception.message}",
            "details": exception.details or {}
        }
    
    async def _handle_handoff_exception(self, exception: HandoffException, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle human handoff exceptions"""
        emoji_logger.system_error("Handoff", f"Handoff error: {exception.message}")
        
        return {
            "success": False,
            "error": "HANDOFF_ERROR",
            "message": f"Human handoff failed: {exception.message}",
            "details": exception.details or {}
        }
    
    async def _handle_conversation_exception(self, exception: ConversationException, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle conversation processing exceptions"""
        emoji_logger.system_error("Conversation", f"Conversation error: {exception.message}")
        
        return {
            "success": False,
            "error": "CONVERSATION_ERROR",
            "message": f"Conversation processing failed: {exception.message}",
            "details": exception.details or {}
        }
    
    async def _handle_base_exception(self, exception: BaseSDRException, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle base SDR exceptions"""
        emoji_logger.system_error("BaseException", f"Base SDR error: {exception.message}")
        
        return {
            "success": False,
            "error": exception.error_code or "SDR_ERROR",
            "message": exception.message,
            "details": exception.details or {}
        }
    
    async def _handle_generic_exception(self, exception: Exception, context: Dict[str, Any]) -> Dict[str, Any]:
        """Handle generic exceptions"""
        emoji_logger.system_error("Generic", f"Unexpected error: {str(exception)}")
        emoji_logger.system_error("Generic", f"Traceback: {traceback.format_exc()}")
        
        return {
            "success": False,
            "error": "UNEXPECTED_ERROR",
            "message": f"An unexpected error occurred: {str(exception)}",
            "details": {"exception_type": type(exception).__name__}
        }
    
    async def _retry_operation(self, context: Dict[str, Any], policy_name: str) -> Dict[str, Any]:
        """
        Retry operation with exponential backoff
        
        Args:
            context: Context containing operation details
            policy_name: Name of retry policy to use
            
        Returns:
            Dict with retry result
        """
        policy = self.retry_policies.get(policy_name, {'max_retries': 3, 'delay': 5})
        operation = context.get('operation')
        args = context.get('args', ())
        kwargs = context.get('kwargs', {})
        
        if not operation:
            return {
                "success": False,
                "error": "RETRY_FAILED",
                "message": "Cannot retry operation: no operation specified",
                "details": {"policy": policy_name}
            }
        
        last_exception = None
        
        for attempt in range(policy['max_retries']):
            try:
                # Calculate delay with exponential backoff
                delay = policy['delay'] * (2 ** attempt)
                
                emoji_logger.system_warning("Retry", f"Attempt {attempt + 1}/{policy['max_retries']} after {delay}s delay")
                
                # Wait before retry
                await asyncio.sleep(delay)
                
                # Execute operation
                if asyncio.iscoroutinefunction(operation):
                    result = await operation(*args, **kwargs)
                else:
                    result = operation(*args, **kwargs)
                
                # Success
                return {
                    "success": True,
                    "message": "Operation succeeded after retry",
                    "result": result,
                    "attempts": attempt + 1
                }
                
            except Exception as e:
                last_exception = e
                emoji_logger.system_error("Retry", f"Attempt {attempt + 1} failed: {str(e)}")
                continue
        
        # All retries failed
        return {
            "success": False,
            "error": "MAX_RETRIES_EXCEEDED",
            "message": f"Operation failed after {policy['max_retries']} attempts",
            "details": {
                "last_exception": str(last_exception),
                "policy": policy_name,
                "max_retries": policy['max_retries']
            }
        }

# Global error handler instance
error_handler = ErrorHandler()