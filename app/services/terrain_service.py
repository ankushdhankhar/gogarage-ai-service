def infer_terrain(latitude: float, longitude: float) -> str:
    # India-focused + generic rules
    if latitude > 28:
        return "mountainous"
    elif latitude < 15:
        return "coastal"
    elif 15 <= latitude <= 28:
        # longitude-based refinement
        if longitude > 75:
            return "urban/plain"
        else:
            return "rural/plain"
    else:
        return "mixed"
