"""
Lead Manager - Gerenciamento SIMPLES de leads
ZERO complexidade, funcionalidade total
"""

from typing import Dict, Any, Optional, List
import re
from app.utils.logger import emoji_logger
from app.config import settings


class LeadManager:
    """
    Gerenciador de SIMPLES leads e qualificação
    Mantém toda a lógica de extração e scoring
    """

    def __init__(self):
        self.is_initialized = False
        self.scoring_enabled = settings.enable_lead_scoring

    def initialize(self):
        """Inicialização simples"""
        if self.is_initialized:
            return

        emoji_logger.system_ready("📊 LeadManager inicializado")
        self.is_initialized = True

    def extract_lead_info(
            self,
            messages: List[Dict[str, Any]],
            existing_lead_info: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Extrai informações do lead de forma SIMPLES
        """
        if existing_lead_info:
            import copy
            lead_info = copy.deepcopy(existing_lead_info)
        else:
            lead_info = {
                "name": None,
                "phone_number": None,
                "email": None,
                "bill_value": None,
                "qualification_score": 0,
                "current_stage": "INITIAL_CONTACT",
                "chosen_flow": None,
                "preferences": {}
            }

        # Garante que a estrutura de 'preferences' e suas chaves existam
        if "preferences" not in lead_info or not isinstance(lead_info.get("preferences"), dict):
            lead_info["preferences"] = {}
        if "interests" not in lead_info["preferences"]:
            lead_info["preferences"]["interests"] = []
        if "objections" not in lead_info["preferences"]:
            lead_info["preferences"]["objections"] = []

        processed_message_count = lead_info.get("processed_message_count", 0)
        new_messages = messages[processed_message_count:]

        if not new_messages:
            return lead_info

        for msg in new_messages:
            content_data = msg.get("content", "")
            
            text_content = ""
            if isinstance(content_data, list):
                for part in content_data:
                    if part.get("type") == "text":
                        text_content = part.get("text", "")
                        break
            elif isinstance(content_data, str):
                text_content = content_data

            content_lower = text_content.lower()
            role = msg.get("role", "")

            if role == "user":
                if not lead_info.get("name"):
                    name = self._extract_name(content_lower)
                    if name:
                        lead_info["name"] = name
                    else:
                        words = content_lower.split()
                        if 1 <= len(words) <= 4:
                            blacklist = [
                                "oi", "olá", "ola", "sim", "não", "nao",
                                "ok", "tudo", "bom", "dia", "tarde",
                                "noite", "boa", "legal", "bem", "quero",
                                "gostaria", "preciso", "pode", "poderia",
                                "claro", "certeza", "beleza", "blz",
                                "tbm", "também", "tá", "ta", "está",
                                "estou", "to", "já", "tenho", "como",
                                "funciona", "quanto", "vou", "pago",
                                "minha", "conta", "desconto", "economia",
                                "origo", "setta", "solar", "energia", "luz"
                            ]
                            potential_name = " ".join(
                                word for word in words if word.lower() not in blacklist
                            )
                            if potential_name and self._is_valid_name(potential_name):
                                lead_info["name"] = potential_name.title()

                if not lead_info.get("email"):
                    email = self._extract_email(content_lower)
                    if email:
                        lead_info["email"] = email

                if not lead_info.get("bill_value"):
                    value = self._extract_bill_value(content_lower)
                    if value:
                        lead_info["bill_value"] = value

                if not lead_info.get("preferences", {}).get("property_type"):
                    prop_type = self._extract_property_type(content_lower)
                    if prop_type:
                        lead_info["preferences"]["property_type"] = prop_type

                if not lead_info.get("preferences", {}).get("location"):
                    location = self._extract_location(content_lower)
                    if location:
                        lead_info["preferences"]["location"] = location

            interests = self._extract_interests(content_lower)
            if interests:
                lead_info["preferences"]["interests"].extend(interests)

            objections = self._extract_objections(content_lower)
            if objections:
                lead_info["preferences"]["objections"].extend(objections)

            if not lead_info.get("chosen_flow"):
                chosen_flow = self._extract_chosen_flow(content_lower)
                if chosen_flow:
                    lead_info["chosen_flow"] = chosen_flow

        lead_info["processed_message_count"] = len(messages)

        lead_info["preferences"]["interests"] = list(
            set(lead_info["preferences"]["interests"])
        )
        lead_info["preferences"]["objections"] = list(
            set(lead_info["preferences"]["objections"])
        )

        if self.scoring_enabled:
            lead_info["qualification_score"] = (
                self.calculate_qualification_score(lead_info)
            )
            lead_info["current_stage"] = self.determine_stage(lead_info)

        return lead_info

    def calculate_qualification_score(
            self,
            lead_info: Dict[str, Any],
    ) -> int:
        """Calcula score de qualificação SIMPLES"""
        score = 0.0
        bill_value = lead_info.get("bill_value", 0)
        if bill_value:
            if bill_value >= 1000:
                score += 40
            elif bill_value >= 700:
                score += 30
            elif bill_value >= 500:
                score += 20
            elif bill_value >= 300:
                score += 10

        if lead_info.get("name"):
            score += 10
        if lead_info.get("phone_number"):
            score += 10
        if lead_info.get("email"):
            score += 5
        if lead_info.get("preferences", {}).get("location"):
            score += 5

        property_type = lead_info.get(
            "preferences", {}
        ).get("property_type")
        if property_type:
            if "comercial" in property_type or "empresa" in property_type:
                score += 15
            elif "residencial" in property_type or "casa" in property_type:
                score += 10

        interests = lead_info.get("preferences", {}).get("interests", [])
        if len(interests) >= 3:
            score += 10
        elif len(interests) >= 2:
            score += 7
        elif len(interests) >= 1:
            score += 5

        objections = lead_info.get("preferences", {}).get("objections", [])
        if len(objections) >= 3:
            score -= 5
        elif len(objections) >= 2:
            score -= 3

        return int(max(0, min(100, score)))

    def determine_stage(self, lead_info: Dict[str, Any]) -> str:
        """Determina estágio do lead no funil"""
        score = lead_info.get("qualification_score", 0)
        if score >= 80:
            return "HOT"
        elif score >= 60:
            return "WARM"
        elif score >= 40:
            return "QUALIFYING"
        elif score >= 20:
            return "INTERESTED"
        else:
            return "INITIAL_CONTACT"

    def _extract_name(self, text: str) -> Optional[str]:
        """Extrai nome do texto com foco em padrões explícitos."""
        patterns = [
            r"meu\s+nome\s+[eé]\s+([A-Za-zÀ-ÿ]+(?:\s+[A-Za-zÀ-ÿ]+){0,3})",
            r"me\s+chamo\s+([A-Za-zÀ-ÿ]+(?:\s+[A-Za-zÀ-ÿ]+){0,3})",
            r"pode\s+me\s+chamar\s+de\s+([A-Za-zÀ-ÿ]+(?:\s+[A-Za-zÀ-ÿ]+){0,3})",
            r"(?:eu\s+)?sou\s+o\s+([A-Za-zÀ-ÿ]+(?:\s+[A-Za-zÀ-ÿ]+){0,3})",
            r"(?:eu\s+)?sou\s+a\s+([A-Za-zÀ-ÿ]+(?:\s+[A-Za-zÀ-ÿ]+){0,3})",
        ]
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                potential_name = match.group(1).strip().title()
                if self._is_valid_name(potential_name):
                    return potential_name
        return None

    def _is_valid_name(self, name: str) -> bool:
        """Valida se uma string é um nome próprio provável."""
        if not name or len(name) < 3 or len(name) > 60:
            return False
        words = name.split()
        if len(words) > 4:
            return False
        blacklist = [
            'a', 'o', 'e', 'de', 'do', 'da', 'dos', 'das', 'com', 'em',
            'para', 'por', 'oi', 'ola', 'sim', 'nao', 'ok', 'tudo', 'bem',
            'bom', 'dia', 'tarde', 'noite', 'quero', 'gostaria', 'preciso',
            'pode', 'claro', 'conta', 'valor', 'energia'
        ]
        for word in words:
            word_lower = word.lower()
            if word_lower in blacklist or not word.isalpha() or len(word) < 2:
                return False
        return True

    def _extract_email(self, text: str) -> Optional[str]:
        """Extrai email do texto"""
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        match = re.search(email_pattern, text)
        return match.group(0).lower() if match else None

    def _extract_bill_value(self, text: str) -> Optional[float]:
        """Extrai valor da conta do texto"""
        patterns = [
            r"conta.{0,20}R?\s*\$?\s*(\d+(?:[.,]\d{0,2})?)",
            r"pago.{0,20}R?\s*\$?\s*(\d+(?:[.,]\d{0,2})?)",
            r"valor.{0,20}R?\s*\$?\s*(\d+(?:[.,]\d{0,2})?)",
            r"(\d+(?:[.,]\d{0,2})?)\s*reais",
            r"uns\s*(\d+(?:[.,]\d{0,2})?)",
            r"R?\s*\$?\s*(\d+(?:[.,]\d{0,2})?)"
        ]
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                try:
                    values = [float(m.replace(",", ".")) for m in matches]
                    reasonable_values = [v for v in values if 50 <= v <= 10000]
                    if reasonable_values:
                        return max(reasonable_values)
                except Exception:
                    pass
        return None

    def _extract_property_type(self, text: str) -> Optional[str]:
        """Extrai tipo de imóvel"""
        types = {
            "casa": ["casa", "residência", "moradia"],
            "apartamento": ["apartamento", "apto", "ap"],
            "comercial": ["empresa", "comércio", "loja", "escritório"],
            "rural": ["fazenda", "sítio", "chácara", "rural"]
        }
        for prop_type, keywords in types.items():
            if any(keyword in text for keyword in keywords):
                return prop_type
        return None

    def _extract_location(self, text: str) -> Optional[str]:
        """Extrai localização"""
        patterns = [
            r"moro em ([A-Za-z\s]+)", r"sou de ([A-Za-z\s]+)",
            r"estou em ([A-Za-z\s]+)", r"cidade de ([A-Za-z\s]+)"
        ]
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip().title()
        return None

    def _extract_interests(self, text: str) -> List[str]:
        """Extrai interesses demonstrados"""
        interests = []
        interest_keywords = {
            "economia": ["economizar", "economia", "reduzir conta"],
            "sustentabilidade": ["sustentável", "meio ambiente", "verde"],
            "investimento": ["investimento", "retorno", "valorização"],
            "independência": ["independência", "própria energia"],
            "tecnologia": ["tecnologia", "inovação", "moderno"]
        }
        for interest, keywords in interest_keywords.items():
            if any(keyword in text for keyword in keywords):
                interests.append(interest)
        return interests

    def _extract_objections(self, text: str) -> List[str]:
        """Extrai objeções mencionadas"""
        objections = []
        objection_keywords = {
            "preço": ["caro", "muito dinheiro", "não tenho"],
            "desconfiança": ["golpe", "enganação", "não confio"],
            "tempo": ["não é hora", "depois", "mais tarde"],
            "propriedade": ["aluguel", "não é meu", "alugado"],
            "dúvidas": ["não entendo", "complicado", "difícil"]
        }
        for objection, keywords in objection_keywords.items():
            if any(keyword in text for keyword in keywords):
                objections.append(objection)
        return objections

    def _extract_chosen_flow(self, text: str) -> Optional[str]:
        """Extrai escolha de fluxo do usuário"""
        text_lower = text.lower().strip()
        flow_mapping = {
            "compra de energia com desconto": "Compra com Desconto",
            "instalação de usina própria": "Instalação Usina Própria",
            "aluguel de lote": "Aluguel de Lote",
            "usina de investimento": "Usina Investimento",
            "opção 1": "Instalação Usina Própria",
            "opção 2": "Aluguel de Lote",
            "opção 3": "Compra com Desconto",
            "opção 4": "Usina Investimento"
        }
        sorted_keys = sorted(flow_mapping.keys(), key=len, reverse=True)
        for key in sorted_keys:
            if key in text_lower:
                return flow_mapping[key]
        return None

    def format_lead_summary(self, lead_info: Dict[str, Any]) -> str:
        """Formata resumo do lead para exibição"""
        summary = "📊 **Resumo do Lead**\n\n"
        if lead_info.get("name"):
            summary += f"👤 Nome: {lead_info['name']}\n"
        if lead_info.get("phone"):
            summary += f"📱 Telefone: {lead_info['phone']}\n"
        if lead_info.get("email"):
            summary += f"📧 Email: {lead_info['email']}\n"
        if lead_info.get("location"):
            summary += f"📍 Localização: {lead_info['location']}\n"
        if lead_info.get("bill_value"):
            summary += f"💰 Valor da conta: R$ {lead_info['bill_value']:.2f}\n"
        if lead_info.get("property_type"):
            summary += f"🏠 Tipo de imóvel: {lead_info['property_type']}\n"
        if lead_info.get("interests"):
            summary += f"✨ Interesses: {', '.join(lead_info['interests'])}\n"
        if lead_info.get("objections"):
            summary += f"⚠️ Objeções: {', '.join(lead_info['objections'])}\n"
        if lead_info.get("chosen_flow"):
            summary += f"🎯 Fluxo escolhido: {lead_info['chosen_flow']}\n"
        if self.scoring_enabled:
            summary += (
                f"\n🎯 Score: {lead_info['qualification_score']:.0f}/100\n"
                f"📈 Estágio: {lead_info['stage'].upper()}\n"
            )
        return summary