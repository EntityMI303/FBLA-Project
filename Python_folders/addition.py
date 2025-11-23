#This program will add two numbers and print the result.
#This will also be used to add two letters and print the result.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

letter1 = input("Enter the first letter (A-Z): ").upper()
letter2 = input("Enter the second letter (A-Z): ").upper()

def add_numbers(num1, num2):
    return num1 + num2

def add_letters(letter1, letter2):
    return (ord(letter1) + ord(letter2) - ord('A'))

print("The sum of the two numbers is:", add_numbers(num1, num2))
print("The sum of the two letters is:", add_letters(letter1, letter2))
# Note: The letter addition logic is not standard and may not yield meaningful results.