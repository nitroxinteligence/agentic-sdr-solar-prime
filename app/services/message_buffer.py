"""
Message Buffer Service - Simples e eficiente usando asyncio.Queue
"""
import asyncio
from typing import Dict, List, Optional
from loguru import logger
from app.utils.logger import emoji_logger


class MessageBuffer:
    """
    Buffer inteligente - processa imediatamente se agente está livre,
    só aguarda timeout se agente está ocupado processando
    """

    def __init__(self, timeout: float = 10.0, max_size: int = 10):
        """
        Inicializa o buffer
        """
        self.timeout = timeout
        self.max_size = max_size
        self.queues: Dict[str, asyncio.Queue] = {}
        self.tasks: Dict[str, asyncio.Task] = {}
        self.processing_locks: Dict[str, asyncio.Lock] = {}
        emoji_logger.system_info(
            f"Buffer Inteligente inicializado (timeout={timeout}s, max={max_size})"
        )

    async def add_message(
            self, phone: str, content: str, message_data: Dict, media_data: Optional[Dict] = None
    ) -> None:
        """
        Adiciona mensagem ao buffer
        """
        if phone not in self.queues:
            self.queues[phone] = asyncio.Queue(maxsize=self.max_size)
            self.tasks[phone] = asyncio.create_task(self._process_queue(phone))
        message = {"content": content, "data": message_data, "media_data": media_data}
        try:
            self.queues[phone].put_nowait(message)
            emoji_logger.system_debug(
                f"Mensagem adicionada ao buffer para {phone}"
            )
        except asyncio.QueueFull:
            emoji_logger.system_warning(f"Buffer para {phone} cheio. O processamento ocorrerá em breve.")

    async def _process_queue(self, phone: str) -> None:
        """
        Processa a fila de forma simplificada e robusta.
        """
        if phone not in self.processing_locks:
            self.processing_locks[phone] = asyncio.Lock()
        
        queue = self.queues.get(phone)
        if not queue:
            return

        try:
            async with self.processing_locks[phone]:
                messages = []
                try:
                    # Aguarda a primeira mensagem
                    first_msg = await asyncio.wait_for(queue.get(), timeout=self.timeout)
                    messages.append(first_msg)
                    
                    # Tenta coletar mais mensagens que chegaram em um curto espaço de tempo
                    while not queue.empty():
                        try:
                            msg = queue.get_nowait()
                            messages.append(msg)
                        except asyncio.QueueEmpty:
                            break
                
                except asyncio.TimeoutError:
                    # Se não houver mensagens após o timeout inicial, encerra a task.
                    return

                if messages:
                    await self._process_messages(phone, messages)

        except Exception as e:
            logger.error(f"Erro ao processar queue para {phone}: {e}")
        finally:
            # Limpa a task e a fila para este telefone
            self.tasks.pop(phone, None)
            self.queues.pop(phone, None)
            self.processing_locks.pop(phone, None)

    async def _process_messages(
            self, phone: str, messages: List[Dict]
    ) -> None:
        """
        Processa mensagens acumuladas de forma robusta.
        """
        from app.api.webhooks import process_message_with_agent

        # Filtro de segurança para remover quaisquer Nones que possam ter entrado na lista
        valid_messages = [m for m in messages if m is not None]
        if not valid_messages:
            emoji_logger.system_warning("Buffer processou um lote de mensagens vazio após a filtragem.", original_count=len(messages))
            return

        combined_content = "\n".join([msg["content"] for msg in valid_messages])
        emoji_logger.system_info(
            f"Processando {len(valid_messages)} mensagens combinadas",
            phone=phone, total_chars=len(combined_content)
        )
        
        last_message_obj = valid_messages[-1]
        last_message_data = last_message_obj.get("data")
        media_data = last_message_obj.get("media_data")

        # Verificação de segurança para garantir que a carga útil da última mensagem exista
        if last_message_data is None:
            emoji_logger.system_error(
                "O campo 'data' da última mensagem no buffer é None. Abortando processamento.",
                last_message_obj=last_message_obj
            )
            return

        message_id = last_message_data.get("key", {}).get("id", "")
        
        await process_message_with_agent(
            phone=phone,
            message_content=combined_content,
            original_message=last_message_data,
            message_id=message_id,
            media_data=media_data
        )

    async def shutdown(self) -> None:
        """Cancela todas as tasks ativas"""
        for task in self.tasks.values():
            task.cancel()
        if self.tasks:
            await asyncio.gather(*self.tasks.values(), return_exceptions=True)
        self.queues.clear()
        self.tasks.clear()


message_buffer: Optional[MessageBuffer] = None


def get_message_buffer() -> MessageBuffer:
    """Retorna instância global do buffer"""
    global message_buffer
    if not message_buffer:
        message_buffer = MessageBuffer()
    return message_buffer


def set_message_buffer(buffer: MessageBuffer) -> None:
    """Define instância global do buffer"""
    global message_buffer
    message_buffer = buffer
