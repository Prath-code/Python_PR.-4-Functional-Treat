# Functional Treat: Data Analyzer and Transformer

## Objective

Functional Treat is a Python program that allows users to analyze and transform data in one-dimensional (1D) and two-dimensional (2D) arrays (using lists). The project demonstrates proficiency in built-in functions, user-defined functions, recursion, lambda functions, global variables, returning multiple values, and sorting/transforming list-based data collections. The program features a menu-driven interface for selecting various data transformation and analysis options.

## Features

- **Built-in Functions:**  
  - Use built-in functions like `len()`, `sum()`, `min()`, `max()`, etc., to display basic statistics about the array data.

- **User-defined Functions (UDF):**  
  - Create specific functions for tasks such as calculating the average, finding duplicates, or displaying unique values.

- **`*args`, `**kwargs`, and `__doc__`:**  
  - Use `*args` to accept multiple values and display them.  
  - Use `**kwargs` to print key-value pairs as a summary of dataset characteristics.  
  - Use `__doc__` in each function to provide a description and print this information in the main menu.

- **Recursion:**  
  - Implement a recursive function to calculate the factorial of a number or the Fibonacci sequence, showcasing recursion in a data analysis context.

- **Lambda Functions:**  
  - Use a lambda function to filter out values above or below a threshold, specified by the user.  
  - Apply lambda functions in conjunction with `map()` and `filter()` to manipulate list data.

- **Global Keyword:**  
  - Use a global variable to store a dataset summary (e.g., total number of values and overall mean) that can be accessed across different functions.

- **Return Multiple Values:**  
  - Create a function that returns multiple statistics about the dataset, such as minimum, maximum, and average values, which are then displayed individually in the main program.

- **1D and 2D Array (List):**  
  - Allow the user to input a 1D list or a 2D list (nested list).  
  - Display the 2D list in a formatted grid structure.

- **Sorting Collection Data Types:**  
  - Use the `sort()` method on a 1D list to arrange values in ascending or descending order.  
  - Use the `sorted()` function to sort rows in a 2D list, showcasing the difference between in-place sorting and returning a new sorted list.

## Program Flow

1. **Welcome and Instructions:**  
   - Displays a welcome message and overview.

2. **Data Input:**  
   - Prompts user to enter data for a 1D or 2D array (manually or using sample data).

3. **Menu-Driven Options:**  
   - Display Data Summary (Built-in Functions)
   - Calculate Factorial (Recursion)
   - Filter Data by Threshold (Lambda Function)
   - Sort Data
   - Display Dataset Statistics (Return Multiple Values)
   - Exit Program

## Example Console Interaction

```
Welcome to the Data Analyzer and Transformer Program

Main Menu:
1. Input Data
2. Display Data Summary (Built-in Functions)
3. Calculate Factorial (Recursion)
4. Filter Data by Threshold (Lambda Function)
5. Sort Data
6. Display Dataset Statistics (Return Multiple Values)
7. Exit Program
Please enter your choice: 1

Step 1: Input Data
Please enter your choice: 1
Enter data for a 1D array (separated by spaces):
34 12 56 78 43 21 90
Data has been stored successfully!

Step 2: Display Data Summary (Built-in Functions)
Please enter your choice: 2
Data Summary:
- Total elements: 7
- Minimum value: 12
- Maximum value: 90
- Sum of all values: 334
- Average value: 47.71

Step 3: Calculate Factorial (Recursion)
Please enter your choice: 3
Enter a number to calculate its factorial: 5
Factorial of 5 is: 120

Step 4: Filter Data by Threshold (Lambda Function)
Please enter your choice: 4
Enter a threshold value to filter out data above this value: 50
Filtered Data (values >= 50):
56, 78, 90

Step 5: Sort Data
Please enter your choice: 5
Choose sorting option:
1. Ascending
2. Descending
Enter your choice: 1
Sorted Data in Ascending Order:
12, 21, 34, 43, 56, 78, 90

Step 6: Display Dataset Statistics (Return Multiple Values)
Please enter your choice: 6
Dataset Statistics:
- Minimum value: 12
- Maximum value: 90
- Sum of all values: 334
- Average value: 47.71

Step 7: Exit Program
Please enter your choice: 7
Thank you for using the Data Analyzer and Transformer Program. Goodbye!
```

## How to Run

1. Ensure you have Python 3.x installed.
2. Run the program:
   ```
   python snake.py
   ```

## Assumptions

- User can input either a 1D or 2D list (array).
- Data is entered as space-separated values for 1D arrays, or as rows for 2D arrays.
- Thresholds and other parameters are provided by the user as prompted.

## Project Structure

- `snake.py` — Main program file containing all logic.
- `README.md` — Project documentation.

## Notes

- All code is original and written for educational purposes.
- No external libraries are required.
- Each function includes a `__doc__` string describing its purpose.
- Clear instructions are provided within the menu interface.
