"""
Model Manager - Gerenciamento simples de modelos AI
ZERO complexidade, m	ilde;xima confiabilidade
"""

from typing import Optional, Dict, Any
import asyncio
import base64
from app.utils.logger import emoji_logger
from app.config import settings

# Import das bibliotecas REAIS de AI
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    emoji_logger.system_warning("google-generativeai n	ilde;o instalado")
    GEMINI_AVAILABLE = False

try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


# Classes wrapper para APIs REAIS
class Gemini:
    """Wrapper REAL para Gemini API"""
    def __init__(self, id, api_key):
        self.id = id
        self.api_key = api_key
        self.model = None

        if GEMINI_AVAILABLE:
            # Configurar Gemini REAL
            genai.configure(api_key=api_key)

            # Mapear nomes de modelo
            model_name = id
            if id == "gemini-2.5-pro":
                model_name = "gemini-1.5-pro"
            elif id == "gemini-2.0-flash-thinking":
                model_name = "gemini-1.5-flash"

            self.model = genai.GenerativeModel(model_name)

    async def achat(self, messages):
        """Chamada REAL para Gemini API com suporte multimodal, seguindo a documentação."""
        import google.generativeai as genai
        import base64
        from PIL import Image
        import io

        if not GEMINI_AVAILABLE or not self.model:
            return type('Response', (), {'content': 'Gemini não disponível. Configure GOOGLE_API_KEY.'})()

        try:
            # A API espera uma lista simples de conteúdos.
            # Vamos extrair o texto e a mídia da última mensagem do usuário.
            final_prompt_parts = []
            
            # Processa o histórico para extrair a última mensagem do usuário
            user_message = None
            for msg in reversed(messages):
                if msg['role'] == 'user':
                    user_message = msg
                    break
            
            if not user_message:
                 # Fallback se não houver mensagem do usuário (improvável)
                return type('Response', (), {'content': 'Nenhuma mensagem do usuário para processar.'})()

            content = user_message.get('content', '')
            if isinstance(content, list):
                # Mensagem multimodal
                for item in content:
                    if item.get("type") == "text":
                        final_prompt_parts.append(item.get("text", ""))
                    elif item.get("type") == "media":
                        media_data = item.get("media_data", {})
                        mime_type = media_data.get("mime_type")
                        base64_content = media_data.get("content")
                        if mime_type and base64_content:
                            try:
                                # A API do Gemini pode lidar com os bytes diretamente
                                image_bytes = base64.b64decode(base64_content)
                                final_prompt_parts.append(genai.types.Blob(
                                    mime_type=mime_type,
                                    data=image_bytes
                                ))
                            except Exception as e:
                                emoji_logger.system_warning(f"Não foi possível processar a mídia com mime_type {mime_type}: {e}")
                                final_prompt_parts.append(f"(Mídia do tipo {mime_type} recebida, mas não pôde ser processada)")

            elif isinstance(content, str):
                # Mensagem de texto simples
                final_prompt_parts.append(content)

            if not final_prompt_parts:
                return type('Response', (), {'content': 'Nenhum conteúdo válido para enviar ao modelo.'})()

            # O histórico de chat ainda não é totalmente suportado com imagens da mesma forma.
            # A abordagem mais segura é enviar a última instrução multimodal.
            response = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: self.model.generate_content(final_prompt_parts)
            )

            return type('Response', (), {'content': response.text})()

        except Exception as e:
            emoji_logger.system_error("Gemini", f"Erro na API: {e}")
            return type('Response', (), {'content': f'Erro Gemini: {str(e)}'})()


class OpenAI:
    """Wrapper REAL para OpenAI API"""
    def __init__(self, id, api_key):
        self.id = id
        self.api_key = api_key
        self.client = None

        if OPENAI_AVAILABLE and api_key:
            # Configurar OpenAI REAL
            self.client = openai.AsyncOpenAI(api_key=api_key)

    async def achat(self, messages):
        """Chamada REAL para OpenAI API"""
        if not OPENAI_AVAILABLE or not self.client:
            return type('Response', (), {
                'content': 'OpenAI n	ilde;o dispon	ilde;vel. Configure OPENAI_API_KEY.'
            })()

        try:
            # Fazer chamada REAL para OpenAI
            response = await self.client.chat.completions.create(
                model=self.id,
                messages=messages,
                temperature=0.7
            )

            return type('Response', (), {
                'content': response.choices[0].message.content
            })()

        except Exception as e:
            emoji_logger.system_error("OpenAI", f"Erro na API: {e}")
            return type('Response', (), {
                'content': f'Erro OpenAI: {str(e)}'
            })()


