from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import engine, Base
from app.models import health_record 
from app.api import auth, prediction, health

# 1. Create Database Tables
Base.metadata.create_all(bind=engine)

# 2. Initialize the App
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# 3. Configure CORS
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# 4. Include Routers (ALL of them must be here, AFTER 'app' is created)
app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(prediction.router, prefix="/api/prediction", tags=["ML Inference"])
app.include_router(health.router, prefix="/api/health", tags=["Health Tracking"])

@app.get("/")
def root():
    return {"system": "MamaCare Backend", "status": "active", "version": "1.0.0"}