import json

from llm import llm
from llm.system_prompts import SYSTEM_PROMPTS
from models import QueryRequest, QueryResponse
from models.tools import LLMToolClassifierOutput

class QueryAnswerer:
    async def answer_query(self, request: QueryRequest) -> QueryResponse:
        output = await llm.write(
            prompt=request.query,
            system_prompt=SYSTEM_PROMPTS["classify_query"],
            response_schema=LLMToolClassifierOutput
        )
        return QueryResponse(answer=json.dumps(output.model_dump()))
