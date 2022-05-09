# -*- coding: utf-8 -*-
"""
Created on Tue May  3 16:50:29 2022

@author: Sinead K
"""

# Size prices
small_price = 2.00
medium_price = 3.00
large_price = 4.00

# Coffee prices
brewed_price = 0.00
espresso_price = 0.50
cold_brew_price = 1.00

# Flavour prices
none_price = 0.00
flavour_price = 0.50

# Start price at 0
price = 0.00
float_price = float(price)

size = input("Please choose a cup size (small/medium/large) ")
size = size.lower()

if size == "small":
    price = price + small_price
elif size == "medium":
    price = float_price + medium_price
elif size == "large":
    price = float_price + large_price
else:
    print("Coffee size not found")
    
coffee = input("Please choose what kind of coffee you would like (brewed/espresso/cold brew) ")
coffee = coffee.lower()

if coffee == "brewed":
    price = price + brewed_price
elif coffee == "espresso":
    price = price + espresso_price
elif coffee == "cold brew":
    price = price + cold_brew_price
else:
    print("Coffee was not found")
    
flavour = input("Please choose what flavour syrup you would like (hazelnut/vanilla/caramel/no) ")
flavour = flavour.lower()

condition1 = (flavour == "hazelnut" or flavour == "vanilla" or flavour == "caramel")
condition2 = (flavour == "no")

if condition1 == True:
    price = price + flavour_price
elif condition2 == True:
    price = price + none_price
else:
    print("Flavour not found")
    
print("Your order consists of a ", size, coffee, "coffee with ",flavour, "syrup.")

# Calculate the tip
tip = (float(price) / 100) * 15

tipped_price = price + tip
total_cost = round(tipped_price, 2)

print("Your total is $", price)
print("Your total after tips is $", total_cost)