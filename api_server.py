from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, HttpUrl, Field
from typing import Optional, List, Dict, Any
import logging
from main import get_youtube_transcript, extract_video_id

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="YouTube Transcript API",
    description="API to fetch transcripts from YouTube videos",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Pydantic models for request/response
class TranscriptRequest(BaseModel):
    url: str = Field(..., description="YouTube video URL")
    languages: Optional[List[str]] = Field(default=["en"], description="Preferred languages for transcript")
    include_timestamps: bool = Field(default=True, description="Include timestamp information")

class TranscriptSegment(BaseModel):
    text: str
    start: float
    duration: float

class TranscriptResponse(BaseModel):
    success: bool
    video_id: Optional[str]
    video_url: Optional[str]
    transcript: Optional[Dict[str, Any]]
    languages_used: Optional[List[str]]
    error: Optional[str]

class HealthResponse(BaseModel):
    status: str
    service: str
    version: str

# API Endpoints
@app.get("/", response_model=Dict[str, str])
async def root():
    """Root endpoint with basic API information."""
    return {
        "message": "YouTube Transcript API",
        "docs": "/docs",
        "redoc": "/redoc",
        "health": "/health"
    }

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        service="youtube-transcript-api",
        version="1.0.0"
    )

@app.post("/transcript", response_model=TranscriptResponse)
async def get_transcript_endpoint(request: TranscriptRequest):
    """
    Get transcript from YouTube video URL.
    
    - **url**: YouTube video URL (required)
    - **languages**: List of preferred languages (default: ["en"])
    - **include_timestamps**: Whether to include timing information
    """
    try:
        logger.info(f"Processing transcript request for URL: {request.url}")
        
        # Get transcript using our main function
        result = get_youtube_transcript(request.url, request.languages)
        
        # If timestamps not requested, remove them from structured data
        if not request.include_timestamps and result.get('success'):
            if result['transcript'] and result['transcript'].get('structured'):
                for segment in result['transcript']['structured']:
                    segment.pop('start', None)
                    segment.pop('duration', None)
        
        logger.info(f"Transcript request completed - Success: {result.get('success')}")
        return TranscriptResponse(**result)
        
    except Exception as e:
        logger.error(f"Error processing transcript request: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@app.get("/transcript", response_model=TranscriptResponse)
async def get_transcript_get(
    url: str = Query(..., description="YouTube video URL"),
    languages: str = Query("en", description="Comma-separated list of preferred languages"),
    include_timestamps: bool = Query(True, description="Include timestamp information")
):
    """
    Get transcript from YouTube video URL using GET method.
    
    - **url**: YouTube video URL (required)
    - **languages**: Comma-separated preferred languages (default: "en")
    - **include_timestamps**: Whether to include timing information
    """
    # Convert comma-separated languages to list
    languages_list = [lang.strip() for lang in languages.split(',') if lang.strip()]
    
    # Create request object and use POST endpoint logic
    request = TranscriptRequest(
        url=url,
        languages=languages_list,
        include_timestamps=include_timestamps
    )
    
    return await get_transcript_endpoint(request)

@app.get("/video-id")
async def extract_video_id_endpoint(url: str = Query(..., description="YouTube video URL")):
    """Extract video ID from YouTube URL."""
    try:
        video_id = extract_video_id(url)
        if video_id:
            return {"success": True, "video_id": video_id, "url": url}
        else:
            raise HTTPException(status_code=400, detail="Invalid YouTube URL format")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Error handlers
@app.exception_handler(404)
async def not_found_handler(request, exc):
    return {"error": "Endpoint not found", "message": "Check /docs for available endpoints"}

@app.exception_handler(500)
async def internal_error_handler(request, exc):
    return {"error": "Internal server error", "message": "Please try again later"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 