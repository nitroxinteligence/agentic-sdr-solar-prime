"""
Prompt Builder for the Agentic SDR
"""
import os
from typing import Dict, Any, List

class PromptBuilder:
    """Builds prompts for the agent."""

    def __init__(self, prompt_file: str = "app/prompts/prompt-agente.md"):
        self.prompt_file = prompt_file
        self.system_prompt = self._load_system_prompt()

    def _load_system_prompt(self) -> str:
        """Loads the system prompt from a file."""
        try:
            # Correctly determine the path to the prompt file relative to this file
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # Go up two directories to the app's root, then to the file
            base_dir = os.path.dirname(os.path.dirname(current_dir))
            file_path = os.path.join(base_dir, 'app', 'prompts', 'prompt-agente.md')

            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return "Você é um assistente de vendas."

    def get_system_prompt(self) -> str:
        """Returns the loaded system prompt."""
        return self.system_prompt

    def build_user_prompt(
        self,
        message: str,
        conversation_history: List[Dict[str, Any]],
        lead_info: Dict[str, Any],
        context: Dict[str, Any],
        media_context: str,
        is_followup: bool = False
    ) -> str:
        """Builds the user prompt with all the necessary context."""
        
        history_str = "\n".join(
            [f"{msg['role']}: {msg['content']}" for msg in conversation_history]
        )

        prompt = (
            f"=== Histórico da Conversa ===\n{history_str}\n\n"
            f