from typing import Literal, Union
from pydantic import BaseModel

TOOL_CATEGORY = Literal["calculator", "currency_converter", "date_calculator", "weather", "error"]

## Calculator Models

class CalculatorInput(BaseModel):
    expression: str

class CalculatorOutput(BaseModel):
    result: str

## Currency Converter Models

class CurrencyConverterInput(BaseModel):
    amount: float
    from_currency: str
    to_currency: str

class CurrencyConverterOutput(BaseModel):
    converted_amount: float

## Date Calculator Models

class DateCalculatorInput(BaseModel):
    date: str
    days_to_add: int

class DateCalculatorOutput(BaseModel):
    final_date: str

## Weather Models

class WeatherInput(BaseModel):
    location: str

class WeatherOutput(BaseModel):
    temperature: float
    condition: str

## LLM Query Models

class LLMToolErrorOutput(BaseModel):
    message: str

class LLMToolClassifierOutput(BaseModel):
    category: TOOL_CATEGORY
    arguments: Union[CalculatorInput, CurrencyConverterInput, DateCalculatorInput, WeatherInput, LLMToolErrorOutput]
