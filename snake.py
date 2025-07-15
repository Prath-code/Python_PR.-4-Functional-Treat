import numpy as np


def display_data_summary(data):
    print("Data Summary:")
    print(f" - Total elements: {len(data)}")
    print(f" - Minimum value: {min(data)}")
    print(f" - Maximum value: {max(data)}")
    print(f" - Sum of all values: {sum(data)}")
    print(f" - Average value: {sum(data) / len(data):.2f}")


def calculate_average(data):
    return sum(data) / len(data)


def display_builtin_functions(data):
    print("Built-in Functions:")
    print(f" - Sum: {sum(data)}")
    print(f" - Minimum: {min(data)}")
    print(f" - Maximum: {max(data)}")
    print(f" - Average: {calculate_average(data):.2f}")


def display_lambda_functions(data):
    avg = calculate_average(data)
    filtered_above = list(filter(lambda x: x > avg, data))
    filtered_below = list(filter(lambda x: x < avg, data))
    print("Lambda Functions:")
    print(f" - Values above average: {filtered_above}")
    print(f" - Values below average: {filtered_below}")


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def display_recursion():
    num = int(input("Enter a number to calculate its factorial: "))
    print(f"Factorial of {num} is: {factorial(num)}")
    num = int(input("Enter a number to calculate its Fibonacci sequence: "))
    print(f"Fibonacci of {num} is: {fibonacci(num)}")


def filter_by_threshold(data):
    threshold = float(
        input("Enter a threshold value to filter out data above this value: ")
    )
    filtered_data = list(filter(lambda x: x <= threshold, data))
    print(f"Filtered Data (values <= {threshold}): {filtered_data}")


def sort_data(data):
    choice = input(
        "Choose sorting option:\n1. Ascending\n2. Descending\nEnter your choice: "
    )
    if choice == "1":
        sorted_data = sorted(data)
    else:
        sorted_data = sorted(data, reverse=True)
    print(f"Sorted Data in {choice} order: {sorted_data}")


def display_multiple_values(data):
    print("Dataset Statistics:")
    print(f" - Minimum value: {min(data)}")
    print(f" - Maximum value: {max(data)}")
    print(f" - Sum of all values: {sum(data)}")
    print(f" - Average value: {calculate_average(data):.2f}")


def main():
    while True:
        print("\nWelcome to the Data Analyzer and Transformer Program")
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Display Factorial/Fibonacci (Recursion)")
        print("4. Filter Data by Threshold (Lambda Function)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Return Multiple Values)")
        print("7. Exit Program")
        choice = input("Please enter your choice: ")

        if choice == "1":
            data_input = input("Enter data for a 1D array (separated by spaces): ")
            data = [float(x) for x in data_input.split()]
            print("Data has been stored successfully!")
        elif choice == "2":
            display_data_summary(data)
        elif choice == "3":
            display_recursion()
        elif choice == "4":
            filter_by_threshold(data)
        elif choice == "5":
            sort_data(data)
        elif choice == "6":
            display_multiple_values(data)
        elif choice == "7":
            print(
                "Thank you for using the Data Analyzer and Transformer Program. Goodbye!"
            )
            break


if __name__ == "__main__":
    main()
