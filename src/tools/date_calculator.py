from datetime import datetime, timedelta

def date_calculator(date: str, days_to_add: int) -> str:
    try:
        # Parse the input date string into a datetime object
        input_date = datetime.strptime(date, "%Y-%m-%d")
        
        # Add the specified number of days
        final_date = input_date + timedelta(days=days_to_add)
        
        # Return the final date as a string in the same format
        return final_date.strftime("%Y-%m-%d")
    except ValueError as e:
        return f"Error: {e}"