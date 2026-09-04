from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import io

# Optional imports depending on what you have installed:
# For Kokoro: pip install kokoro soundfile
# For Pocket TTS: pip install pocket-tts

app = FastAPI(title="VAI TTS Server")

class TTSRequest(BaseModel):
    text: str
    voice: str = "default"
    model: str = "kokoro"  # allows switching between "kokoro" and "pocket"

@app.get("/")
def home():
    return {"message": "VAI TTS Server is running!"}

@app.post("/generate")
async def generate_speech(request: TTSRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    
    model_name = request.model.lower()
    
    try:
        audio_bytes = None
        
        if model_name == "kokoro":
            # --- Kokoro Integration Placeholder ---
            # Example logic structure for Kokoro:
            # from kokoro import KPipeline
            # import soundfile as sf
            # pipeline = KPipeline(lang_code='a')
            # generator = pipeline(request.text, voice=request.voice if request.voice != "default" else "af_heart")
            # for i, (gs, ps, audio) in enumerate(generator):
            #     # writing audio to a bytes buffer
            #     buffer = io.BytesIO()
            #     sf.write(buffer, audio, 24000, format='WAV')
            #     audio_bytes = buffer.getvalue()
            #     break # get the first segment
            
            pass # Remove 'pass' once you paste your specific logic
            
        elif model_name == "pocket":
            # --- Pocket TTS Integration Placeholder ---
            # Example logic structure for Pocket TTS:
            # from pocket_tts import TTSModel
            # import scipy.io.wavfile
            # tts_model = TTSModel.load_model()
            # voice_state = tts_model.get_state_for_audio_prompt(request.voice if request.voice != "default" else "alba")
            # audio = tts_model.generate_audio(voice_state, request.text)
            # buffer = io.BytesIO()
            # scipy.io.wavfile.write(buffer, tts_model.sample_rate, audio.numpy())
            # audio_bytes = buffer.getvalue()
            
            pass # Remove 'pass' once you paste your specific logic
            
        else:
            raise HTTPException(status_code=400, detail=f"Unsupported model: {model_name}")

        # If audio_bytes is still empty because code isn't plugged in yet, return a mock response or error
        if not audio_bytes:
            return JSONResponse(
                status_code=501, 
                content={"detail": f"Model '{model_name}' logic is not fully wired up yet in code."}
            )

        # Return the generated audio file back to your app
        return Response(content=audio_bytes, media_type="audio/wav")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
