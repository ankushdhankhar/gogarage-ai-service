from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router

app = FastAPI(title="Terrain-based Vehicle AI Service")

# ✅ CORS FIRST (this fixes OPTIONS 400)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",                     # local dev
        "https://gogarage-car-service.vercel.app"     # deployed frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ ROUTES AFTER CORS
app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "AI service running"}
