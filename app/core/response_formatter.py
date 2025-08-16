"""
Response Formatter - Garante formatação correta das respostas
Adiciona tags <RESPOSTA_FINAL> automaticamente quando necessário
"""

import re
from typing import Optional
from app.utils.logger import emoji_logger

class ResponseFormatter:
    """
    Formata e valida respostas do agente
    Garante que todas as respostas tenham tags <RESPOSTA_FINAL>
    """
    
    @staticmethod
    def ensure_response_tags(response: str) -> str:
        """
        Garante que a resposta tenha tags <RESPOSTA_FINAL>
        
        Args:
            response: Resposta do modelo
            
        Returns:
            Resposta com tags garantidas
        """
        if not response:
            return "<RESPOSTA_FINAL>Oi! Como posso ajudar você com energia solar? ☀️</RESPOSTA_FINAL>"
        
        # Verificar se já tem tags
        has_opening = "<RESPOSTA_FINAL>" in response
        has_closing = "</RESPOSTA_FINAL>" in response
        
        if has_opening and has_closing:
            # Tags já presentes - retornar como está
            emoji_logger.system_debug("✅ Tags já presentes na resposta")
            return response
        
        # Se tem alguma variação de RESPOSTA_FINAL, tentar corrigir
        if "RESPOSTA_FINAL" in response.upper():
            emoji_logger.system_warning("⚠️ Tags com formatação incorreta - corrigindo")
            
            # Tentar extrair conteúdo entre variações de tags
            patterns = [
                r'<RESPOSTA[_ ]?FINAL>(.*?)</RESPOSTA[_ ]?FINAL>',
                r'RESPOSTA[_ ]?FINAL[:\s]+(.*?)(?:\n\n|$)',
                r'\[RESPOSTA[_ ]?FINAL\](.*?)\[/RESPOSTA[_ ]?FINAL\]'
            ]
            
            for pattern in patterns:
                match = re.search(pattern, response, re.DOTALL | re.IGNORECASE)
                if match:
                    content = match.group(1).strip()
                    return f"<RESPOSTA_FINAL>{content}</RESPOSTA_FINAL>"
        
        # Se não tem tags, adicionar automaticamente
        emoji_logger.system_warning("🔧 Tags ausentes - adicionando automaticamente")
        
        # Limpar resposta de possível lixo
        clean_response = response.strip()
        
        # Remover possíveis tentativas de raciocínio
        # Se a resposta começa com algo como "Analisando..." ou "Vou..."
        reasoning_patterns = [
            r'^(Analisando|Vou|Deixa eu|Processando|Verificando).*?\n',
            r'^(Ok|Certo|Entendi|Hmm)[\.,!]?\s*\n',
            r'^\[.*?\]\s*\n'  # Remove qualquer coisa entre colchetes no início
        ]
        
        for pattern in reasoning_patterns:
            clean_response = re.sub(pattern, '', clean_response, flags=re.MULTILINE | re.IGNORECASE)
        
        # Se após limpar ficou vazio ou muito curto
        if not clean_response or len(clean_response) < 10:
            emoji_logger.system_error("ResponseFormatter", "Resposta vazia após limpeza - usando fallback")
            clean_response = "Oi! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime. Como posso te chamar?"
        
        # Adicionar tags
        formatted = f"<RESPOSTA_FINAL>{clean_response}</RESPOSTA_FINAL>"
        
        emoji_logger.system_success(f"✅ Resposta formatada com tags: {len(formatted)} chars")
        
        return formatted
    
    @staticmethod
    def validate_response_content(response: str) -> bool:
        """
        Valida se o conteúdo da resposta está adequado
        
        Args:
            response: Resposta a validar
            
        Returns:
            True se válida, False caso contrário
        """
        # Extrair conteúdo das tags
        match = re.search(r'<RESPOSTA_FINAL>(.*?)</RESPOSTA_FINAL>', response, re.DOTALL)
        
        if not match:
            return False
        
        content = match.group(1).strip()
        
        # Validações
        if not content:
            emoji_logger.system_error("ResponseFormatter", "Conteúdo vazio dentro das tags")
            return False
        
        if len(content) < 5:
            emoji_logger.system_error("ResponseFormatter", f"Conteúdo muito curto: {content}")
            return False
        
        # Verificar se não é só pontuação ou números
        if re.match(r'^[\s\d\W]+$', content):
            emoji_logger.system_error("ResponseFormatter", "Conteúdo sem texto válido")
            return False
        
        # Verificar palavras proibidas que indicam vazamento de raciocínio
        forbidden_phrases = [
            "vou analisar", "processando", "calculando",
            "verificando", "aguarde", "só um momento", "um minutinho"
        ]
        
        content_lower = content.lower()
        for phrase in forbidden_phrases:
            if phrase in content_lower:
                emoji_logger.system_warning(f"⚠️ Frase proibida detectada: {phrase}")
                return False
        
        return True
    
    @staticmethod
    def get_safe_fallback(context: str = "início") -> str:
        """
        Retorna uma resposta segura baseada no contexto
        
        Args:
            context: Contexto da conversa
            
        Returns:
            Resposta segura formatada
        """
        fallbacks = {
            "início": "Oi! Tudo bem? Me chamo Helen Vieira, sou consultora da Solarprime e irei realizar o seu atendimento. Antes de começarmos, como posso te chamar?",
            "nome_coletado": "Perfeito! Hoje na Solarprime temos 4 modelos de soluções energéticas. Qual valor você paga atualmente na sua conta de luz?",
            "valor_coletado": "Excelente! Com esse valor consigo uma economia muito interessante para você. Podemos agendar uma conversa rápida para eu te mostrar os números?",
            "default": "Como posso ajudar você com energia solar hoje? ☀️"
        }
        
        response = fallbacks.get(context, fallbacks["default"])
        return f"<RESPOSTA_FINAL>{response}</RESPOSTA_FINAL>"

# Instância global
response_formatter = ResponseFormatter()