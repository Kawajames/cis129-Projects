# cis129_lab03_coffeeShop.py
# Created by Dakota Kartchner for CIS129 Prog and Problem Solving

coffee_price = 5    # $5 for each coffee
muffin_price = 4    # $4 for each muffin
tea_price = 3       # $3 for each tea
cookie_price = 2    # $2 for each cookie
tax_rate = 0.06     # 0.06 is equal to 6%
#This shows the cost of each item

coffees_bought = int(input("How many coffees were bought?"))
muffins_bought = int(input("How many muffins were bought?"))
teas_bought = int(input("How many teas were bought?"))
cookies_bought = int(input("How many cookies were bought?"))
# Ask the user for the quantity of each item bought

coffee_total = coffees_bought * coffee_price
muffin_total = muffins_bought * muffin_price
tea_total = teas_bought * tea_price
cookie_total = cookies_bought * cookie_price
# Calculate totals for each item

subtotal = coffee_total + muffin_total + tea_total + cookie_total
total_tax = subtotal * tax_rate
total_price = subtotal + total_tax
# Calculate subtotal, tax, and total price


# Print the formatted receipt
print("***************************************")
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
print(coffees_bought)
print("Number of muffins bought?")
print(muffins_bought)
print("Number of teas bought?")
print(teas_bought)
print("Number of cookies bought?")
print(cookies_bought)
print("***************************************")
print(" ")
print("***************************************")
print("My Coffee and Muffin Shop Receipt")
print(str(coffees_bought) + " Coffee at $" + str(coffee_price) + " each: $" + str(coffee_total) + ".00")
print(str(muffins_bought) + " Muffins at $" + str(muffin_price) + " each: $" + str(muffin_total) + ".00")
print(str(teas_bought) + " Tea at $" + str(tea_price) + " each: $" + str(tea_total) + ".00")
print(str(cookies_bought) + " Cookies at $" + str(cookie_price) + " each: $" + str(cookie_total) + ".00")
print("6% tax: $" + str(total_tax))
print("---------")
print(("Total: $") + str(total_price))
print("***************************************")
print("Thank you for visiting, Come Again!")
