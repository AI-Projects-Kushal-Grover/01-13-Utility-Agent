from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    query: str = Field()

class QueryResponse(BaseModel):
    answer: str = Field()
