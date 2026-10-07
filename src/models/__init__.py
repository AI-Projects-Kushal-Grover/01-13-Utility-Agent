from pydantic import BaseModel, Field

from models.tools import LLMToolClassifierOutput

class QueryRequest(BaseModel):
    query: str = Field()

class QueryResponse(BaseModel):
    answer: str = Field()
    tool_call: LLMToolClassifierOutput | None = Field(default=None)
