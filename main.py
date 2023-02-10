from base64 import urlsafe_b64decode as b64decode
from typing import Optional

from fastapi import FastAPI
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware


from utils import get_video_urls, heights




app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def home():
    return "video -} /video/base64($video_url_id)?height=$height\naudio -} /audio/base64($video_url_id)\naudio + video -} /base64($video_url_id)?height=$height"

@app.get("/{video_id_b64}")
def audio_video(video_id_b64: str,  height: Optional[int] = 720):
    # Parse video_id and return JSON
    try:
        video_id = b64decode(video_id_b64).decode("ascii")
    except:
        return {"error": "Invalid base64 data"}
    return get_video_urls(video_id, "audio_video", height)

