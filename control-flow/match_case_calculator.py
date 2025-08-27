Objective: Learn to use Match Case statements for handling multiple operations in a simple calculator program.

Task Description:

Develop a Python script named match_case_calculator.py. This calculator will prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division). The script will then perform the selected operation using a Match Case statement and display the result.

Instructions:

Prompt for User Input:

Ask the user to input two numbers (one at a time) using: Enter the first number: and Enter the second number:
Make sure you use num1 and num2 for first and second numbers
Ask for the type of operation they’d like to perform: Choose the operation (+, -, *, /):.
Perform the Calculation Using Match Case:

Implement a Match Case statement that executes the chosen operation based on the user’s input.
For addition (+), subtract (-), multiply (*), and divide (/).
Ensure to handle the division by zero case gracefully, displaying a message if the user tries to divide by zero.
Output the Result:

Display the result of the operation in a user-friendly message, e.g., The result is [result].
Example Interaction:

Enter the first number: 10
Enter the second number: 5
Choose the operation (+, -, *, /): *
The result is 50.
Or, for a division by zero scenario:

Enter the first number: 10
Enter the second number: 0
Choose the operation (+, -, *, /): /
Cannot divide by zero.
Repo:

GitHub repository: alx_be_python
Directory: control-flow
File: match_case_calculator.py