print("Welcome to the Lens Calculator!")

s1 = input("Enter a string: ")
s2 = input("Enter a string: ")
s3 = input("Enter a string: ")

num1 = len(s1)
num2 = len(s2)
num3 = len(s3)
operator = input("Enter an operator: ")

def lens_calculator(num1, num2, num3, operator):
    if operator == "+":
        return num1 + num2 + num3
    elif operator == "-":
        return num1 - num2 - num3
    elif operator == "*":
        return num1 * num2 * num3
    elif operator == "/":
        if num2 != 0 and num3 != 0:
            return num1 / num2 / num3
        else:
            return "Division by zero is not allowed"
    else:
        return "Invalid operator"

result = lens_calculator(num1, num2, num3, operator)
print(f"The result of the operation is: {result}")
print("Thank you for using the Lens Calculator!")

