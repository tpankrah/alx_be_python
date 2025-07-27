#Requirements for arithmetic_operations.py:
#Function Definition:
#Define a function named perform_operation.
#Parameters: num1 (float), num2 (float), and operation (string). 
# The operation parameter accepts four possible values: 'add', 'subtract', 'multiply', or 'divide'.
#The function should execute the arithmetic operation based on the operation parameter 
# and the numerical values provided.
#For division, include handling for division by zero, 
# returning a specific message or value that your main.py script can recognize and display appropriately.
#Return the result of the arithmetic operation.

def perform_operation( num1 :float, num2 :float, operation :str):
   
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                return "Sorry, division by zero no allowed"
            else:
                return num1 / num2
        case _:
            return 'operation is incorrect'