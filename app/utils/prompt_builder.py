def build_vehicle_service_prompt(
    terrain: str, latitude: float, longitude: float
) -> str:
    return f"""
You are an automotive service expert.

Location:
Latitude: {latitude}
Longitude: {longitude}
Terrain: {terrain}

Suggest vehicle servicing recommendations based on this terrain.

Focus on:
- Suspension & shock absorbers
- Brakes
- Tires
- Engine & cooling
- Safety checks

Respond ONLY in valid JSON.
No explanations.

JSON format:
{{
  "terrain": "{terrain}",
  "risk_level": "LOW | MEDIUM | HIGH",
  "recommended_services": [],
  "driving_tips": []
}}
"""
