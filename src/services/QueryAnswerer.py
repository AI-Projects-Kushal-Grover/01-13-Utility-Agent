import json

from llm import llm
from llm.system_prompts import SYSTEM_PROMPTS
from models import QueryRequest, QueryResponse
from models.tools import LLMToolAnswerOutput, LLMToolClassifierOutput
from tools import get_tool_function

class QueryAnswerer:
    async def answer_query(self, request: QueryRequest) -> QueryResponse:
        output = await llm.write(
            prompt=request.query,
            system_prompt=SYSTEM_PROMPTS["classify_query"],
            response_schema=LLMToolClassifierOutput
        )
        if output.category == "error":
            return QueryResponse(answer=json.dumps(output.arguments.model_dump()))

        tool_function = get_tool_function(output.category)
        tool_result = tool_function(**output.arguments.model_dump())

        result_output = await llm.write(
            prompt=request.query,
            system_prompt=SYSTEM_PROMPTS["answer_query"],
            response_schema=LLMToolAnswerOutput,
            additional_context={f"{output.category} tool result": tool_result}
        )

        return QueryResponse(answer=result_output.answer, tool_call=output)
