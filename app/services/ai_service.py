from groq import Groq
import json
import os
from dotenv import load_dotenv
from app.utils.prompt_builder import build_vehicle_service_prompt

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY is not set")

client = Groq(api_key=GROQ_API_KEY)

# -----------------------------
# Dynamically select a model
# -----------------------------
def get_supported_model() -> str:
    models = client.models.list().data

    # Prefer instruction / chat capable models
    for m in models:
        name = m.id.lower()
        if "it" in name or "chat" in name or "instruct" in name:
            return m.id

    # Fallback: first available model
    return models[0].id



def get_ai_suggestions(
    terrain: str,
    latitude: float,
    longitude: float,
    user_message: str | None = None
):
    prompt = build_vehicle_service_prompt(
        terrain,
        latitude,
        longitude,
        user_message
    )

    completion = client.chat.completions.create(
        model=os.getenv("GROQ_MODEL"),  # dynamic model
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    output = completion.choices[0].message.content.strip()

    # CHAT MODE → return text
    if user_message:
        return output

    # RECOMMENDATION MODE → return JSON
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        return {
            "terrain": terrain,
            "risk_level": "UNKNOWN",
            "recommended_services": ["General vehicle inspection recommended"],
            "driving_tips": ["Drive cautiously and consult a service center"]
        }
