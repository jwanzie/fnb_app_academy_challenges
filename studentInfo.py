'''Task Overview

Student Info Formatter

Write a Python script called student_info.py that collects personal information from the user and displays it in a formatted profile card. The program must demonstrate correct use of all four data types, string manipulation, arithmetic, and the f-string output format.

Requirements

- Use input() to collect: first name, surname, age (as an integer), and a favourite number (as a float)

- Display a formatted greeting using an f-string: ‘Welcome, [Full Name]!’

- Display the name in UPPERCASE using .upper() and in Title Case using .title()

- Calculate and display the age in months (age × 12)
 
- Round the favourite number to 2 decimal places using round()

- Print the data type of each collected value using type()'''

def studentInfo():
  firstname = input('Enter first name: ')
  surname = input('Enter surname: ')
  name = firstname + ' ' + surname
  print(f'Welcome, {name.upper().title()}')

  age = int(input('Enter age: '))
  print(f'Age in months, {age * 12}')

  favorite_number = float(input('Enter favorite number: '))
  print(f'Favorite number is, {round(favorite_number, 2)}')

  print(type(name), type(age), type(favorite_number))

studentInfo()