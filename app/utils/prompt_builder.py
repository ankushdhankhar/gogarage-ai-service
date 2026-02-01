def build_vehicle_service_prompt(
    terrain: str,
    latitude: float,
    longitude: float,
    user_message: str | None = None
) -> str:

    base_context = f"""
You are an experienced automotive service advisor.

User location:
Latitude: {latitude}
Longitude: {longitude}
Terrain: {terrain}

Vehicle context:
- Suspension
- Shock absorbers
- Brakes
- Tires
- Engine
- Safety systems
"""

    # 👉 CHAT MODE (SHORT ANSWERS ONLY)
    if user_message:
        return base_context + f"""
User question:
"{user_message}"

Rules for answering:
- Use simple English
- Maximum 3 short sentences
- No paragraphs
- No explanations unless asked
- Be direct and practical

Do NOT return JSON.
"""

    # 👉 RECOMMENDATION MODE (COMPACT LISTS)
    return base_context + """
Give vehicle servicing recommendations based on terrain.

Rules:
- Keep each item short (max 6–8 words)
- No explanations
- No paragraphs
- Use clear action phrases

Respond ONLY in valid JSON:
{
  "terrain": "",
  "risk_level": "LOW | MEDIUM | HIGH",
  "recommended_services": [],
  "driving_tips": []
}
"""
