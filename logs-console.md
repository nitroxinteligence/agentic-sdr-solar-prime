2025-08-23 14:20:50.924 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Model: Gemini response has no valid part, indicating a potential issue (e.g., safety filters). Triggering fallback. | Data: {'finish_reason': 'N/A', 'prompt_feedback': '', 'error': "Invalid operation: The `response.text` quick accessor requires the response to contain a valid `Part`, but none were returned. The candidate's [finish_reason](https://ai.google.dev/api/generate-content#finishreason) is 1."}
2025-08-23 14:20:51.431 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ Model: Erro de quota (429). Tentativa 2 falhou, aguardando 1.0s. Detalhes: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. [violations {
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
  seconds: 8
}
]
2025-08-23 14:20:52.910 | ERROR    | app.utils.logger:log_with_emoji:75 | ❌ Model: Todas as tentativas falharam após erro de quota: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. [violations {
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
2025-08-23 14:20:52.910 | ERROR    | app.utils.logger:log_with_emoji:75 | ❌ Model: Erro ao chamar modelo: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. [violations {
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
2025-08-23 14:20:52.910 | ERROR    | app.utils.logger:log_with_emoji:75 | ❌ Model: Erro no modelo primário: 429 You exceeded your current quota, please check your plan and billing details. For more information on this error, head to: https://ai.google.dev/gemini-api/docs/rate-limits. [violations {
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
2025-08-23 14:20:52.911 | ERROR    | app.utils.logger:log_with_emoji:75 | ❌ Service: Todos os modelos falharam
2025-08-23 14:20:52.911 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ Resposta gerada: Não consegui gerar uma resposta no momento....
2025-08-23 14:20:52.912 | WARNING  | app.utils.logger:log_with_emoji:75 | ⚠️ 🔧 Tags ausentes - adicionando automaticamente
2025-08-23 14:20:52.912 | INFO     | app.utils.logger:log_with_emoji:75 | ✅ ✅ Resposta formatada com tags: 76 chars
2025-08-23 14: