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

Vehicle service context:
- Suspension
- Brakes
- Tires
- Engine
- Safety
"""

    if user_message:
        return base_prompt + f"""
User question:
"{user_message}"

Answer clearly and briefly.
"""

    return base_prompt + """
Give vehicle servicing recommendations.

Respond ONLY in JSON:
{
  "terrain": "",
  "risk_level": "",
  "recommended_services": [],
  "driving_tips": []
}
"""
