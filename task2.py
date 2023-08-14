"""# Get user input for student's information
name = input("Enter student's name: ")
age = input("Enter student's age: ")
course = input("Enter student's course: ")
marks = float(input("Enter student's marks: "))

# Create the student dictionary
student = {
    'name': name,
    'age': age,
    'course': course,
    'marks': marks
}

# Display the student dictionary
print("Student information:")
print(student)
"""


"""num = int(input("enter the value of students number :"))"""

# Get user input for the number of key-value pairs
num_pairs = int(input("Enter the number of key-value pairs: "))

# Initialize an empty dictionary
dynamic_dict = {}
dynamic_dicts = {}

# Loop to populate the dictionary with user input
for i in range(num_pairs):
    key = input(f"Enter key {i + 1}: ")
    roll_no = int(input(f'enter roll no for student  {i +1}: '))
    name = (input(f'enter name for student  {i +1}: '))
    marks = int(input(f'enter marks no for student  {i +1}: '))
    grade = ''
    if(90<marks<=100):
       grade = "A"
    elif(80<marks<=90):
      grade = "B"
    elif(60<marks<=80):
      grade = "C"
    elif(40<=marks<=60):
      grade = "D"
    elif(0<=marks<40):
      grade = "FAIL"
    else:
      print("Invalid Marks")
    grades = grade

    dynamic_dicts = {
        'roll_no':roll_no,
        'name':name,
        'marks':marks,
        'grade':grades,
    }
    dynamic_dict[key] = dynamic_dicts



# Display the dynamically created dictionary
print("Dynamically created dictionary:")
print(dynamic_dict)
"""for student, data in dynamic_dict.items():
  print(f"{student} : {data}")"""

update = input("Enter yes to update student's marks or enter no: ")
if update == 'yes':
  student_to_update = input("Enter thr name of student whose marks you want to edit: ")
  if student_to_update in dynamic_dicts:
    new_marks = int(input("Enter marks for updatation: "))
    dynamic_dicts[marks] = new_marks
    if(90<marks<=100):
       grade = "A"
    elif(80<marks<=90):
      grade = "B"
    elif(60<marks<=80):
      grade = "C"
    elif(40<=marks<=60):
      grade = "D"
    elif(0<=marks<40):
      grade = "FAIL"
    else:
      print("Invalid Marks")
    grades = grade
    dynamic_dict[grade] = grade
  else:
    print("student not found")

for student, data in dynamic_dict.items():
  print(f"{student} : {data}")