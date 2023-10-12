class StudentName:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

class StudentMark:
    def __init__(self, roll_no, marks_subject1, marks_subject2, marks_subject3):
        self.roll_no = roll_no
        self.marks_subject1 = marks_subject1
        self.marks_subject2 = marks_subject2
        self.marks_subject3 = marks_subject3

def main():
    # Get the number of students from the user
    num_students = int(input("Enter the number of students: "))

    students = []  # List to store student objects

    # Input student details
    for i in range(num_students):
        name = input(f"Enter the name of student {i + 1}: ")
        roll_no = input(f"Enter the roll number of student {i + 1}: ")
        marks_subject1 = float(input(f"Enter marks for subject 1 of student {i + 1}: "))
        marks_subject2 = float(input(f"Enter marks for subject 2 of student {i + 1}: "))
        marks_subject3 = float(input(f"Enter marks for subject 3 of student {i + 1}: "))

        # Create StudentName and StudentMark objects and store them in the list
        name_obj = StudentName(name, roll_no)
        mark_obj = StudentMark(roll_no, marks_subject1, marks_subject2, marks_subject3)
        students.append((name_obj, mark_obj))

    # Display student details
    for i, (name_obj, mark_obj) in enumerate(students):
        print(f"Student {i + 1} Details:")
        print(f"Name: {name_obj.name}")
        print(f"Roll Number: {name_obj.roll_no}")
        print(f"Marks (Subject 1): {mark_obj.marks_subject1}")
        print(f"Marks (Subject 2): {mark_obj.marks_subject2}")
        print(f"Marks (Subject 3): {mark_obj.marks_subject3}")
        print()

if __name__ == "__main__":
    main()
