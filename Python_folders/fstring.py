import random

unit_price = 49.99
quantity = int(input("Enter the quantity of items: "))
if quantity <= 0:
    print("Quantity must be a positive integer.")
    exit()
print(f"Subtotal: ${quantity * unit_price:.2f}")

tax_rates = [0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.11, 0.12, 0.13, 0.14, 
             0.15, 0.16, 0.17, 0.18, 0.19, 0.20, 0.21, 0.22, 0.23, 0.24, 
             0.25, 0.26, 0.27, 0.28, 0.29, 0.30, 0.31, 0.32, 0.33, 0.34, 
             0.35, 0.36, 0.37, 0.38, 0.39, 0.40]

print("Calculating tax for a random rate:")

for i in range(1):  # single iteration
    tax_rate = random.choice(tax_rates)
    tax = quantity * unit_price * tax_rate
    print(f"Tax at {tax_rate * 100:.0f}%: ${tax:.2f}")

print(f"Total cost including tax: ${(quantity * unit_price) + tax:.2f}")