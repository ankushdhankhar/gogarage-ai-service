import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    ALLOWED_ORIGINS = [
        "http://localhost:3000",                     # local dev
        "https://gogarage-car-service.vercel.app"     # deployed frontend
    ]

settings = Settings()
