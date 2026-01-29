def infer_terrain(latitude: float, longitude: float) -> str:
    """
    Heuristic-based terrain inference.
    Can be replaced with elevation APIs later.
    """
    if latitude > 25 and longitude < 80:
        return "mountainous"
    elif latitude < 15:
        return "coastal"
    elif 15 <= latitude <= 25:
        return "urban/plain"
    else:
        return "mixed"
