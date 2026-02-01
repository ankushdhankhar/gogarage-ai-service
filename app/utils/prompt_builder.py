def build_vehicle_service_prompt(
    terrain: str,
    latitude: float,
    longitude: float,
    user_message: str | None = None
) -> str:

    base_prompt = f"""
You are an automotive service expert.

Location:
Latitude: {latitude}
Longitude: {longitude}
Terrain: {terrain}
"""

    if user_message:
        return base_prompt + f"""
User question:
"{user_message}"

Answer clearly and concisely in plain text.
"""

    return base_prompt + """
Provide vehicle servicing recommendations.

Respond ONLY in valid JSON:
{
  "terrain": "",
  "risk_level": "",
  "recommended_services": [],
  "driving_tips": []
}
"""
