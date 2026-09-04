from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel

app = FastAPI(title="VAI TTS Server")

class TTSRequest(BaseModel):
    text: str
    voice: str = "default"
    model: str = "kokoro"  # Allows switching between "kokoro" and "pocket"

@app.get("/")
def home():
    return {"message": "VAI TTS Server is running!"}

@app.post("/generate")
async def generate_speech(request: TTSRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text parameter is required.")
    
    # Route to the selected model choice
    model_name = request.model.lower()
    
    if model_name == "kokoro":
        # Add your Kokoro generation code here
        pass
    elif model_name == "pocket":
        # Add your Pocket TTS generation code here
        pass
    else:
        raise HTTPException(status_code=400, detail=f"Model '{request.model}' is not supported.")

    # Replace this placeholder with your model's actual output audio bytes
    dummy_audio_bytes = b""
    
    return Response(content=dummy_audio_bytes, media_type="audio/wav")
