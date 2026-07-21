'''Practical Task

Task Overview

Build a command-line contact book called contact_book.py that stores contacts as a list of dictionaries and allows the user to add, search, view, and delete contacts. This is a foundational data structure pattern used in virtually every real app.

Requirements

- Store contacts as a list of dictionaries, each with keys: name, phone, email

- Implement an add_contact() function that appends a new dictionary to the list

- Implement a search_contact(name) function that searches by name and returns the matching dictionary (or None if not found)

- Implement a delete_contact(name) function that removes a contact by name

- Implement a view_all() function that displays all contacts in a formatted layout

- Use a while loop menu to let the user choose an action (1=Add, 2=Search, 3=Delete, 4=View All, 5=Exit)
'''

contacts = []

def add_contact(contacts):

  new_contact = ({'name': input('Enter name: '), 'phone': input('Enter phone number: '), 'email': input('Enter email: ')})
  contacts.append(new_contact)
  
  print(f'Successfully added new contact!') 


def search_contact(contacts):
  name = input('Enter name: ')

  for i, contact in enumerate(contacts):
    if contact['name'] == name:
      print(f'{i+1}. Name: {contact['name']}  \nPhone Number: {contact['phone']}  \nEmail: {contact['email']}')
  

def delete_contact(name):
  name = input('Enter name: ')

  for i, contact in enumerate(contacts):
    if contact['name'] == name:
      contacts.remove(contacts[i])
      print('Contact deleted')


def view_all(contacts):
  for i, contact in enumerate(contacts):
    print(f'{i+1}. Name: {contact['name']}  \nPhone Number: {contact['phone']}  \nEmail: {contact['email']}')


while True:
  print('1. Add contact \n2. Search contact \n3. Delete contact. \n4. View contacts \n5. Exit')

  choice = input('Choose an option: ')

  if choice == '1':
    add_contact(contacts)
  elif choice == '2':
    search_contact(contacts)
  elif choice == '3':
    delete_contact(contacts)
  elif choice == '4':
    view_all(contacts)
  elif choice == '5':
    break
  else:
    print('Invalid choice, try again')