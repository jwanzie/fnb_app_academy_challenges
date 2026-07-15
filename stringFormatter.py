'''Username and Message Formatter
Write a Python script called string_formatter.py that takes a user’s first name, last name, and a short bio message as input, then applies multiple string transformations to produce a formatted user profile output. This simulates how a real app backend processes user-submitted text.'''

def stringFormatter():
  first = input('Enter your first name: ')
  last = input('Enter your last name: ')
  bio = input('Enter your bio message: ').strip().replace("I am", "I'm")

  username = (first + last).lower()
  full_name = (first + ' ' + last).title() 

  print(f'Welcome {full_name}!. Your assigned username is {username}.\n Bio ({len(bio)} words): {bio}')

stringFormatter()