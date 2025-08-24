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

    def _get_text_from_message(self, msg: Dict[str, Any]) -> str:
        """Helper para extrair texto de forma segura de uma mensagem."""
        content = msg.get("content", "")
        if isinstance(content, list):
            for part in content:
                if part.get("type") == "text":
                    return part.get("text", "")
            return ""
        return str(content)

    def analyze_context(self,
                        messages: List[Dict[str, Any]],
                        lead_info: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analisa contexto da conversa de forma SIMPLES
        """
        current_message_text = self._get_text_from_message(messages[-1]) if messages else ""
        
        context = {
            "conversation_stage": self._determine_stage(messages, lead_info),
            "user_intent": self._extract_intent(current_message_text),
            "sentiment": self._analyze_sentiment(current_message_text),
            "emotional_state": self._analyze_emotional_state(messages),
            "key_topics": self._extract_topics(messages),
            "urgency_level": self._assess_urgency(current_message_text),
            "engagement_level": self._calculate_engagement(messages),
            "objections_raised": self._find_objections(messages),
            "questions_asked": self._extract_questions(messages),
            "action_needed": self._determine_action(current_message_text)
        }
        return context

    def _determine_stage(self, messages: List[Dict[str, Any]], lead_info: Dict[str, Any]) -> str:
        """
        Determina o estágio da conversa com base nos dados consolidados do lead_info,
        tornando a lógica mais robusta e menos dependente de análise de texto.
        """
        # A fonte da verdade agora são os dados do lead, não o texto da conversa.
        has_name = bool(lead_info.get("name"))
        has_bill_value = bool(lead_info.get("bill_value"))
        has_chosen_flow = bool(lead_info.get("chosen_flow"))

        # Lógica de fluxo baseada em dados, muito mais confiável.
        if not has_name:
            return "estagio_0_coleta_nome"
        
        if not has_bill_value:
            return "estagio_1_qualificacao_por_valor"

        if not has_chosen_flow:
            return "estagio_2_roteamento_e_apresentacao"

        # Se todas as informações principais foram coletadas, estamos na fase de qualificação detalhada.
        # Uma verificação final de intenção de agendamento pode ser útil.
        last_message_text = self._get_text_from_message(messages[-1]) if messages else ""
        if any(keyword in last_message_text for keyword in ["agendar", "marcar", "reunião", "horário"]):
            return "agendamento"

        return "qualificacao_detalhada"

    def _extract_intent(self, message: str) -> str:
        message_lower = message.lower()
        intents = {
            "reagendamento": ["reagendar", "reagende", "remarcar", "mudar o horario", "outro horario"],
            "cancelamento": ["cancelar", "cancela", "nao vou poder", "cancele"],
            "informação": ["quanto", "como", "qual", "quando", "onde", "quem"],
            "interesse": ["quero", "gostaria", "interessado"], "dúvida": ["sera", "nao sei", "talvez"],
            "objeção": ["caro", "dificil", "problema"], "agendamento": ["agendar", "marcar", "reuniao", "reunião"],
            "compra": ["comprar", "adquirir", "fechar"], "reclamação": ["ruim", "pessimo", "horrivel"],
            "elogio": ["otimo", "excelente", "adorei"]
        }
        for intent, keywords in intents.items():
            if any(keyword in message_lower for keyword in keywords):
                return intent
        return "conversa"

    def _analyze_sentiment(self, message: str) -> Dict[str, Any]:
        if not self.sentiment_enabled: return {"enabled": False}
        message_lower = message.lower()
        pos_words = ["bom", "ótimo", "excelente", "legal", "perfeito", "adorei", "gostei", "sim", "quero"]
        neg_words = ["ruim", "péssimo", "horrível", "não", "nunca", "problema", "difícil", "caro"]
        pos_count = sum(1 for word in pos_words if word in message_lower)
        neg_count = sum(1 for word in neg_words if word in message_lower)
        if pos_count > neg_count: sentiment, score = "positivo", min(1.0, pos_count * 0.2)
        elif neg_count > pos_count: sentiment, score = "negativo", max(-1.0, -neg_count * 0.2)
        else: sentiment, score = "neutro", 0.0
        return {"enabled": True, "sentiment": sentiment, "score": score, "confidence": 0.7}

    def _analyze_emotional_state(self, messages: List[Dict[str, Any]]) -> Dict[str, Any]:
        if not self.emotional_enabled: return {"enabled": False}
        emotions = {"frustração": 0, "entusiasmo": 0, "hesitação": 0, "urgência": 0, "confiança": 0}
        for msg in messages[-5:]:
            content = self._get_text_from_message(msg).lower()
            if any(w in content for w in ["demora", "difícil"]): emotions["frustração"] += 1
            if any(w in content for w in ["ótimo", "excelente", "adorei"]): emotions["entusiasmo"] += 1
            if any(w in content for w in ["não sei", "talvez", "pensar"]): emotions["hesitação"] += 1
            if any(w in content for w in ["urgente", "rápido", "agora"]): emotions["urgência"] += 1
            if any(w in content for w in ["confio", "acredito", "certeza"]): emotions["confiança"] += 1
        
        dominant = "neutro"
        intensity = 0.0
        if any(emotions.values()):
            dominant_emotion_key = max(emotions, key=emotions.get)
            if emotions[dominant_emotion_key] > 0:
                dominant = dominant_emotion_key
                intensity = min(1.0, emotions[dominant] * 0.3)

        return {"enabled": True, "dominant": dominant, "scores": emotions, "intensity": intensity}

    def _extract_topics(self, messages: List[Dict[str, Any]]) -> List[str]:
        topics, keywords = [], {"economia": ["economizar", "conta", "valor"], "energia_solar": ["solar", "painel", "energia"], "investimento": ["investir", "retorno", "custo"], "instalação": ["instalar", "obra", "telhado"]}
        all_text = " ".join([self._get_text_from_message(msg) for msg in messages]).lower()
        for topic, keys in keywords.items():
            if any(key in all_text for key in keys):
                topics.append(topic)
        return topics

    def _assess_urgency(self, message: str) -> str:
        msg_lower = message.lower()
        if any(w in msg_lower for w in ["urgente", "agora", "hoje"]): return "alta"
        if any(w in msg_lower for w in ["amanhã", "semana", "breve"]): return "média"
        if any(w in msg_lower for w in ["futuro", "depois", "talvez"]): return "baixa"
        return "normal"

    def _calculate_engagement(self, messages: List[Dict[str, Any]]) -> float:
        if len(messages) < 2: return 0.5
        text_messages = [self._get_text_from_message(m) for m in messages]
        avg_len = sum(len(m) for m in text_messages) / len(messages)
        q_count = sum(1 for m in text_messages if "?" in m)
        factors = {"msg_count": min(1.0, len(messages) / 20), "avg_len": min(1.0, avg_len / 100), "questions": min(1.0, q_count / 5)}
        return sum(factors.values()) / len(factors)

    def _find_objections(self, messages: List[Dict[str, Any]]) -> List[str]:
        objections, patterns = [], {"preço": ["caro", "dinheiro"], "desconfiança": ["golpe", "não confio"], "timing": ["agora não", "depois"], "propriedade": ["aluguel", "não é meu"], "tecnologia": ["complicado", "difícil"]}
        all_text = " ".join([self._get_text_from_message(msg) for msg in messages]).lower()
        for obj, pats in patterns.items():
            if any(p in all_text for p in pats):
                objections.append(obj)
        return objections

    def _extract_questions(self, messages: List[Dict[str, Any]]) -> List[str]:
        questions = []
        for msg in messages:
            content = self._get_text_from_message(msg)
            if "?" in content:
                questions.append(content.strip())
        return questions[-5:]

    def _determine_action(self, message: str) -> str:
        msg_lower = message.lower()
        actions = {"agendar": ["agendar", "marcar", "reunião"], "qualificar": ["conta", "valor", "consumo"], "informar": ["como funciona", "quanto custa", "dúvida"], "fechar": ["quero", "fechar", "contratar"]}
        for action, keys in actions.items():
            if any(key in msg_lower for key in keys):
                return action
        return "conversar"
