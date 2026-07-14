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