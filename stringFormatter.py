'''Username and Message Formatter

Write a Python script called string_formatter.py that takes a user’s first name, last name, and a short bio message as input, then applies multiple string transformations to produce a formatted user profile output. This simulates how a real app backend processes user-submitted text.

Requirements

- Collect first name, last name, and bio message using input()

- Create a username by combining first initial + last name in lowercase (e.g. ‘tdlamini’)

- Display the full name in Title Case using .title()

- Strip leading/trailing whitespace from the bio before displaying it using .strip()

- Count and display the number of characters in the bio using len()

- Replace any occurrence of ‘I am’ in the bio with ‘I’m’ using .replace()

- Display all output using f-strings'''

def stringFormatter():
  first = input('Enter your first name: ')
  last = input('Enter your last name: ')
  bio = input('Enter your bio message: ').strip().replace("I am", "I'm")

  username = (first + last).lower()
  full_name = (first + ' ' + last).title() 

  print(f'Welcome {full_name}!. Your assigned username is {username}.\n Bio ({len(bio)} words): {bio}')

stringFormatter()