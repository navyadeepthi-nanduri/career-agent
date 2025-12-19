from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .schemas import RecommendationRequest, RecommendationResponse
from .ai_logic import generate_recommendation

app = FastAPI(title="Career Guidance AI Agent")

# Allow frontend (running on another port) to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in production, restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Career Guidance AI Agent backend is running"}

@app.post("/recommend", response_model=RecommendationResponse)
def get_recommendation(request: RecommendationRequest):
    return generate_recommendation(request.profile)
