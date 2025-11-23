numbers = [1, -2, 3, -4, 5]
def abs_values(numbers):
    """Return a list of absolute values of the given numbers."""
    return [abs(num) for num in numbers]

def main():
    """Main function to demonstrate absolute values."""
    abs_list = abs_values(numbers)
    print("Original numbers:", numbers)
    print("Absolute values:", abs_list)

if __name__ == "__main__":
    main()