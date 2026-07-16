'''Task Overview

Multi-Function Calculator

Build a Python calculator called calculator.py that takes two numbers as input and performs all four basic arithmetic operations plus two advanced operations. The calculator must handle user input safely using type casting and display results clearly using f-strings.

Requirements

- Use float(input()) to collect two numbers from the user

- Calculate and display: addition, subtraction, multiplication, division

- Calculate and display: floor division (//) and modulus (%)

- Round all results to 2 decimal places using round()

- Handle division by zero — if the second number is 0, display a friendly error message instead of crashing

- Display all results in a formatted table using f-strings'''

def calculator():
  num1 = float(input('Enter the first number: '))
  num2 = float(input('Enter the second number: '))

  try:
    sum = round(num1 + num2, 2)
    diff = round(num1 - num2, 2)
    multi = round(num1 * num2, 2)
    div = round(num1 / num2, 2)
    intDiv = round(num1 // num2, 2)
    mod = round(num1 % num2, 2)
   
    print(f'Sum = {sum} \nDifference = {diff} \nMultiplication = {multi} \nDivision = {div} \nInteger Division = {intDiv} \nModulus = {mod}')
  
  except ZeroDivisionError:
    
    print(f'Sum = {sum} \nDifference = {diff} \nMultiplication = {multi} \nDivision = Error: Cannot divide by zero \nInteger Division = Error: Cannot divide by zero \nModulus = Error: Cannot divide by zero')

calculator()