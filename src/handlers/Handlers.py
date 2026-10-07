from models import QueryRequest, QueryResponse
from services import query_answerer

class QueryHandler:
    async def answer_query(self, request: QueryRequest) -> QueryResponse:
        return await query_answerer.answer_query(request)
