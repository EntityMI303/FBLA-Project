bananas = "1.99"
apples = "0.99"
oranges = "0.79"
dragon_fruit = "2.49"
watermelon = "4.99"
papaya = "4.49"
squash = "3.99"

def shopping():
    print("Welcome to the fruit store!")
    print("Here are the available fruits and their prices:")
    print(f"Bananas: ${bananas}")
    print(f"Apples: ${apples}")
    print(f"Oranges: ${oranges}")
    print(f"Dragon Fruit: ${dragon_fruit}")
    print(f"Watermelon: ${watermelon}")
    print(f"Papaya: ${papaya}")
    print(f"Squash: ${squash}")

    total_cost = 0.0
    banana_qty = int(input("How many bananas would you like to buy? "))
    if banana_qty < 0:
        print("Invalid quantity for bananas. Please enter a non-negative number.")
        return
    total_cost += float(bananas) * banana_qty
    apple_qty = int(input("How many apples would you like to buy? "))
    if apple_qty < 0:
        print("Invalid quantity for apples. Please enter a non-negative number.")
        return
    total_cost += float(apples) * apple_qty
    orange_qty = int(input("How many oranges would you like to buy? "))
    if orange_qty < 0:
        print("Invalid quantity for oranges. Please enter a non-negative number.")
        return
    total_cost += float(oranges) * orange_qty
    dragon_fruit_qty = int(input("How many dragon fruits would you like to buy? "))
    if dragon_fruit_qty < 0:
        print("Invalid quantity for dragon fruits. Please enter a non-negative number.")
        return
    total_cost += float(dragon_fruit) * dragon_fruit_qty
    watermelon_qty = int(input("How many watermelons would you like to buy? "))
    if watermelon_qty < 0:
        print("Invalid quantity for watermelons. Please enter a non-negative number.")
        return
    total_cost += float(watermelon) * watermelon_qty
    papaya_qty = int(input("How many papayas would you like to buy? "))
    if papaya_qty < 0:
        print("Invalid quantity for papayas. Please enter a non-negative number.")
        return
    total_cost += float(papaya) * papaya_qty
    squash_qty = int(input("How many squashes would you like to buy? "))
    if squash_qty < 0:
        print("Invalid quantity for squashes. Please enter a non-negative number.")
        return
    total_cost += float(squash) * squash_qty

    retail_price = total_cost * 1.2  # Adding a 20% markup for retail price
    print(f"The retail price of your total purchase is: ${retail_price:.2f}")
    total_cost += retail_price  # Adding retail price to total cost

    tax_rate = 0.07  # Assuming a tax rate of 7%
    tax = total_cost * tax_rate
    if tax < 0:
        print("The tax cannot be negative. Please check your total cost.")
        return
    print(f"The tax on your total purchase is: ${tax:.2f}")
    total_cost += tax  # Adding tax to total cost

    discount_rate = float(input("How much would you like to discount? It must be between 0 and 1"))  # Assuming a discount rate of 10%
    discount = total_cost * discount_rate
    if discount < 0:
        print("The total cost cannot be negative. Please check your quantities.")
        return
    print(f"The discount on your total purchase is: ${discount:.2f}")
    total_cost -= discount  # Applying discount to total cost

    print(f"Your total cost after applying the discount is: ${total_cost:.2f}")
    if total_cost < 0:
        print("The total cost cannot be negative. Please check your quantities.")
        return
    if total_cost == 0:
        print("You have not purchased any items. The total cost is zero. Consider buying some fruits next time.")
        return
    if total_cost <= 20 :
        print("You have spent a little! Consider buying more fruits next time.")
    if total_cost <= 50:
        print("Wow! You have spent a lot! Thank you for your purchase.")
    if total_cost <= 100:
        print("You are a big spender! Thank you for your generous purchase.")
    if total_cost <= 500:
        print("You are a super big spender! Thank you for your amazing purchase.")
    if total_cost <= 1000:
        print("You are a mega big spender! Thank you for your incredible purchase.")
    if total_cost > 1000:
        print("You are a billionaire! Thank you for your extraordinary purchase.")

    print(f"Your total cost is: ${total_cost:.2f}")

    print("Thank you for shopping with us!")

shopping()