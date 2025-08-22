"""
Context Analyzer - Análise SIMPLES de contexto e emoções
ZERO complexidade, funcionalidade total
"""
import re
from typing import Dict, Any, List
from app.utils.logger import emoji_logger
from app.config import settings


class ContextAnalyzer:
    """
    Analisador SIMPLES de contexto e estado emocional
    Mantém toda a inteligência de análise conversacional
    """

    def __init__(self):
        self.is_initialized = False
        self.context_enabled = settings.enable_context_analysis
        self.sentiment_enabled = settings.enable_sentiment_analysis
        self.emotional_enabled = settings.enable_emotional_triggers

    def initialize(self):
        """Inicialização simples"""
        if self.is_initialized:
            return

        emoji_logger.system_ready("🧠 ContextAnalyzer inicializado")
        self.is_initialized = True

    def analyze_context(self,
                        messages: List[Dict[str, Any]],
                        lead_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analisa contexto da conversa de forma SIMPLES

        Args:
            messages: Histórico de mensagens
            lead_info: Informações atuais do lead

        Returns:
            Análise completa do contexto
        """
        current_message = messages[-1]['content'] if messages else ""
        context = {
            "conversation_stage": self._determine_stage(messages, lead_info),
            "user_intent": self._extract_intent(current_message),
            "sentiment": self._analyze_sentiment(current_message),
            "emotional_state": self._analyze_emotional_state(messages),
            "key_topics": self._extract_topics(messages),
            "urgency_level": self._assess_urgency(current_message),
            "engagement_level": self._calculate_engagement(messages),
            "objections_raised": self._find_objections(messages),
            "questions_asked": self._extract_questions(messages),
            "action_needed": self._determine_action(current_message)
        }

        return context

    def _determine_stage(self, messages: List[Dict[str, Any]], lead_info: Dict[str, Any]) -> str:
        """
        Determina estágio da conversa baseado no conteúdo e no estado do lead

        Args:
            messages: Histórico
            lead_info: Informações do lead

        Returns:
            Estágio atual
        """
        has_name = bool(lead_info.get("name"))
        has_solutions_presented = False
        has_choice = False

        user_count = sum(1 for m in messages if m.get("role") == "user")
        assistant_count = sum(
            1 for m in messages if m.get("role") == "assistant"
        )
        emoji_logger.conversation_event(
            f"📊 Analisando estágio - Msgs: {len(messages)} "
            f"(👤 {user_count} user, 🤖 {assistant_count} assistant)"
        )

        # Se o nome ainda não foi coletado pelo lead_info, tenta extrair do histórico
        if not has_name:
            for msg in messages:
                content = msg.get("content", "").lower()
                role = msg.get("role", "")

                if role == "user":
                    # Verifica padrões explícitos de nome
                    if any(re.search(r'\b' + pattern + r'\b', content) for pattern in ["meu nome é", "me chamo", "sou o", "sou a"]):
                        has_name = True
                        break
                    # Verifica se a mensagem anterior foi uma pergunta sobre o nome
                    elif len(messages) > 1:
                        prev_msg_index = messages.index(msg) - 1
                        if prev_msg_index >= 0:
                            prev_msg = messages[prev_msg_index]
                            prev_content = prev_msg.get("content", "").lower()
                            # Padrões de pergunta sobre nome
                            name_questions = ["como posso te chamar", "qual seu nome", "como se chama"]
                            if prev_msg.get("role") == "assistant" and any(q in prev_content for q in name_questions):
                                # Se a resposta for curta (1-3 palavras), assume que é o nome
                                if 1 <= len(content.split()) <= 3:
                                    has_name = True
                                    break
        
        # Continua a análise do histórico para os outros estágios
        for msg in messages:
            content = msg.get("content", "").lower()
            role = msg.get("role", "")

            if role == "assistant" and all(
                sol in content for sol in [
                    "instalação", "aluguel", "compra", "investimento"
                ]
            ):
                has_solutions_presented = True

            if role == "user" and any(word in content for word in [
                "opção", "primeira", "segunda", "terceira", "quarta",
                "instalação", "aluguel", "compra", "investimento"
            ]):
                has_choice = True

        # Lógica de decisão de estágio
        if messages:
            last_message = messages[-1]
            if last_message.get("role") == "assistant":
                last_content = last_message.get("content", "").lower()
                if any(q in last_content for q in ["marcar uma reunião", "quando podemos marcar", "quando você estaria disponível"]):
                    return "agendamento"

        if not has_name:
            return "estágio_0_coleta_nome"
        elif has_name and not has_solutions_presented:
            return "estágio_1_apresentar_soluções"
        elif has_solutions_presented and not has_choice:
            return "estágio_2_aguardando_escolha"
        elif has_choice:
            return "qualificação"
        else:
            msg_count = len(messages)
            if msg_count <= 2:
                return "início"
            elif msg_count <= 10:
                return "exploração"
            else:
                return "negociação"

    def _extract_intent(self, message: str) -> str:
        """
        Extrai intenção principal da mensagem

        Args:
            message: Mensagem

        Returns:
            Intenção identificada
        """
        message_lower = message.lower()

        intents = {
            "informação": [
                "quanto", "como", "qual", "quando", "onde", "quem"
            ],
            "interesse": [
                "quero", "gostaria", "interessado", "me interessa"
            ],
            "dúvida": ["será", "não sei", "talvez", "dúvida"],
            "objeção": ["caro", "difícil", "problema", "não posso"],
            "agendamento": ["agendar", "marcar", "reunião", "conversar"],
            "compra": ["comprar", "adquirir", "fechar", "contratar"],
            "reclamação": ["ruim", "péssimo", "horrível", "insatisfeito"],
            "elogio": ["ótimo", "excelente", "muito bom", "adorei"]
        }

        for intent, keywords in intents.items():
            if any(keyword in message_lower for keyword in keywords):
                return intent

        return "conversa"

    def _analyze_sentiment(self, message: str) -> Dict[str, Any]:
        """
        Analisa sentimento da mensagem

        Args:
            message: Mensagem

        Returns:
            Análise de sentimento
        """
        if not self.sentiment_enabled:
            return {"enabled": False}

        message_lower = message.lower()

        positive_words = [
            "bom", "ótimo", "excelente", "legal", "maravilha",
            "perfeito", "adorei", "gostei", "sim", "quero"
        ]
        negative_words = [
            "ruim", "péssimo", "horrível", "não", "nunca",
            "problema", "difícil", "caro", "dúvida", "medo"
        ]

        positive_count = sum(
            1 for word in positive_words if word in message_lower
        )
        negative_count = sum(
            1 for word in negative_words if word in message_lower
        )

        if positive_count > negative_count:
            sentiment = "positivo"
            score = min(1.0, positive_count * 0.2)
        elif negative_count > positive_count:
            sentiment = "negativo"
            score = max(-1.0, -negative_count * 0.2)
        else:
            sentiment = "neutro"
            score = 0.0

        return {
            "enabled": True,
            "sentiment": sentiment,
            "score": score,
            "confidence": 0.7
        }

    def _analyze_emotional_state(
            self, messages: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Analisa estado emocional do usuário

        Args:
            messages: Histórico

        Returns:
            Estado emocional
        """
        if not self.emotional_enabled:
            return {"enabled": False}

        emotions = {
            "frustração": 0, "entusiasmo": 0, "hesitação": 0,
            "urgência": 0, "confiança": 0
        }

        recent_messages = messages[-5:]

        for msg in recent_messages:
            content = msg.get("content", "").lower()

            if any(word in content for word in [
                "demora", "difícil", "complicado"
            ]):
                emotions["frustração"] += 1

            if any(word in content for word in ["ótimo", "excelente", "adorei"]):
                emotions["entusiasmo"] += 1

            if any(word in content for word in ["não sei", "talvez", "pensar"]):
                emotions["hesitação"] += 1

            if any(word in content for word in ["urgente", "rápido", "agora"]):
                emotions["urgência"] += 1

            if any(word in content for word in ["confio", "acredito", "certeza"]):
                emotions["confiança"] += 1

        dominant_emotion = max(emotions.items(), key=lambda x: x[1])

        return {
            "enabled": True,
            "dominant": (
                dominant_emotion[0] if dominant_emotion[1] > 0 else "neutro"
            ),
            "scores": emotions,
            "intensity": min(1.0, dominant_emotion[1] * 0.3)
        }

    def _extract_topics(self, messages: List[Dict[str, Any]]) -> List[str]:
        """
        Extrai tópicos principais da conversa

        Args:
            messages: Histórico

        Returns:
            Lista de tópicos
        """
        topics = []
        topic_keywords = {
            "economia": ["economizar", "conta", "valor", "pagar"],
            "energia_solar": ["solar", "painel", "energia", "sol"],
            "investimento": ["investir", "retorno", "prazo", "custo"],
            "instalação": ["instalar", "obra", "telhado", "espaço"],
            "financiamento": ["financiar", "parcelar", "entrada", "prazo"],
            "manutenção": [
                "manutenção", "garantia", "durabilidade", "vida útil"
            ],
            "sustentabilidade": ["sustentável", "ambiente", "verde", "limpa"]
        }

        all_text = " ".join(
            [msg.get("content", "") for msg in messages]
        ).lower()

        for topic, keywords in topic_keywords.items():
            if any(keyword in all_text for keyword in keywords):
                topics.append(topic)

        return topics

    def _assess_urgency(self, message: str) -> str:
        """
        Avalia nível de urgência

        Args:
            message: Mensagem

        Returns:
            Nível de urgência
        """
        message_lower = message.lower()
        high_urgency = ["urgente", "agora", "hoje", "imediatamente", "rápido"]
        medium_urgency = ["amanhã", "semana", "breve", "logo"]
        low_urgency = ["futuro", "depois", "talvez", "pensando"]

        if any(word in message_lower for word in high_urgency):
            return "alta"
        elif any(word in message_lower for word in medium_urgency):
            return "média"
        elif any(word in message_lower for word in low_urgency):
            return "baixa"
        else:
            return "normal"

    def _calculate_engagement(self, messages: List[Dict[str, Any]]) -> float:
        """
        Calcula nível de engajamento

        Args:
            messages: Histórico

        Returns:
            Score de engajamento (0-1)
        """
        if len(messages) < 2:
            return 0.5

        factors = {
            "message_count": min(1.0, len(messages) / 20),
            "avg_length": 0,
            "questions": 0,
            "response_time": 0.5
        }

        avg_length = sum(
            len(msg.get("content", "")) for msg in messages
        ) / len(messages)
        factors["avg_length"] = min(1.0, avg_length / 100)

        question_count = sum(
            1 for msg in messages if "?" in msg.get("content", "")
        )
        factors["questions"] = min(1.0, question_count / 5)

        engagement = sum(factors.values()) / len(factors)
        return engagement

    def _find_objections(self, messages: List[Dict[str, Any]]) -> List[str]:
        """
        Encontra objeções mencionadas

        Args:
            messages: Histórico

        Returns:
            Lista de objeções
        """
        objections = []
        objection_patterns = {
            "preço": ["muito caro", "não tenho dinheiro", "fora do orçamento"],
            "desconfiança": ["não confio", "é golpe", "parece suspeito"],
            "timing": ["não é o momento", "depois eu vejo", "agora não"],
            "propriedade": ["casa alugada", "não sou dono", "inquilino"],
            "tecnologia": ["não entendo", "muito complicado", "difícil"]
        }

        all_text = " ".join(
            [msg.get("content", "") for msg in messages]
        ).lower()

        for objection, patterns in objection_patterns.items():
            if any(pattern in all_text for pattern in patterns):
                objections.append(objection)

        return objections

    def _extract_questions(self, messages: List[Dict[str, Any]]) -> List[str]:
        """
        Extrai perguntas feitas

        Args:
            messages: Histórico

        Returns:
            Lista de perguntas
        """
        questions = []
        for msg in messages:
            content = msg.get("content", "")
            if "?" in content:
                question = content.split("?")[0][-100:] + "?"
                questions.append(question.strip())
        return questions[-5:]

    def _determine_action(self, message: str) -> str:
        """
        Determina ação necessária

        Args:
            message: Mensagem

        Returns:
            Ação recomendada
        """
        message_lower = message.lower()
        actions = {
            "agendar": [
                "agendar", "marcar", "reunião", "conversar", "leonardo"
            ],
            "qualificar": ["conta", "valor", "gasto", "consumo", "kwh"],
            "informar": [
                "como funciona", "quanto custa", "dúvida", "explicar"
            ],
            "fechar": ["quero", "fechar", "contratar", "assinar"],
            "reengajar": ["pensar", "depois", "talvez", "não sei"]
        }

        for action, keywords in actions.items():
            if any(keyword in message_lower for keyword in keywords):
                return action

        return "conversar"

    def get_context_summary(self, context: Dict[str, Any]) -> str:
        """
        Gera resumo do contexto

        Args:
            context: Análise de contexto

        Returns:
            Resumo formatado
        """
        summary = "📊 **Análise de Contexto**\n\n"
        summary += f"🎯 Estágio: {context['conversation_stage']}\n"
        summary += f"💭 Intenção: {context['user_intent']}\n"

        if context['sentiment'].get('enabled'):
            summary += f"😊 Sentimento: {context['sentiment']['sentiment']}\n"

        if context['emotional_state'].get('enabled'):
            summary += f"❤️ Emoção: {context['emotional_state']['dominant']}\n"

        summary += f"⚡ Urgência: {context['urgency_level']}\n"
        summary += f"📈 Engajamento: {context['engagement_level']:.0%}\n"
        summary += f"🎬 Ação: {context['action_needed']}\n"

        if context['key_topics']:
            summary += f"\n📌 Tópicos: {', '.join(context['key_topics'])}\n"

        if context['objections_raised']:
            summary += f"⚠️ Objeções: {', '.join(context['objections_raised'])}\n"

        return summary
