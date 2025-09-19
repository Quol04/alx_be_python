# Develop a Python script named match_case_calculator.py. This calculator will prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division). 

num1 = int (input("Enter the first number: "))

num2 = int (input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    case _:
        result = "Invalid operation"

print("The Result is:", result)