class StudentInfo:
    student_count = 0

    def __init__(self):
        self.name = input("enter the student name :")
        self.roll_no = int(input("Enter the roll no :"))
        # self.name = name
        # self.roll_no = roll_no

    def collect_info(self):
        print(f'Name = {self.name} | Roll No = {self.roll_no}')


class StudentMarks(StudentInfo):

    def __init__(self):
        self.roll_no = int(input("Enter the roll no :"))
        self.marks = int(input("Enter marks for student 1:"))
        self.grade = input("Enter grade for student 1 :")
    
    def collect_marks(self):
        print(f'Roll No = {self.roll_no} | Marks = {self.marks} | grade = {self.grade}')
        

        




# name = input("Enter the name for student 1:")
# roll_no = int(input("Enter the roll no for student 1 :"))
# marks = int(input("Enter marks for student 1:"))
# grade = input("Enter grade for student 1 :")
std1 = StudentInfo()
std1 = StudentMarks()
std1.collect_info()


name = input("Enter the name :")
roll_no = int(input("Enter the roll no"))
marks = int(input("Enter marks for student 1:"))
grade = input("Enter grade for student 1 :")
std2 = StudentInfo(name , roll_no)
std2 = StudentMarks(roll_no, marks, grade)

# std3 = StudentInfo()
# std4 = StudentInfo()



std1.collect_info()

std2.collect_info()
# std3.collect_info()
# std4.collect_info()

