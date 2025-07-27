def perform_operation( num1, num2, operation):
   
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