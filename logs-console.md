2025-08-23 14:28:52.918 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Model: Erro de quota (429). Tentativa 1 falhou, aguardando 1.0s. Detalhes: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. [violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerDayPerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-pro"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 50
}
, links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, retry_delay {
  seconds: 7
}
]
2025-08-23 14:28:59.158 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Model: Gemini response has no valid part, indicating a potential issue (e.g., safety filters). Triggering fallback. | Data: {'finish_reason': 'N/A', 'prompt_feedback': '', 'error': "Invalid operation: The `response.text` quick accessor requires the response to contain a valid `Part`, but none were returned. The candidate's [finish_reason](https://ai.google.dev/api/generate-content#finishreason) is 1."}
2025-08-23 14:28:59.634 | ERROR    | app.utils.logger:log_with_emoji:75 | ❌ Model: Todas as tentativas falharam após erro de quota: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. [violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerDayPerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-pro"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 50
}
, links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, retry_delay {
}
]
2025-08-23 14:28:59.635 | ERROR    | app.utils.logger:log_with_emoji:75 | ❌ Model: Erro ao chamar modelo: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. [violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerDayPerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-pro"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 50
}
, links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, retry_delay {
}
]
2025-08-23 14:28:59.635 | ERROR    | app.utils.logger:log_with_emoji:75 | ❌ Model: Erro no modelo primário: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. [violations {
  quota_metric: "generativelanguage.googleapis.com/generate_content_free_tier_requests"
  quota_id: "GenerateRequestsPerDayPerProjectPerModel-FreeTier"
  quota_dimensions {
    key: "model"
    value: "gemini-2.5-pro"
  }
  quota_dimensions {
    key: "location"
    value: "global"
  }
  quota_value: 50
}
, links {
  description: "Learn more about Gemini API quotas"
  url: "https://ai.google.dev/gemini-api/docs/rate-limits"
}
, retry_delay {
}
]
2025-08-23 14:28:59.635 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Model: Modelo primário falhou. Acionando fallback para o3-mini.
INFO:     127.0.0.1:48898 - "GET /health HTTP/1.1" 200 OK
2025-08-23 14:29:00.782 | ERROR    | app.utils.logger:log_with_emoji:75 | ❌ Model: Erro na API OpenAI: Error code: 400 - {'error': {'message': "Unsupported parameter: 'temperature' is not supported with this model.", 'type': 'invalid_request_error', 'param': 'temperature', 'code': 'unsupported_parameter'}}
2025-08-23 14:29:00.783 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Resposta do LLM vazia | Data: {'model': 'o3-mini'}
2025-08-23 14:29:00.783 | ERROR    | app.utils.logger:log_with_emoji:75 | ❌ Service: Todos os modelos falharam
2025-08-23 14:29:00.784 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada: Não consegui gerar uma resposta no momento....
2025-08-23 14:29:00.784 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ 🔧 Tags ausentes - adicionando automaticamente
2025-08-23 14:29:00.785 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Resposta formatada com tags: 76 chars
2025-08-23 14:29:06.259 | INFO     | app.utils.logger:log_with_emoji:75 | 📤 Enviando typing para 558182986181 | Data: {'duration_seconds': 1.9, 'message_length': 43, 'recipient': '558182986181', 'type': 'typing'}