import re
from typing import Callable
from decimal import Decimal

text = '''Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, 
доповнений додатковими надходженнями 27.45 і 324.00 доларів. Також 555.56 баксів і 123.23 євро'''

def generator_numbers(text: str):
    real_numbers = re.findall(' (\\d+.\\d+) ', text)    # Regex for list of real numbers
    for real_number in real_numbers:
        yield Decimal(real_number)                      # Making generator to give real numbers one by one

def sum_profit(text: str, func: Callable):              # Calculating sum using generator
    sum = 0
    for number in func(text):
        sum += number
    return sum

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")