import os
import re
import requests

HF_API_TOKEN = os.getenv("HF_API_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}"
}

# =========================
# CLASSIFICAÇÃO (HEURÍSTICA NLP)
# =========================

PRODUCTIVE_KEYWORDS = [
    "status", "chamado", "problema", "erro",
    "suporte", "atualização", "pendente",
    "dúvida", "solicitação", "request"
]

THRESHOLD = 1


def classify_email_with_ai(text: str) -> str:
    text = text.lower()

    score = sum(
        1 for word in PRODUCTIVE_KEYWORDS
        if re.search(rf"\b{word}\b", text)
    )

    return "Produtivo" if score >= THRESHOLD else "Improdutivo"


# =========================
# GERAÇÃO DE RESPOSTA (IA)
# =========================

GENERATOR_URL = (
    "https://api-inference.huggingface.co/models/"
    "google/flan-t5-base"
)


def generate_response(category: str, email_text: str) -> str:
    if category == "Produtivo":
        prompt = (
            "Gere uma resposta educada e profissional para um email "
            "corporativo que solicita suporte ou atualização de status."
        )
    else:
        prompt = (
            "Gere uma resposta curta, cordial e profissional para um email "
            "que não exige ação imediata."
        )

    payload = {"inputs": prompt}

    try:
        response = requests.post(
            GENERATOR_URL,
            headers=HEADERS,
            json=payload,
            timeout=30
        )

        result = response.json()

        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"]

    except Exception:
        pass

    return "Agradecemos sua mensagem. Em breve retornaremos."
