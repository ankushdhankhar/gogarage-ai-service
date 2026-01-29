from fastapi import APIRouter
from app.models.location import LocationRequest
from app.services.terrain_service import infer_terrain
from app.services.ai_service import get_ai_suggestions

router = APIRouter(prefix="/ai", tags=["AI"])

@router.post("/analyze")
def analyze_location(data: LocationRequest):
    terrain = infer_terrain(data.latitude, data.longitude)

    suggestions = get_ai_suggestions(
        terrain,
        data.latitude,
        data.longitude
    )

    return {
        "status": "success",
        "latitude": data.latitude,
        "longitude": data.longitude,
        "terrain": terrain,
        "suggestions": suggestions
    }
