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

    # 👉 CHAT MODE
    if user_message:
        return base_context + f"""
User question:
"{user_message}"

Answer in clear, simple English.
Be practical and helpful.
Do NOT return JSON.
"""

    # 👉 RECOMMENDATION MODE
    return base_context + """
Give vehicle servicing recommendations based on terrain.

Respond ONLY in valid JSON:
{
  "terrain": "",
  "risk_level": "LOW | MEDIUM | HIGH",
  "recommended_services": [],
  "driving_tips": []
}
"""
