# Open necessary files for writing
studentinfo_file = open("StudentInfo.txt", "a+")
studentmarks_file = open("StudentMarks.txt", "a+")
a_grade_file = open("A grade.txt", "a+")
b_grade_file = open("B grade.txt", "a+")
c_grade_file = open("C grade.txt", "a+")

# Define the StudentInfo class to handle student information
class StudentInfo:
    def __init__(self, rollno, name):
        self.rollNo = rollno
        self.name = name
        studentinfo_file.write(f"{self.rollNo}-{self.name}\n")

# Define the StudentMarks class to handle student marks
class StudentMarks:
    def __init__(self, rollno, marks_one, marks_two, marks_three):
        self.rollno = rollno
        self.marks1 = marks_one
        self.marks2 = marks_two
        self.marks3 = marks_three
        studentmarks_file.write(f"{self.rollno}-{self.marks1}-{self.marks2}-{self.marks3}\n")

# Define the main class to manage the program
class main:
    def __init__(self):
        marks_lis = []
        info_lis = []
        info_sorted = []
        marks_sorted = []
        a_grade_list = []
        b_grade_list = []
        c_grade_list = []
        info_dict = {}

        # Input the number of students
        no_of_student = int(input("Enter the number of students: "))
        for i in range(no_of_student):
            rollno = input(f"Enter the roll number of Student {i+1}: ")
            name = input(f"Enter the name of Student {i+1}: ")
            marks_1 = input(f"Enter Marks 1 of Student {i+1}: ")
            marks_2 = input(f"Enter Marks 2 of Student {i+1}: ")
            marks_3 = input(f"Enter Marks 3 of Student {i+1}: ")
            
            # Create instances of StudentInfo and StudentMarks classes to record the data
            info = StudentInfo(rollno, name)
            marks = StudentMarks(rollno, marks_1, marks_2, marks_3)
        
        # Close the studentinfo_file and studentmarks_file before reading
        studentinfo_file.close()
        studentinfo_read = open("StudentInfo.txt", 'r')
        studentinfo_contents = studentinfo_read.readlines()
        
        studentmarks_file.close()
        studentmarks_read = open("StudentMarks.txt", 'r')
        studentmarks_contents = studentmarks_read.readlines()

        # Process student information and create a dictionary
        for i in range(len(studentinfo_contents)):
            info_length = len(studentinfo_contents[i])
            remove_newline = studentinfo_contents[i][:info_length - 1]
            info_lis.append(remove_newline)
        
        for i in range(len(info_lis)):
            info_sorted = info_lis[i].split("-")
            for j in range(len(info_sorted) - 1):
                roll = info_sorted[j]
                name_1 = info_sorted[j+1]
                info_dict[str(roll)] = name_1

        # Process student marks
        for i in range(len(studentmarks_contents)):
            marks_length = len(studentmarks_contents[i])
            remove_newline = studentmarks_contents[i][:marks_length - 1]
            marks_lis.append(remove_newline)

        for i in range(len(marks_lis)):
            marks_sorted = marks_lis[i].split("-")

            # Check if the length of marks_sorted is not divisible by 4, skip this iteration
            if len(marks_sorted) % 4 != 0:
                continue

            for j in range(0, len(marks_sorted), 4):  # Iterate in groups of 4
                roll_no = marks_sorted[j]
                marks1 = marks_sorted[j + 1]
                marks2 = marks_sorted[j + 2]
                marks3 = marks_sorted[j + 3]

                # Calculate aggregated_score and average here
                aggregated_score = int(marks1) + int(marks2) + int(marks3)
                average = int(aggregated_score / 3)

                # Classify students into A, B, and C grades based on their averages
                if average <= 100 and average > 80:
                    a_grade_list.append((roll_no, average))
                    a_grade_list.sort()
                    # a_grade_list.reverse()
                elif average <= 80 and average > 60:
                    b_grade_list.append((roll_no, average))
                    b_grade_list.sort()
                    #b_grade_list.reverse()
                elif average <= 60 and average > 40:
                    c_grade_list.append((roll_no, average))
                    c_grade_list.sort()
                    #c_grade_list.reverse()

        # Write the results to respective grade files
        for i in range(len(a_grade_list)):
            a_grade_file.write(f"{a_grade_list[i][0]}-{info_dict[a_grade_list[i][0]]}-{a_grade_list[i][1]}\n")

        for i in range(len(b_grade_list)):
            b_grade_file.write(f"{b_grade_list[i][0]}-{info_dict[b_grade_list[i][0]]}-{b_grade_list[i][1]}\n")

        for i in range(len(c_grade_list)):
            c_grade_file.write(f"{c_grade_list[i][0]}-{info_dict[c_grade_list[i][0]]}-{c_grade_list[i][1]}\n")


        # Close all open files
        studentinfo_read.close()
        studentmarks_read.close()
        a_grade_file.close()
        b_grade_file.close()
        c_grade_file.close()

if __name__ == '__main__':
    main()