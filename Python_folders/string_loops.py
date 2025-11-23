s1 = input("Enter a string: ")
s2 = input("Enter a string: ")
s3 = input("Enter a string: ")
strings = [s1, s2, s3]

print("Calculating the length of each string...")
for x in strings:
    print(f"The length of '{x}' is {len(x)} characters.")
    print("The smallest character in the string is:", min(x))
    print("The largest character in the string is:", max(x))

print("All strings have been processed.")
print("Thank you for using the String Length Calculator!")
