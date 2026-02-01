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

    for m in models:
        name = m.id.lower()
        if "it" in name or "chat" in name or "instruct" in name:
            return m.id

    return models[0].id


MODEL_NAME = get_supported_model()
print(f"[Groq] Using model: {MODEL_NAME}")


def get_ai_suggestions(
    terrain: str,
    latitude: float,
    longitude: float,
    user_message: str | None = None
):
    """
    If user_message is provided → return CHAT TEXT
    Else → return JSON recommendations
    """

    prompt = build_vehicle_service_prompt(
        terrain,
        latitude,
        longitude,
        user_message
    )

    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        output = completion.choices[0].message.content.strip()

        # 🔥 CHAT MODE → RETURN TEXT
        if user_message:
            return output

        # 🔥 RECOMMENDATION MODE → RETURN JSON
        try:
            return json.loads(output)
        except json.JSONDecodeError:
            return {
                "terrain": terrain,
                "risk_level": "UNKNOWN",
                "recommended_services": [
                    "General vehicle inspection recommended"
                ],
                "driving_tips": [
                    "Drive cautiously and consult a service center"
                ],
                "raw_ai_output": output
            }

    except Exception as e:
        return {
            "error": "Groq AI error",
            "details": str(e),
            "model_used": MODEL_NAME
        }
