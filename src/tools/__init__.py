from models.tools import TOOL_CATEGORY
from tools import calculator, currency, date_calculator, weather

def get_tool_function(category: TOOL_CATEGORY):
    if category == "calculator":
        return calculator.calculator
    elif category == "currency_converter":
        return currency.currency
    elif category == "date_calculator":
        return date_calculator.date_calculator
    elif category == "weather":
        return weather.weather
    else:
        raise ValueError(f"Unknown tool category: {category}")
