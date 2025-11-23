first_name = input("Enter first name:")
middle_name = input("Enter middle name:")
if(not middle_name):
    middle_name = ""
last_name = input("Enter last name:")


def get_full_name():
    output = f"{first_name}\n{middle_name}\n{last_name}".strip()
    print(output)

if __name__ == "__main__":
    get_full_name()