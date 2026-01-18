from pydantic import BaseModel

class DepressionRequest(BaseModel):
    query: str
    type: str
    top_k: int

class DepressionUpdate(BaseModel):
    id: int
    query: str
    type: str
    top_k: int