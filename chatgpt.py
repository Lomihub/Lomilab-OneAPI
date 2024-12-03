from pydantic import BaseModel
from typing import List

class ChatGPTMessage(BaseModel):
    role: str
    content: str

class ChatGPTRequest(BaseModel):
    model: str
    messages: List[ChatGPTMessage]
    max_tokens: int
    stream: bool