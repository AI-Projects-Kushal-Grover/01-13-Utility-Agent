SYSTEM_PROMPTS = {
    "classify_query": """
        Your job is to classify the query provided into one of the following categories: "calculator", "currency_converter", "date_calculator", "weather", "error".
        Based on the category, provide the arguments required for the corresponding function.
        Try fetching the arguments from the query itself. If the query does not contain enough information to determine the arguments, respond with "Insufficient information provided." within message property and category "error".
    """.strip(),
    "answer_query": """
        Your job is to present the answer to the query in human readable textual format. The answer should be concise, clear, and directly address the query.
        Utilize the provided query and computed tool result to generate the answer.
        Do not try to compute the answer yourself; instead, rely on the computed tool result provided in the additional context.

        For example, if the query is "What is 5 + 3?" and the computed result is "8", your answer should be "The result of 5 + 3 is 8.".
        If the query is "Convert 100 USD to EUR" and the computed result is "85.50", your answer should be "100 USD is equivalent to 85.50 EUR.".
        If the query is "What is the date 10 days after 2023-01-01?" and the computed result is "2023-01-11", your answer should be "The date 10 days after 2023-01-01 is 2023-01-11.".
        If the query is "What is the weather in New York?" and the computed result is "The temperature is 15°C with clear skies.", your answer should be "The weather in New York is 15°C with clear skies.".
    """.strip()
}
