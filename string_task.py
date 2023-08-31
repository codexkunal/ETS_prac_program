str_line = input("Enter your string: ")

str_line = str_line[::-1]
print(str_line)
"""new_str = str_line
new_str = new_str[::-1]
print(new_str)"""

str_line.split(" ")
print(str_line)
lst = []
for i in range(len(str_line)):
        if str_line[i].isalpha():
            lst.append(str_line[i])
        elif i == " ":
            continue
print(lst)