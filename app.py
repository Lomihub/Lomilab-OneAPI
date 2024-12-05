from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from dotenv import load_dotenv
import openai
import redis
import json
import time
import os
from typing import Optional
import shutil
import redis

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

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

@app.post("/push_file/{file_path:path}")
async def push_file(file_path: str):
    try:
        destination_path = f"C:\{os.path.basename(file_path)}"
        with open(file_path, "rb") as src_file:
            with open(destination_path, "wb") as dest_file:
                dest_file.write(src_file.read())
        return {"status": True, "message": "File pushed successfully", "reason": ""}
    except Exception as e:
        return {"status": False, "message": "There was something wrong...", "reason": str(e)}
    

@app.post("/push_folder/{folder_path:path}")
async def copy_folder(folder_path: str, dest_folder: str = "C:\\"):
    if not os.path.exists(folder_path):
        return {"status": False, "message": f"Folder {folder_path} is not exists", "reason": ""}
    
    if not os.path.exists(dest_folder):
        return {"status": False, "message": f"Destination folder {dest_folder} is not exists", "reason": ""}

    try:
        dest_path = os.path.join(dest_folder, os.path.basename(folder_path))
        shutil.copytree(folder_path, dest_path)
        return {"status": True, "message": f"Folder {folder_path} copied to {dest_path}", "reason": ""}
    except Exception as e:
        return {"status": False, "message": "There was something wrong...", "reason": str(e)}