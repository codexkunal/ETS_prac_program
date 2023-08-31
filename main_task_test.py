
"""def calculate(*args):
    if len(args) == 1:
        print("List:", args[0])
    elif len(args) == 2:
        combined_list = args[0] + args[1]
        max_num = max(combined_list)
        min_num = min(combined_list)
        print("Combined List:", combined_list)
        print("Maximum:", max_num)
        print("Minimum:", min_num)
    elif len(args) >= 3:
        combined_list = []
        for lst in args:
            combined_list.extend(lst)
        squared_elements = list(map(lambda x: x ** 2, combined_list))
        print("Combined List:", combined_list)
        print("Squared elements:", squared_elements)
    else:
        print("Invalid number of lists provided.")

def create_list():
    num_lists = int(input("Enter the number of lists you want to create: "))
    all_lists = []

    for _ in range(num_lists):
        list_elements = []
        list_size = int(input(f"Enter the number of elements for list {_ + 1}: "))

        for j in range(list_size):
            element = int(input(f"Enter element {j + 1} for list {_ + 1}: "))
            list_elements.append(element)

        all_lists.append(list_elements)

    return all_lists

lists = create_list()

calculate(*lists)
"""

def calculate_sum(*args):
    combined_list = []
    
    for inner_list in args:
        combined_list.extend(inner_list)
    
    total_sum = sum(combined_list)
    return total_sum

def main():
    outer_list = []
    
    for _ in range(3):
        inner_list = []
        num_elements = int(input("Enter the number of elements for the inner list: "))
        
        for _ in range(num_elements):
            element = int(input("Enter an integer element: "))
            inner_list.append(element)
        
        outer_list.append(inner_list)
    
    concatenated_sum = calculate_sum(*outer_list)
    print("Concatenated List:", outer_list)
    print("Sum of all elements:", concatenated_sum)

if __name__ == "__main__":
    main()

"""def calculate(*args):
    if len(args) == 1:
        print("List:", args[0])
    elif len(args) == 2:
        combined_list = args[0] + args[1]
        max_num = max(combined_list)
        min_num = min(combined_list)
        print("Combined List:", combined_list)
        print("Maximum:", max_num)
        print("Minimum:", min_num)
    elif len(args) >= 3:
        combined_list = []
        for lst in args:
            combined_list.extend(lst)
        squared_elements = list(map(lambda x: x ** 2, combined_list))
        print("Combined List:", combined_list)
        print("Squared elements:", squared_elements)
    else:
        print("Invalid number of lists provided.")

def create_list():
    num_lists = int(input("Enter the number of lists you want to create: "))
    all_lists = []

    for _ in range(num_lists):
        list_elements = []
        list_size = int(input(f"Enter the number of elements for list {_ + 1}: "))

        for j in range(list_size):
            element = int(input(f"Enter element {j + 1} for list {_ + 1}: "))
            list_elements.append(element)

        all_lists.append(list_elements)

    return all_lists

lists = create_list()

calculate(*lists)
"""

def calculate_sum(*args):
    combined_list = []
    
    for inner_list in args:
        combined_list.extend(inner_list)
    
    total_sum = sum(combined_list)
    return total_sum

def main():
    outer_list = []
    
    for _ in range(3):
        inner_list = []
        num_elements = int(input("Enter the number of elements for the inner list: "))
        
        for _ in range(num_elements):
            element = int(input("Enter an integer element: "))
            inner_list.append(element)
        
        outer_list.append(inner_list)
    
    concatenated_sum = calculate_sum(*outer_list)
    print("Concatenated List:", outer_list)
    print("Sum of all elements:", concatenated_sum)

if __name__ == "__main__":
    main()

