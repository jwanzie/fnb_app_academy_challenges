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