"""def create_student():
    student_data = {}
    
    roll_no = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    grade = input("Enter Grade: ")
    
    student_data['roll_no'] = roll_no
    student_data['name'] = name
    student_data['marks'] = marks
    student_data['grade'] = grade
    
    return student_data

def main():
    num_students = int(input("Enter the number of students: "))
    student_records = {}

    for i in range(num_students):
        student = create_student()
        student_records[f'Student{i+1}'] = student

    print("\nStudent Records:")
    for student, data in student_records.items():
        print(f"{student}: {data}")

if __name__ == "__main__":
    main()
"""
"""n = int(input("Enter the number : "))

stud_data = {}
stud_records = {}

for i in range(n+1):
    stud_records[i] = stud_data
    for j in range(i):
        roll_no = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        grade = input("Enter Grade: ")


        stud_data['roll_no'] = roll_no
        stud_data['marks'] = marks
        stud_data['name'] = name
        stud_data['grade'] = grade

for student , data in stud_records.items():
        print(f"Student{student}: DATA:{data} ")"""

def main():
    # Get user input for the number of key-value pairs
    num_pairs = int(input("Enter the number of key-value pairs: "))

    # Initialize an empty dictionary
    dynamic_dict = {}

    # Loop to populate the dictionary with user input
    for i in range(num_pairs):
        key = input(f"Enter key {i + 1}: ")
        roll_no = int(input(f'Enter roll no for student {i + 1}: '))
        name = input(f'Enter name for student {i + 1}: ')
        marks = int(input(f'Enter marks for student {i + 1}: '))
        grade = ''
        if 90 < marks <= 100:
            grade = "A"
        elif 80 < marks <= 90:
            grade = "B"
        elif 60 < marks <= 80:
            grade = "C"
        elif 40 <= marks <= 60:
            grade = "D"
        elif 0 <= marks < 40:
            grade = "FAIL"
        else:
            print("Invalid Marks")
        grades = grade

        dynamic_dicts = {
            'roll_no': roll_no,
            'name': name,
            'marks': marks,
            'grade': grades,
        }
        dynamic_dict[key] = dynamic_dicts

    # Display the dynamically created dictionary
    print("Dynamically created dictionary:")
    print(dynamic_dict)

    update = input("Enter 'yes' to update student's marks or enter 'no': ")
    if update == 'yes':
        student_to_update = input("Enter the name of the student whose marks you want to edit: ")
        if student_to_update in dynamic_dicts:
            new_marks = int(input("Enter new marks for updatation: "))
            if 90 < new_marks <= 100:
                grade = "A"
            elif 80 < new_marks <= 90:
                grade = "B"
            elif 60 < new_marks <= 80:
                grade = "C"
            elif 40 <= new_marks <= 60:
                grade = "D"
            elif 0 <= new_marks < 40:
                grade = "FAIL"
            else:
                print("Invalid Marks")
            grades = grade
            dynamic_dict[student_to_update]['marks'] = new_marks
            dynamic_dict[student_to_update]['grade'] = grades
        else:
            print("Student not found")

    for key, data in dynamic_dict.items():
        print(f"{key} : {data}")

if __name__ == "__main__":
    main()


