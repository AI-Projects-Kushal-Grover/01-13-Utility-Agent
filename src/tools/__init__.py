from collections.abc import Callable

from models.tools import TOOL_CATEGORY
from tools import calculator, currency, date_calculator, weather

TOOL_FUNCTIONS: dict[TOOL_CATEGORY, Callable] = {
    "calculator": calculator.calculator,
    "currency_converter": currency.currency,
    "date_calculator": date_calculator.date_calculator,
    "weather": weather.weather,
}


def get_tool_function(category: TOOL_CATEGORY):
    if category not in TOOL_FUNCTIONS:
        raise ValueError(f"Unknown tool category: {category}")
    return TOOL_FUNCTIONS[category]
