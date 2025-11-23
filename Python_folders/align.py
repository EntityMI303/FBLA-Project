unit_price = 49.99
quantity = int(input("Enter the quantity: "))
if quantity < 0:
    print("Invalid quantity. Please enter a non-negative number.")
sales_tax_rate = 0.09
subtotal = unit_price * quantity