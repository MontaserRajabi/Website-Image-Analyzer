from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import requests, os

app = FastAPI()

VISION_KEY = os.getenv("74zfy9oNEFghoq9YhWvdkz4P73G2fC9t3tfMqgqndVvwUhu7TX1MJQQJ99BJAC5T7U2XJ3w3AAAFACOGLsqX")
VISION_ENDPOINT = os.getenv("https://asdaasdasdads.cognitiveservices.azure.com/")
ANALYZE_URL = f"{VISION_ENDPOINT}/vision/v3.2/analyze"

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    headers = {
        "Ocp-Apim-Subscription-Key": VISION_KEY,
        "Content-Type": "application/octet-stream"
    }
    params = {"visualFeatures": "Categories,Description,Objects,Tags"}
    img_bytes = await file.read()
    response = requests.post(ANALYZE_URL, headers=headers, params=params, data=img_bytes)
    return JSONResponse(content=response.json())
