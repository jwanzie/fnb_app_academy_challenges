def gradeReport():
  students = [{'Name': 'Joan',
              'Maths': 90, 
              'English': 56, 
              'Science': 83}, 
              
            {'Name': 'Joy', 
              'Maths': 81, 
              'English': 66, 
              'Science': 78}, 
            
            {'Name': 'Jane', 
              'Maths': 50, 
              'English': 67, 
              'Science': 66}, 
            
            {'Name': 'Jim', 
              'Maths': 76, 
              'English': 46, 
              'Science': 88}, 
            
            {'Name': 'John', 
              'Maths': 67, 
              'English': 59, 
              'Science': 64}]
  
  print('Grade Report.')

  for i, student in enumerate(students):
    average = round((student['Maths'] + student['English'] + student['Science']) / 3, 2)

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
    
    print(f'Name: {student['Name']} \nAverage: {average} \nGrade: {grade} \nStatus: {status}\n')
  
gradeReport()