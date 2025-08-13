"""
Message Splitter Service - Quebra mensagens preservando emojis e palavras
"""
try:
    import regex
    HAS_REGEX = True
except ImportError:
    import re as regex
    HAS_REGEX = False

# Importar NLTK para divisão inteligente por frases
try:
    from nltk.tokenize import sent_tokenize
    import nltk
    
    # Verificar se punkt está disponível
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        # Tentar baixar apenas punkt padrão
        try:
            nltk.download('punkt', quiet=True)
        except Exception:
            # Se não conseguir baixar, desabilitar NLTK
            raise ImportError("Não foi possível baixar dados punkt do NLTK")
    
    HAS_NLTK = True
except (ImportError, LookupError) as e:
    HAS_NLTK = False
    print(f"NLTK não disponível: {e}")
    
from typing import List, Optional
from app.utils.logger import emoji_logger

class MessageSplitter:
    """
    Splitter inteligente que preserva emojis, palavras e frases
    Usa regex module para suporte a grapheme clusters e NLTK para divisão por frases
    """
    
    def __init__(self, max_length: int = 200, add_indicators: bool = False, enable_smart_splitting: bool = True, smart_splitting_fallback: bool = True):
        """
        Inicializa o splitter
        
        Args:
            max_length: Tamanho máximo de cada chunk
            add_indicators: Se deve adicionar [1/3], [2/3] etc
            enable_smart_splitting: Se deve usar divisão inteligente por frases
            smart_splitting_fallback: Se deve fazer fallback para algoritmo atual quando NLTK falha
        """
        self.max_length = max_length
        self.add_indicators = add_indicators
        self.enable_smart_splitting = enable_smart_splitting
        self.smart_splitting_fallback = smart_splitting_fallback
        
        if not HAS_REGEX:
            emoji_logger.system_warning(
                "Módulo 'regex' não instalado. Usando 're' padrão (pode quebrar emojis)"
            )
        
        if self.enable_smart_splitting and not HAS_NLTK:
            emoji_logger.system_warning(
                "NLTK não disponível. Divisão inteligente desabilitada, usando algoritmo padrão"
            )
            self.enable_smart_splitting = False
        
        smart_status = "ativada" if self.enable_smart_splitting else "desativada"
        emoji_logger.system_info(f"Message Splitter inicializado (max={max_length} chars, smart={smart_status})")
    
    def split_message(self, text: str) -> List[str]:
        """
        Divide mensagem em chunks preservando palavras, emojis e frases
        
        Args:
            text: Texto para dividir
            
        Returns:
            Lista de chunks
        """
        if not text:
            return []
        
        # 🔥 VERIFICAR SE É A MENSAGEM DAS 4 SOLUÇÕES - NÃO DIVIDIR!
        if self._is_four_solutions_message(text):
            formatted_text = self._format_four_solutions_message(text)
            # Retornar como lista única, sem dividir
            return [formatted_text]
        
        # Se cabe, retorna direto
        if len(text) <= self.max_length:
            return [text.strip()]
        
        # Tentar divisão inteligente por frases primeiro
        if self.enable_smart_splitting and HAS_NLTK:
            try:
                chunks = self._split_by_sentences(text)
                emoji_logger.system_debug(
                    f"Mensagem dividida inteligentemente",
                    original_length=len(text),
                    chunks=len(chunks),
                    method="smart_splitting"
                )
                
                # Adiciona indicadores se configurado
                if self.add_indicators and len(chunks) > 1:
                    chunks = self._add_indicators(chunks)
                
                return chunks
            except Exception as e:
                emoji_logger.system_warning(
                    f"Divisão inteligente falhou: {e}. Usando algoritmo padrão"
                )
                if not self.smart_splitting_fallback:
                    raise
        
        # Fallback: Divide preservando emojis (algoritmo original)
        if HAS_REGEX:
            chunks = self._split_with_regex(text)
        else:
            chunks = self._split_simple(text)
        
        # Adiciona indicadores se configurado
        if self.add_indicators and len(chunks) > 1:
            chunks = self._add_indicators(chunks)
        
        emoji_logger.system_debug(
            f"Mensagem dividida",
            original_length=len(text),
            chunks=len(chunks),
            method="fallback_splitting"
        )
        
        return chunks
    
    def _split_by_sentences(self, text: str) -> List[str]:
        """
        Divide texto por frases usando NLTK para divisão inteligente
        
        Args:
            text: Texto para dividir
            
        Returns:
            Lista de chunks agrupando frases
        """
        try:
            # Tokenizar em frases usando NLTK
            sentences = sent_tokenize(text, language='portuguese')
            
            if not sentences:
                return [text.strip()]
            
            # Se só há uma frase mas é muito longa, forçar divisão
            if len(sentences) == 1 and len(sentences[0]) > self.max_length:
                return self._force_split_long_sentence(sentences[0])
            
            # Agrupar frases respeitando o limite de caracteres
            chunks = []
            current_chunk = ""
            
            for sentence in sentences:
                sentence = sentence.strip()
                if not sentence:
                    continue
                
                # Teste se a frase cabe no chunk atual
                test_chunk = current_chunk + (" " if current_chunk else "") + sentence
                
                if len(test_chunk) <= self.max_length:
                    # Cabe no chunk atual
                    current_chunk = test_chunk
                else:
                    # Não cabe, finalizar chunk atual e começar novo
                    if current_chunk:
                        chunks.append(current_chunk.strip())
                    
                    # Se a frase sozinha é muito longa, dividir ela
                    if len(sentence) > self.max_length:
                        chunks.extend(self._force_split_long_sentence(sentence))
                        current_chunk = ""
                    else:
                        current_chunk = sentence
            
            # Adicionar último chunk se houver
            if current_chunk:
                chunks.append(current_chunk.strip())
            
            return chunks if chunks else [text.strip()]
        
        except Exception as e:
            emoji_logger.system_warning(f"Erro na divisão por frases: {e}")
            raise
    
    def _force_split_long_sentence(self, sentence: str) -> List[str]:
        """
        Força divisão de frase muito longa usando algoritmo de fallback
        
        Args:
            sentence: Frase muito longa para dividir
            
        Returns:
            Lista de chunks da frase dividida
        """
        # Usar algoritmo atual para dividir frase longa
        if HAS_REGEX:
            return self._split_with_regex(sentence)
        else:
            return self._split_simple(sentence)
    
    def _split_with_regex(self, text: str) -> List[str]:
        """
        Divide usando regex module (preserva emojis)
        
        Args:
            text: Texto para dividir
            
        Returns:
            Lista de chunks
        """
        chunks = []
        
        # Extrai grapheme clusters (caracteres completos incluindo emojis)
        graphemes = regex.findall(r'\X', text)
        
        while graphemes:
            # Determina tamanho máximo do chunk
            chunk_size = min(self.max_length, len(graphemes))
            
            # Constrói chunk respeitando o limite de caracteres
            chunk_text = ""
            chunk_count = 0
            
            for i, grapheme in enumerate(graphemes[:chunk_size]):
                test_chunk = chunk_text + grapheme
                # Verifica se adicionar este grapheme excede o limite
                if len(test_chunk) > self.max_length:
                    break
                chunk_text = test_chunk
                chunk_count = i + 1
            
            # Se não é o último chunk e terminou no meio de palavra, volta até espaço
            if len(graphemes) > chunk_count and chunk_text:
                # Procura último espaço no chunk
                last_space = -1
                current_text = ""
                for i, grapheme in enumerate(graphemes[:chunk_count]):
                    current_text += grapheme
                    if grapheme.isspace():
                        last_space = i + 1
                
                # Se encontrou espaço, corta ali
                if last_space > 0:
                    chunk_text = ''.join(graphemes[:last_space]).rstrip()
                    chunk_count = last_space
            
            # Adiciona chunk se não vazio
            chunk_text = chunk_text.strip()
            if chunk_text:
                chunks.append(chunk_text)
            
            # Remove graphemes processados
            graphemes = graphemes[chunk_count:]
            # Pula espaços iniciais do próximo chunk
            while graphemes and graphemes[0].isspace():
                graphemes.pop(0)
        
        return chunks
    
    def _split_simple(self, text: str) -> List[str]:
        """
        Divide de forma simples (fallback sem regex module)
        
        Args:
            text: Texto para dividir
            
        Returns:
            Lista de chunks
        """
        chunks = []
        words = text.split()
        current_chunk = []
        current_length = 0
        
        for word in words:
            word_length = len(word)
            
            # Se a palavra sozinha é maior que o limite
            if word_length > self.max_length:
                # Salva chunk atual se houver
                if current_chunk:
                    chunks.append(' '.join(current_chunk))
                    current_chunk = []
                    current_length = 0
                
                # Quebra palavra grande (último recurso)
                while len(word) > self.max_length:
                    chunks.append(word[:self.max_length])
                    word = word[self.max_length:]
                
                if word:
                    current_chunk = [word]
                    current_length = len(word)
            
            # Se adicionar a palavra ultrapassa o limite
            elif current_length + word_length + 1 > self.max_length:
                # Salva chunk atual
                if current_chunk:
                    chunks.append(' '.join(current_chunk))
                
                # Começa novo chunk
                current_chunk = [word]
                current_length = word_length
            
            else:
                # Adiciona ao chunk atual
                current_chunk.append(word)
                current_length += word_length + 1  # +1 para o espaço
        
        # Adiciona último chunk
        if current_chunk:
            chunks.append(' '.join(current_chunk))
        
        return chunks
    
    def _add_indicators(self, chunks: List[str]) -> List[str]:
        """
        Adiciona indicadores [1/3], [2/3] etc
        
        Args:
            chunks: Lista de chunks
            
        Returns:
            Chunks com indicadores
        """
        total = len(chunks)
        result = []
        
        for i, chunk in enumerate(chunks, 1):
            indicator = f"[{i}/{total}] "
            
            # Se adicionar indicador ultrapassa limite, ajusta
            if len(indicator + chunk) > self.max_length:
                # Remove alguns caracteres do fim
                max_content = self.max_length - len(indicator) - 3
                chunk = chunk[:max_content] + "..."
            
            result.append(indicator + chunk)
        
        return result
    
    def _is_four_solutions_message(self, text: str) -> bool:
        """
        Detecta se é a mensagem especial das 4 soluções da SolarPrime
        
        Args:
            text: Texto para verificar
            
        Returns:
            True se for a mensagem das 4 soluções
        """
        # Indicadores chave da mensagem das 4 soluções
        indicators = [
            "hoje na solarprime",
            "quatro modelos de soluções",
            "instalação de usina própria",
            "aluguel de lote",
            "compra de energia com desconto",
            "usina de investimento"
        ]
        
        text_lower = text.lower()
        
        # Verificar se tem pelo menos 3 indicadores (para evitar falsos positivos)
        matches = sum(1 for indicator in indicators if indicator in text_lower)
        
        # Se tem pelo menos 3 indicadores E menciona as 4 opções, é a mensagem das soluções
        has_options = all(f"{i})" in text for i in range(1, 5))
        
        return matches >= 3 or (matches >= 2 and has_options)
    
    def _format_four_solutions_message(self, text: str) -> str:
        """
        Formata a mensagem das 4 soluções com quebras de linha adequadas
        
        Args:
            text: Texto original
            
        Returns:
            Texto formatado com quebras de linha
        """
        # Padrões para adicionar quebra de linha
        replacements = [
            # Quebra após a introdução
            ("quatro modelos de soluções energéticas:", "quatro modelos de soluções energéticas:\n"),
            ("quatro modelos de soluções:", "quatro modelos de soluções:\n"),
            # Quebra antes de cada opção numerada
            (" 1)", "\n1)"),
            (" 2)", "\n2)"),
            (" 3)", "\n3)"),  
            (" 4)", "\n4)"),
            # Quebra antes da pergunta final
            ("Qual desses modelos", "\n\nQual desses modelos"),
            ("Qual te interessa", "\n\nQual te interessa"),
        ]
        
        formatted_text = text
        for old, new in replacements:
            formatted_text = formatted_text.replace(old, new)
        
        # Limpar quebras duplas se houver
        while "\n\n\n" in formatted_text:
            formatted_text = formatted_text.replace("\n\n\n", "\n\n")
        
        # Garantir que não comece com quebra
        formatted_text = formatted_text.strip()
        
        emoji_logger.system_info(
            "📱 Mensagem das 4 soluções formatada com quebras de linha",
            original_length=len(text),
            formatted_length=len(formatted_text)
        )
        
        return formatted_text

# Instância global
message_splitter: Optional[MessageSplitter] = None

def get_message_splitter() -> MessageSplitter:
    """Retorna instância global do splitter"""
    global message_splitter
    if not message_splitter:
        message_splitter = MessageSplitter()
    return message_splitter

def set_message_splitter(splitter: MessageSplitter) -> None:
    """Define instância global do splitter"""
    global message_splitter
    message_splitter = splitter