class ModelManager:
    """
    Gerenciador SIMPLES de modelos AI com fallback autom	ilde;tico
    Mant	ilde;m 100% da funcionalidade de forma modular
    """

    def __init__(self):
        self.primary_model = None
        self.fallback_model = None
        self.reasoning_model = None
        self.retry_count = 0
        self.max_retries = 5
        self.is_initialized = False

    def initialize(self):
        """Inicializa	ilde;	ilde;o SIMPLES dos modelos"""
        if self.is_initialized:
            return

        # Modelo prim	ilde;rio - Gemini
        try:
            if settings.primary_ai_model.startswith("gemini"):
                self.primary_model = Gemini(
                    id=settings.primary_ai_model,
                    api_key=settings.google_api_key
                )
                emoji_logger.system_ready(
                    "Modelo prim	ilde;rio Gemini configurado",
                    model=settings.primary_ai_model
                )
        except Exception as e:
            emoji_logger.system_warning(f"Erro ao configurar Gemini: {e}")

        # Modelo fallback - OpenAI
        try:
            if (settings.fallback_ai_model and
                    settings.fallback_ai_model.startswith("gpt")):
                self.fallback_model = OpenAI(
                    id=settings.fallback_ai_model,
                    api_key=settings.openai_api_key
                )
                emoji_logger.system_ready(
                    "Modelo fallback OpenAI o3-mini configurado"
                )
        except Exception as e:
            emoji_logger.system_warning(f"Erro ao configurar OpenAI: {e}")

        # Modelo reasoning - Gemini thinking
        try:
            if settings.agno_reasoning_enabled:
                self.reasoning_model = Gemini(
                    id="gemini-2.0-flash-thinking",
                    api_key=settings.google_api_key
                )
                emoji_logger.system_ready(
                    "Modelo reasoning configurado",
                    model="gemini-2.0-flash-thinking"
                )
        except Exception as e:
            emoji_logger.system_warning(f"Erro ao configurar reasoning: {e}")

        self.is_initialized = True
        emoji_logger.system_ready(
            "Sistema de modelos configurado",
            primary_model=settings.primary_ai_model,
            fallback_available=self.fallback_model is not None,
            reasoning_enabled=self.reasoning_model is not None
        )

    async def get_response(
            self,
            messages: list,
            system_prompt: Optional[str] = None,
            use_reasoning: bool = False,
            temperature: float = 0.7,
            max_tokens: int = 2000
    ) -> Optional[str]:
        """
        Obtém resposta REAL do modelo com fallback automático

        Args:
            messages: Lista de mensagens da conversa (incluindo a do usuário)
            system_prompt: Prompt do sistema (opcional, pode ser injetado)
            use_reasoning: Se deve usar modelo de reasoning
            temperature: Temperatura para geração
            max_tokens: Máximo de tokens

        Returns:
            Resposta REAL do modelo ou None se falhar
        """
        # Injeta o system_prompt no modelo Gemini, se aplicável
        model_to_use = self.primary_model
        if use_reasoning and self.reasoning_model:
            model_to_use = self.reasoning_model
        
        if isinstance(model_to_use, Gemini) and system_prompt:
            model_to_use.model.system_instruction = system_prompt

        if use_reasoning and self.reasoning_model:
            try:
                response = await self._try_model(
                    self.reasoning_model, messages, system_prompt
                )
                if response:
                    return response
            except Exception as e:
                emoji_logger.model_error(f"Erro no reasoning model: {e}")

        if self.primary_model:
            try:
                response = await self._try_model(
                    self.primary_model, messages, system_prompt
                )
                if response:
                    return response
            except Exception as e:
                emoji_logger.model_error(f"Erro no modelo primário: {e}")

        if self.fallback_model:
            try:
                response = await self._try_model(
                    self.fallback_model, messages, system_prompt
                )
                if response:
                    emoji_logger.model_warning("Usando modelo fallback")
                    return response
            except Exception as e:
                emoji_logger.model_error(f"Erro no modelo fallback: {e}")

        emoji_logger.service_error("Todos os modelos falharam")
        return None

    async def _try_model(
            self,
            model: Any,
            messages: list,
            system_prompt: Optional[str] = None
    ) -> Optional[str]:
        """
        Tenta obter resposta de um modelo específico

        Args:
            model: Modelo a usar
            messages: Lista de mensagens da conversa
            system_prompt: Prompt do sistema

        Returns:
            Resposta ou None se falhar
        """
        try:
            # Para modelos OpenAI, o system prompt é apenas outra mensagem
            if isinstance(model, OpenAI) and system_prompt:
                messages_with_system = [{"role": "system", "content": system_prompt}] + messages
            else:
                messages_with_system = messages

            response = await model.achat(messages_with_system)

            if response and response.content:
                return response.content

        except Exception as e:
            emoji_logger.model_error(f"Erro ao chamar modelo: {e}")

        return None

    async def retry_with_backoff(
            self,
            func,
            max_attempts: int = 3,
            initial_delay: float = 1.0
    ):
        """
        Retry com backoff exponencial SIMPLES

        Args:
            func: Fun	ilde;	ilde;o a executar
            max_attempts: M	ilde;ximo de tentativas
            initial_delay: Delay inicial em segundos

        Returns:
            Resultado da fun	ilde;	ilde;o ou None
        """
        delay = initial_delay

        for attempt in range(max_attempts):
            try:
                result = await func()
                if result:
                    return result
            except Exception as e:
                if attempt < max_attempts - 1:
                    emoji_logger.model_warning(
                        f"Tentativa {attempt + 1} falhou, "
                        f"aguardando {delay}s"
                    )
                    await asyncio.sleep(delay)
                    delay *= 2
                else:
                    emoji_logger.model_error(
                        f"Todas as tentativas falharam: {e}"
                    )

        return None

    def get_model_info(self) -> Dict[str, Any]:
        """Retorna informa	ilde;	ilde;es sobre os modelos configurados"""
        return {
            "primary": (
                settings.primary_ai_model if self.primary_model else None
            ),
            "fallback": (
                settings.fallback_ai_model if self.fallback_model else None
            ),
            "reasoning": (
                "gemini-2.0-flash-thinking" if self.reasoning_model else None
            ),
            "initialized": self.is_initialized
        }
