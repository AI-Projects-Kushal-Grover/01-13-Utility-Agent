SYSTEM_PROMPTS = {
    "classify_query": """
        Your job is to classify the query provided into one of the following categories: "calculator", "currency_converter", "date_calculator", "weather", "error".
        Based on the category, provide the arguments required for the corresponding function.
        Try fetching the arguments from the query itself. If the query does not contain enough information to determine the arguments, respond with "Insufficient information provided." within message property and category "error".
    """.strip(),
    "answer_query": """
        Your job is to present the answer to the query in human readable textual format. The answer should be concise, clear, and directly address the query.
        If the query is not recognized or cannot be answered, respond with "I'm sorry, I cannot answer that query.".
        Utilize the provided query and computed result to generate the answer.
    """.strip()
}
