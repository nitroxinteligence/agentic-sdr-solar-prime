"""
Gemini API Retry Logic - Tratamento robusto de erros 500
"""

import asyncio
import time
from typing import Any, Callable
from functools import wraps
import logging

logger = logging.getLogger(__name__)


class GeminiRetryHandler:
    """
    Handler para retry automático em caso de erros 500 do Gemini
    """

    def __init__(self, max_retries: int = 5, base_delay: float = 2.0):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.error_count = 0
        self.last_error_time = None

    async def execute_with_retry(
            self, func: Callable, *args, **kwargs
    ) -> Any:
        """
        Executa função com retry automático
        """
        last_exception = None
        for attempt in range(self.max_retries):
            try:
                if attempt > 0:
                    logger.info(f"Tentativa {attempt + 1}/{self.max_retries}")
                result = await func(*args, **kwargs)
                self.error_count = 0
                return result
            except Exception as e:
                last_exception = e
                error_str = str(e)
                if "500" in error_str or "INTERNAL" in error_str:
                    self.error_count += 1
                    self.last_error_time = time.time()
                    delay = self.base_delay * (2 ** attempt)
                    logger.warning(
                        f"Erro 500 (tentativa {attempt + 1}/{self.max_retries})"
                    )
                    logger.warning(f"Aguardando {delay}s...")
                    if attempt < self.max_retries - 1:
                        await asyncio.sleep(delay)
                    else:
                        logger.error(
                            f"Máximo de {self.max_retries} tentativas excedido"
                        )
                        raise
                else:
                    logger.error(f"Erro não recuperável: {error_str}")
                    raise
        if last_exception:
            raise last_exception
        else:
            raise Exception("Erro desconhecido após múltiplas tentativas")


def retry_on_500(max_retries: int = 5, base_delay: float = 2.0):
    """
    Decorator para adicionar retry automático em métodos
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            handler = GeminiRetryHandler(max_retries, base_delay)
            return await handler.execute_with_retry(func, *args, **kwargs)
        return wrapper
    return decorator


class GeminiCircuitBreaker:
    """
    Circuit Breaker para prevenir sobrecarga quando API está falhando
    """

    def __init__(self, failure_threshold: int = 3, timeout: int = 60):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.is_open = False

    def record_success(self):
        """Registra sucesso e reset contador"""
        self.failure_count = 0
        self.is_open = False

    def record_failure(self):
        """Registra falha e verifica se deve abrir circuito"""
        self.failure_count += 1
        self.last_failure_time = time.time()
        if self.failure_count >= self.failure_threshold:
            self.is_open = True
            logger.error(
                f"Circuit breaker ABERTO após {self.failure_count} falhas"
            )

    def can_attempt(self) -> bool:
        """Verifica se pode tentar chamada"""
        if not self.is_open:
            return True
        if (self.last_failure_time and
                (time.time() - self.last_failure_time) > self.timeout):
            logger.info("Circuit breaker: Timeout expirado, tentando reconectar")
            self.is_open = False
            self.failure_count = 0
            return True
        return False


gemini_retry_handler = GeminiRetryHandler()
gemini_circuit_breaker = GeminiCircuitBreaker()
