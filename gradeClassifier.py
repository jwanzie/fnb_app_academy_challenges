'''Practical Task

Task Overview 

Build a student grade classifier called grade_classifier.py that takes a learner’s name and marks for three subjects, calculates an average, assigns a grade and a status (Pass/Fail), and displays a full report card. The program must correctly use conditionals for all grade and status logic.

Requirements 

- Collect learner name and marks for three subjects (as floats) using input()

- Calculate the average mark across the three subjects

- Assign a letter grade: A (80+), B (70-79), C (60-69), D (50-59), F (below 50) using if/elif/else

- Assign Pass status if the average is 50 or above, Fail otherwise

- Flag any individual subject mark below 40 as ‘needs intervention’

- Display a formatted report card showing all inputs, the average, the grade, the status, and any intervention flags'''

def gradeClassifier():
  name = input('Enter student name: ')
  math_marks = float(input('Enter math marks: '))
  english_marks = float(input('Enter math marks: '))
  science_marks = float(input('Enter math marks: '))
  average = round((math_marks + english_marks + science_marks) / 3, 2)

  if average >= 80:
    grade = 'A'
  elif 79 >= average >= 70:
    grade = 'B'
  elif 69 >= average >= 60:
    grade = 'C'
  elif 59 >= average >= 50:
    grade = 'D'
  else:
    grade = 'F'

  if average >= 50:
    status = 'Pass'
  else:
    status = 'Fail'
  
  print(f'Student name: {name} \nMath: {math_marks} \nEnglish: {english_marks} \nScience: {science_marks} \nAverage: {average} \nGrade: {grade} \nStatus: {status}')

gradeClassifier()