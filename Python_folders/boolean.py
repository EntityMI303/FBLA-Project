#This program will review true and false values and print the result.

x = "true"
y = "false"
ques = input("Is the water colorless?")

def boolean_values(x, y):
    return (x == "true") and (y == "false")

def boolean_question(ques):
    if ques == "Yes":
        return x
    elif ques == "No":
        return y
    else: 
        return "Invalid input. Please answer with 'Yes' or 'No'."
    
print("The answer is:", boolean_question(ques))

if boolean_question(ques) == x:
    print("Good Job!")
elif boolean_question(ques) == y:
    print("Wrong!")
else:
    print("Please answer with 'Yes' or 'No'.")
# This program will review true and false values and print the result.
