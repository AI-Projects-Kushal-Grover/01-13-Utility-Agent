import os
from typing import TypeVar, Type

import instructor
from pydantic import BaseModel

TResponse = TypeVar("TResponse", bound=BaseModel)

class LLM():
    def __init__(self) -> None:
        self.model = os.getenv("LLM_MODEL", "gpt-4o-mini")
        mode = os.getenv("LLM_INSTRUCTOR_MODE", "MD_JSON")
        self.client = instructor.from_provider(
            self.model,
            async_client=True,
            mode=instructor.Mode[mode],
            api_key=os.getenv("LLM_API_KEY"),
            base_url=os.getenv("LLM_API_BASE_URL"),
        )

    async def write(self, *, prompt: str, system_prompt: str, response_schema: Type[TResponse], additional_context: dict | None = None) -> TResponse:
        response = await self.client.create(
            messages=[
                {"role": "system", "content": system_prompt.strip()},
                {"role": "user", "content": prompt.strip()}
            ],
            response_model=response_schema,
            context=additional_context
        )
        return response
