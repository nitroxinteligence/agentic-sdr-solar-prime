(.venv) mateusmpz@Mateuss-MacBook-Pro agent-sdr-ia-solarprime % python main.py
✅ Arquivo .env encontrado: /Users/mateusmpz/Documents/Projetos Clientes - Code/agent-sdr-ia-solarprime/.env
Traceback (most recent call last):
  File "/Users/mateusmpz/Documents/Projetos Clientes - Code/agent-sdr-ia-solarprime/main.py", line 15, in <module>
    from app.api import health, webhooks  # teams module not yet implemented
  File "/Users/mateusmpz/Documents/Projetos Clientes - Code/agent-sdr-ia-solarprime/app/api/webhooks.py", line 20, in <module>
    from app.agents.agentic_sdr_refactored import get_agentic_agent
  File "/Users/mateusmpz/Documents/Projetos Clientes - Code/agent-sdr-ia-solarprime/app/agents/__init__.py", line 6, in <module>
    from app.agents.agentic_sdr_stateless import (
ImportError: cannot import name 'create_stateless_agent' from 'app.agents.agentic_sdr_stateless' (/Users/mateusmpz/Documents/Projetos Clientes - Code/agent-sdr-ia-solarprime/app/agents/agentic_sdr_stateless.py)