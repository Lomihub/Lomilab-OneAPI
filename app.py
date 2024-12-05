from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import openai
import redis
import json
import time
import os
from typing import Optional

openai.api_key = "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"
redis_client = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)

app = FastAPI()

class AnonymousRequestBody(BaseModel):
    message: str

def get_anonymous_response(message: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": message}],
            max_tokens=150
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API Error: {str(e)}")

def get_anonymous_response_with_cache(message: str) -> str:
    cache_key = f":chatgpt:{message}"
    
    cached_response = redis_client.get(cache_key)
    if cached_response:
        return cached_response
    
    response = get_anonymous_response(message)
    
    redis_client.setex(cache_key, 21600, response)
    
    return response

@app.post("/anonymous")
async def anonymous_api(request: AnonymousRequestBody):
    message = request.message.strip()
    if not message:
        raise HTTPException(status_code=400, detail="Message is empty")
    
    try:
        response = get_anonymous_response_with_cache(message)
        return {"status": True, "message": response, "reason": ""}
    except Exception as e:
        return {"status": False, "message": "There was something wrong...", "reason": str(e)}
    
@app.post("/upload_file/{file_path:path}")
async def import_file(file_path: str):
    try:
        with open(file_path, "r") as file:
            # Assume that we are uploading the file to Google Drive
            return {"status": True, "message": "File uploaded successfully", "reason": ""}
    except Exception as e:
        return {"status": False, "message": "There was something wrong...", "reason": str(e)}
    
@app.post("/upload_folder/{folder_path:path}")
async def import_folder(folder_path: str):
    try:
        if os.path.isdir(folder_path):
            return {"status": True, "message": "Folder uploaded successfully", "reason": ""}
        else:
            return {"status": False, "message": "Folder not found", "reason": ""}
    except Exception as e:
        return {"status": False, "message": "There was something wrong...", "reason": str(e)}

