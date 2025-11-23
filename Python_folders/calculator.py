#This program will act as an calculator and print the result.

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
operation = input("Enter an operation from this(+, -, *, /, %, **, //):")

def calculator(x, y, operation):
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/':
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero."
    elif operation == '%':
        return x % y
    elif operation == '**':
        return x ** y
    elif operation == '//':
        if y != 0:
            return x // y
        else:
            return "Error: Division by zero."
    else:
        return "Invalid operation."
    
    
result = calculator(x, y, operation)
print(f"The result of {x} {operation} {y} is: {result}")

if result < 0:
    print("The result is negative.")
elif result == 0:
    print("The result is zero.")
elif result > 0:
    print("The result is positive.")

if result % 2 == 0:
    print("The result is even.")
else:
    print("The result is odd.")

