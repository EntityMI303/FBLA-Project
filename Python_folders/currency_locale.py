import locale 

sample_amount = float(input("Enter a sample amount: "))
if sample_amount < 0:
    print("The sample amount cannot be negative. Please enter a non-negative number.")
    exit()

country_option = input("Enter your country(e.g en_US):")

locale.setLocale(locale.LC_ALL, country_option)
print(locale.currency(sample_amount, grouping=True))