from simpleeval import simple_eval

def calculator(expression: str) -> str:
    try:
        result = simple_eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {e}"
