from typing import Literal, Union
from pydantic import BaseModel

TOOL_CATEGORY = Literal["calculator", "currency_converter", "date_calculator", "weather", "error"]

## Calculator Models

class CalculatorInput(BaseModel):
    expression: str

## Currency Converter Models

class CurrencyConverterInput(BaseModel):
    amount: float
    from_currency: str
    to_currency: str

## Date Calculator Models

class DateCalculatorInput(BaseModel):
    date: str
    days_to_add: int

## Weather Models

class WeatherInput(BaseModel):
    location: str

## LLM Query Models

class LLMToolErrorOutput(BaseModel):
    message: str

LLMToolAnswerInput = Union[CalculatorInput, CurrencyConverterInput, DateCalculatorInput, WeatherInput, LLMToolErrorOutput]

class LLMToolClassifierOutput(BaseModel):
    category: TOOL_CATEGORY
    arguments: LLMToolAnswerInput

class LLMToolAnswerOutput(BaseModel):
    answer: str
