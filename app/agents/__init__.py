"""
Agents Module - Agentes Inteligentes com AGNO Framework
Suporta tanto modo Singleton quanto Stateless
"""

from app.agents.agentic_sdr_refactored import (
    AgenticSDR,
    get_agentic_agent,
    create_stateless_agent,
    reset_agent
)

# Importa a versão stateless completa se necessário
try:
    from app.agents.agentic_sdr_stateless import (
        AgenticSDRStateless,
        create_stateless_agent as create_pure_stateless_agent
    )
except ImportError:
    AgenticSDRStateless = None
    create_pure_stateless_agent = None

__all__ = [
    "AgenticSDR",
    "get_agentic_agent",
    "create_stateless_agent",
    "reset_agent",
    "AgenticSDRStateless",
    "create_pure_stateless_agent"
]