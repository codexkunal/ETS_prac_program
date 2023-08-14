<<<<<<< HEAD
lst_no = int(input("Enter the number of list you want to create: "))
lst = []
print(lst)
for i in range(lst_no):
    lst_element = []
    lst_no_ele = int(input(f"How many elements you want in the list{i+1}: "))
    for j in range(lst_no_ele):
        lst_items = int(input(f"Enter the elements {j+1} for list {i+1}: "))
        lst_element.append(lst_items)
    lst.append(lst_element)
print(f'list without any operation = {lst}')
#print(lst[0])
#print(*lst)

def calc(*args):
    if len(args) == 1:
      print(f'User has Entered only one list which is as follows  {args[0]}')
    elif len(args) == 2:
      combined_list = args[0] + args[1]
      max_list = max(combined_list)
      min_list = min(combined_list)
      print(f'Max value is = {max_list} and Min value is = {min_list}')
    elif len(args) == 3:
        combined_list1 = []
        for inner_list in args:
          combined_list1.extend(inner_list)
          total_sum = sum(combined_list1)
        #combined_list1 = sum(args[0]) + sum(args[1]) + sum(args[2])
        #combined_list1 = args[0] + args[1] + args[2]
        print(f'list after adding all elements = {total_sum   }')
    elif len(args) >= 3:
       combined_list2 = []
       for l in args:
          combined_list2.extend(l)
       print(f'List after combining all the other lists = {combined_list2}')
       squared_list = list(map(lambda x:x**2,combined_list2))
       odd_list = list(filter(lambda x : (x%2 != 0),combined_list2))
       print(f'squared of the combined list = {squared_list}')
       print(f'odd elements of the combined list = {odd_list}')


=======
lst_no = int(input("Enter the number of list you want to create: "))
lst = []
print(lst)
for i in range(lst_no):
    lst_element = []
    lst_no_ele = int(input(f"How many elements you want in the list{i+1}: "))
    for j in range(lst_no_ele):
        lst_items = int(input(f"Enter the elements {j+1} for list {i+1}: "))
        lst_element.append(lst_items)
    lst.append(lst_element)
print(f'list without any operation = {lst}')
#print(lst[0])
#print(*lst)

def calc(*args):
    if len(args) == 1:
      print(f'User has Entered only one list which is as follows  {args[0]}')
    elif len(args) == 2:
      combined_list = args[0] + args[1]
      max_list = max(combined_list)
      min_list = min(combined_list)
      print(f'Max value is = {max_list} and Min value is = {min_list}')
    elif len(args) == 3:
        combined_list1 = []
        for inner_list in args:
          combined_list1.extend(inner_list)
          total_sum = sum(combined_list1)
        #combined_list1 = sum(args[0]) + sum(args[1]) + sum(args[2])
        #combined_list1 = args[0] + args[1] + args[2]
        print(f'list after adding all elements = {total_sum   }')
    elif len(args) >= 3:
       combined_list2 = []
       for l in args:
          combined_list2.extend(l)
       print(f'List after combining all the other lists = {combined_list2}')
       squared_list = list(map(lambda x:x**2,combined_list2))
       odd_list = list(filter(lambda x : (x%2 != 0),combined_list2))
       print(f'squared of the combined list = {squared_list}')
       print(f'odd elements of the combined list = {odd_list}')


>>>>>>> 18c66ba77d6984aea84ee5a0f0822f57bba1190b
calc(*lst)