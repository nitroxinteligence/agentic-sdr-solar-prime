"""
Google Meet Handler - Solução inteligente para integração com Google Meet
Detecta capacidades e usa a melhor abordagem disponível
"""

import logging
import uuid
from typing import Dict, Optional, Any
from app.config import Settings

logger = logging.getLogger(__name__)
settings = Settings()


class GoogleMeetHandler:
    """
    Handler inteligente para Google Meet
    """

    def __init__(self):
        """Inicializa o handler e detecta capacidades"""
        self.has_domain_delegation = False
        self.delegated_user = None
        self.can_create_meet = False
        self._detect_capabilities()

    def _detect_capabilities(self):
        """Detecta se podemos criar Google Meet nativamente"""
        if (hasattr(settings, 'google_workspace_user_email') and
                settings.google_workspace_user_email):
            self.has_domain_delegation = True
            self.delegated_user = settings.google_workspace_user_email
            self.can_create_meet = True
            logger.info(
                f"✅ Domain-Wide Delegation detectado: {self.delegated_user}"
            )
        else:
            logger.info("⚠️ Domain-Wide Delegation não configurado")
            logger.info(
                "💡 Google Meet nativo requer Domain-Wide Delegation ou OAuth"
            )

    def create_conference_data(self) -> Optional[Dict[str, Any]]:
        """
        Cria conferenceData para Google Calendar
        """
        if self.can_create_meet:
            return {
                'createRequest': {
                    'requestId': str(uuid.uuid4()),
                    'conferenceSolutionKey': {
                        'type': 'hangoutsMeet'
                    }
                }
            }
        return None

    def get_meet_instructions(self, event_id: str = None) -> str:
        """
        Retorna instruções para configurar ou acessar Google Meet
        """
        if self.can_create_meet:
            return """
📹 Google Meet Configurado
✅ Link será gerado automaticamente ao criar o evento
📱 Acesse pelo Google Calendar ou pelo link enviado
"""
        else:
            return f"""
📹 Google Meet - Configuração Necessária

⚠️ Google Meet nativo requer uma das opções:

OPÇÃO 1: Domain-Wide Delegation (Recomendado para empresas)
1. Acesse: https://admin.google.com
2. Vá em Segurança > Controles de API > Delegação em todo o domínio
3. Adicione o Service Account: {settings.google_service_account_email}
4. Com os escopos:
   - https://www.googleapis.com/auth/calendar
   - https://www.googleapis.com/auth/calendar.events
5. Configure a variável de ambiente:
   GOOGLE_WORKSPACE_USER_EMAIL=seu-email@empresa.com

OPÇÃO 2: Criar Meet manualmente
1. Acesse o evento no Google Calendar
2. Clique em "Adicionar videoconferência do Google Meet"
3. O link será criado automaticamente

OPÇÃO 3: Link alternativo temporário
Para criar um link temporário de reunião:
1. Acesse: https://meet.google.com
2. Clique em "Nova reunião"
3. Copie o link e adicione ao evento

📝 Event ID: {event_id or 'N/A'}
"""

    def enhance_event_for_meet(
        self,
        event_data: Dict[str, Any],
        title: str = None,
        description: str = None
    ) -> Dict[str, Any]:
        """
        Aprimora dados do evento para suportar Google Meet
        """
        if self.can_create_meet:
            conference_data = self.create_conference_data()
            if conference_data:
                event_data['conferenceData'] = conference_data
                logger.info("✅ ConferenceData adicionado ao evento")
        return event_data

    def process_created_event(
            self, created_event: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Processa evento criado e extrai informações do Meet
        """
        result = {
            'google_event_id': created_event.get('id'),
            'html_link': created_event.get('htmlLink'),
            'has_meet': False,
            'meet_link': None,
            'meet_setup_required': not self.can_create_meet
        }
        if created_event.get('hangoutLink'):
            result['has_meet'] = True
            result['meet_link'] = created_event['hangoutLink']
            logger.info(f"✅ Google Meet criado: {result['meet_link']}")
        elif created_event.get('conferenceData', {}).get('entryPoints'):
            for entry_point in created_event['conferenceData']['entryPoints']:
                if entry_point.get('entryPointType') == 'video':
                    result['has_meet'] = True
                    result['meet_link'] = entry_point.get('uri')
                    break
        if not result['has_meet'] and self.can_create_meet:
            logger.warning(
                "⚠️ Meet deveria ter sido criado mas não foi encontrado"
            )
        return result

    def get_status(self) -> Dict[str, Any]:
        """
        Retorna status atual do handler
        """
        return {
            'can_create_meet': self.can_create_meet,
            'has_domain_delegation': self.has_domain_delegation,
            'delegated_user': self.delegated_user,
            'service_account': settings.google_service_account_email,
            'recommendations': self._get_recommendations()
        }

    def _get_recommendations(self) -> list:
        """Retorna lista de recomendações baseadas no status atual"""
        recommendations = []
        if not self.can_create_meet:
            recommendations.append(
                "Configure Domain-Wide Delegation para criar Google Meet"
            )
            recommendations.append("Ou use OAuth ao invés de Service Account")
            recommendations.append("Ou adicione Meet manualmente")
        if self.has_domain_delegation:
            recommendations.append("✅ Domain-Wide Delegation configurado")
        return recommendations


google_meet_handler = GoogleMeetHandler()