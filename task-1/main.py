def get_int_input(message):
    user_input = int(input(message))

    if user_input < 0:
        print("Input must be positive number")
        return get_int_input(message)
    
    return user_input


def get_char_input(message):
    return input(message)


def print_triangle_star_pattern_a():
    print("========== 1. Print Triangle Star Pattern A ==========") 
    print_newlines(1)
    triangle_height = get_int_input("Enter the height of the triangle: ")
    print_newlines(1)

    for i in range(1, triangle_height + 1):
        print("*" * i)


def print_triangle_star_pattern_b():
    print("========== 2. Print Triangle Star Pattern B ==========")
    print_newlines(1)
    triangle_height = get_int_input("Enter the height of the triangle: ")
    print_newlines(1)

    for i in range(triangle_height, 0, -1):
        print("*" * i)


def print_triangle_star_pattern_c():
    print("========== 3. Print Triangle Star Pattern C ==========")
    print_newlines(1)
    triangle_height = get_int_input("Enter the height of the triangle: ")
    print_newlines(1)

    for i in range(1, triangle_height + 1):
        spaces = " " * (triangle_height - i)
        stars = "*" * i
        print(spaces + stars)


def print_triangle_star_pattern_d():
    print("========== 4. Print Triangle Star Pattern D ==========")
    print_newlines(1)
    triangle_height = get_int_input("Enter the height of the triangle (Must be odd number): ")
    print_newlines(1)

    if triangle_height % 2 == 0:
        print("Height must be odd number")
        return
    
    for i in range(1, triangle_height + 1, 2):
        spaces = " " * ((triangle_height - i) // 2)
        stars = "*" * i
        print(spaces + stars)


def print_fibonacci_sequence():
    print("========== 5. Print Fibonacci Sequence ==========")
    print_newlines(1)
    n = get_int_input("Enter the number of terms: ")
    print_newlines(1)

    first_term, second_term = 0, 1
    count = 0

    print("[", end=' ')
    if n == 1:
        print(first_term)
    else:
        while count < n:
            if count == n - 1:
                print(first_term, end=' ')
            else:
                print(first_term, end=', ')

            nth_term = first_term + second_term
            first_term = second_term
            second_term = nth_term
            count += 1
    print("]")


def print_reversed_array():
    print("========== 6. Reverse an array ==========")
    print_newlines(1)
    array_of_numbers = get_char_input("Enter array of numbers(example [4, 2, 8, 5, 1]): ")
    print_newlines(1)

    list_of_numbers = string_to_list(array_of_numbers)
    reversed_list = list_of_numbers[::-1]
    print(f"Reversed array is {reversed_list}")
    

def count_and_print_only_duplicate_numbers():
    print("========== 7. Count and print only duplicate numbers ==========")
    print_newlines(1)
    array_of_numbers = get_char_input("Enter array of numbers (example [4, 2, 2, 8, 5, 1, 2, 4]): ")
    print_newlines(1)
    list_of_numbers = string_to_list(array_of_numbers)

    duplicate_numbers = get_duplicate_numbers(list_of_numbers)
    unique_elements = remove_duplicates(duplicate_numbers)

    if len(unique_elements) == 0:
        print("There is no duplicate number")
    else:
        for number in unique_elements:
            print(f"{number} appears {list_of_numbers.count(number)} times")


def print_largest_and_smallest_number():
    print("========== 8. Print largest and smallest number ==========")
    print_newlines(1)
    array_of_numbers = get_char_input("Enter array of numbers (example [4, 2, 8, 5, 1]): ")
    print_newlines(1)
    list_of_numbers = string_to_list(array_of_numbers)

    largest_number = max(list_of_numbers)
    smallest_number = min(list_of_numbers)
    print(f"Largest number is {largest_number}")
    print(f"Smallest number is {smallest_number}")


def string_to_list(input_string):
    cleaned_string = input_string.strip("[]")
    elements = cleaned_string.split(", ")
    result_list = [int(element) for element in elements]
    return result_list


def get_duplicate_numbers(list_of_numbers):
    duplicate_numbers = []
    for number in list_of_numbers:
        if list_of_numbers.count(number) > 1:
            duplicate_numbers.append(number)
    return duplicate_numbers


def remove_duplicates(list_of_numbers):
    unique_elements = []
    for number in list_of_numbers:
        if number not in unique_elements:
            unique_elements.append(number)
    return unique_elements


def process_function(number_of_function):
    print_newlines(3)
    functions = {
        1: print_triangle_star_pattern_a,
        2: print_triangle_star_pattern_b,
        3: print_triangle_star_pattern_c,
        4: print_triangle_star_pattern_d,
        5: print_fibonacci_sequence,
        6: print_reversed_array,
        7: count_and_print_only_duplicate_numbers,
        8: print_largest_and_smallest_number,
    }
    if number_of_function in functions:
        functions[number_of_function]()
    else:
        print("Function not found ...")


def print_menus():
    print("========== List of Functions ==========")
    print_newlines(1)
    menus = {
        1: "Print triangle star pattern a",
        2: "Print triangle star pattern b",
        3: "Print triangle star pattern c",
        4: "Print triangle star pattern d",
        5: "Print fibonacci sequence",
        6: "Print reversed an array",
        7: "Count and print only duplicate numbers",
        8: "Print largest and smallest number",
    }
    for key, value in menus.items():
        print(f"{key}. {value}")


def print_newlines(number_of_newlines):
    for i in range(number_of_newlines):
        print()


if __name__ == "__main__":
    print_menus()
    print_newlines(1)

    number_of_function = get_int_input("Enter number of function (1 - 8): ") 
    process_function(number_of_function)