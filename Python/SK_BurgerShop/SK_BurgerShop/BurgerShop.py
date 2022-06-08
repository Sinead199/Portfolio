# -*- coding: utf-8 -*-
"""
Created on Tue May 10 11:00:19 2022

@author: Sinead K
"""

# Still in the progress of implementing a list to hold multiple instances of class objects eg 2x Burgers Ordered
#Will be completing this in my own time as I don't want to fall behind.

global total_price
total_price = 0.00

print("""--------------------------""") 
print("""Welcome to the Burger Shop""")
print("""--------------------------""")

# implement the classes listed below 
class FoodItem:
    food_type = None
    food_price = None
    def __init__(self, ft, fp):
        self.food_type = ft
        self.food_price = fp

    def display(self):
        print(self.food_type,self.food_price)  

class Burger(FoodItem):
    burger_meat = None
    burger_sauce = None
    def __init__(self, ft, fp, bm, bs):
        FoodItem.__init__(self, ft, fp)
        self.burger_meat = bm
        self.burger_sauce = bs
    def display(self):
        print(self.burger_meat, "Burger")
        print("Sauce:",self.burger_sauce)
        print("Price: €","{:.2f}".format(self.food_price))

class Side(FoodItem):
    side_type = None
    side_size = None
    def __init__(self, ft, fp, st, ss):
        FoodItem.__init__(self, ft, fp)
        self.side_type = st
        self.side_size = ss
    def display(self):
        print(self.side_size,self.side_type)
        print("Price: €","{:.2f}".format(self.food_price))
        
class Drink(FoodItem):
    drink_flav = None
    drink_size = None
    def __init__(self, ft, fp, df, ds):
        FoodItem.__init__(self, ft, fp)
        self.drink_flav = df
        self.drink_size = ds
    def display(self):
        print(self.drink_size,self.drink_flav)
        print("Price: €","{:.2f}".format(self.food_price))
        
class Combo(FoodItem):
    combo_size = None
    combo_drink = None
    def __init__ (self,ft,fp,cs,cd):
        FoodItem. __init__(self, ft, fp)
        self.combo_size = cs
        self.combo_drink = cd
        
    def display(self):
        print(self.combo_size,self.food_type)
        print("Signature Burger")
        print(self.combo_size,"Fries")
        print(self.combo_size,self.combo_drink)
        print("Price: €","{:.2f}".format(self.food_price))

class Order:
    order_name = None
    def __init__(self,on):
        self.order_name = on
    
    def display_order(self):
        print("\n Order Completed")
        print("\n Name on Order: ",self.order_name)
        print("\n Your Order is as Follows")
        print("-----------------------------")
        if 'bo' in globals():
            bo.display()
        else:
            print('No Burger')
        print("-----------------------------")
        if 'so' in globals():
            so.display()
        else:
            print('No Side')
        print("-----------------------------")
        if 'do' in globals():
            do.display()
        else:
            print('No Drink')
        print("-----------------------------")
        if 'co' in globals():
            co.display()
        else:
            print('No Combo meal')
        print("-----------------------------")
        total_float = "{:.2f}".format(total_price)
        print("Your Total is: €",total_float)


#ask user for input and store it in burger object 
def user_input_burger():
    meat_dict ={
        '1':'Chicken',
        '2':'Beef',
        '3':'Cancel Order'
    }
    
    global total_price

    for meat_id in meat_dict.keys():
        print(meat_id,meat_dict[meat_id]) 
        
    meat_input = int(input("\n Please select what meat you would like on your burger. "))
    if meat_input == 1:
        # Chicken Selected
        mi = meat_dict.get('1')
        print(mi, "Selected\n")
    elif meat_input == 2:
        # Beef Selected
        mi = meat_dict.get('2')
        print(mi, "Selected\n")
    elif meat_input == 3:
        return
    elif meat_input != "":
        print('Invalid option. Please enter a number between 1 and 3 inclusive.')
        
    sauce_dict ={
        '1':'Ketchup',
        '2':'Mayonaise',
        '3':'Chilli',
        '4':'None',
        '5':'Cancel Order'
    }

    for sauce_id in sauce_dict.keys():
        print(sauce_id,sauce_dict[sauce_id]) 
        
    sauce_input = int(input("\n Please select what sauce you would like on your burger. "))
    if sauce_input == 1:
        # Ketchup Selected
        si = sauce_dict.get('1')
        price = 5.50
        total_price = total_price + price
        print(si, "Selected\n")
    elif sauce_input == 2:
        # Mayonaise Selected
        si = sauce_dict.get('2')
        price = 5.50
        total_price = total_price + price
        print(si, "Selected\n")
    elif sauce_input == 3:
        # Chilli Selected
        si = sauce_dict.get('3')
        price = 5.50
        total_price = total_price + price
        print(si, "Selected\n")
    elif sauce_input == 4:
        # None Selected
        si = sauce_dict.get('4')
        price = 5.00
        total_price = total_price + price
        print(si, "Selected\n")
    elif sauce_input == 5:
        return
    elif sauce_input != "":
        print('Invalid option. Please enter a number between 1 and 5 inclusive.')
    b = Burger("burger", price, mi, si)
    return b

#ask user for input and store it in side object
def user_input_side():               
    side_dict ={
        '1':'Straight-Cut Fries',
        '2':'Cheese Bites',
        '3':'Curly Fries',
        '4':'Cancel Order'
    }
    
    global total_price

    for side_id in side_dict.keys():
        print(side_id,side_dict[side_id]) 
        
    side_input = int(input("\n Please select what side you would like. "))
    if side_input == 1:
        # Straight Cut Fries Selected
        si = side_dict.get('1')
        print(si, "Selected\n")
    elif side_input == 2:
        # Cheese Bites Selected
        si = side_dict.get('2')
        print(si, "Selected\n")
    elif side_input == 3:
        # Curly Fries Selected
        si = side_dict.get('3')
        print(si, "Selected\n")
    elif side_input == 4:
        return
    elif side_input != "":
        print('Invalid option. Please enter a number between 1 and 4 inclusive.')
        
    side_size_dict ={
        '1':'Small',
        '2':'Medium',
        '3':'Large',
        '4':'Cancel Order'
    }

    for side_size_id in side_size_dict.keys():
        print(side_size_id,side_size_dict[side_size_id]) 
        
    side_size_input = int(input("\n Please select what size side portion you would like. "))
    if side_size_input == 1:
        # Small Selected
        ssi = side_size_dict.get('1')
        price = 2.00
        total_price = total_price + price
        print(ssi, "Selected\n")
    elif side_size_input == 2:
        # Medium Selected
        ssi = side_size_dict.get('2')
        price = 3.00
        total_price = total_price + price
        print(ssi, "Selected\n")
    elif side_size_input == 3:
        # Large Selected
        ssi = side_size_dict.get('3')
        price = 4.00
        total_price = total_price + price
        print(ssi, "Selected\n")
    elif side_size_input == 4:
        return
    elif side_size_input != "":
        print('Invalid option. Please enter a number between 1 and 4 inclusive.')
    
    s = Side("Side", price, si, ssi)
    return s     

#ask user for input and store it in side object
def user_input_drink():               
    drink_dict ={
        '1':'Coke',
        '2':'Fanta',
        '3':'Sprite',
        '4':'Cancel Order'
    }
    
    global total_price

    for drink_id in drink_dict.keys():
        print(drink_id,drink_dict[drink_id]) 
        
    drink_input = int(input("\n Please select what drink you would like. "))
    if drink_input == 1:
        # Coke Selected
        di = drink_dict.get('1')
        print(di, "Selected\n")
    elif drink_input == 2:
        # Fanta Selected
        di = drink_dict.get('2')
        print(di, "Selected\n")
    elif drink_input == 3:
        # Sprite Selected
        di = drink_dict.get('3')
        print(di, "Selected\n")
    elif drink_input == 4:
        return
    elif drink_input != "":
        print('Invalid option. Please enter a number between 1 and 4 inclusive.')
        
    drink_size_dict ={
        '1':'Small',
        '2':'Medium',
        '3':'Large',
        '4':'Cancel Order'
    }

    for drink_size_id in drink_size_dict.keys():
        print(drink_size_id,drink_size_dict[drink_size_id]) 
        
    drink_size_input = int(input("\n Please select what size drink you would like. "))
    if drink_size_input == 1:
        # Small Selected
        dsi = drink_size_dict.get('1')
        price = 1.50
        total_price = total_price + price
        print(dsi, "Selected\n")
    elif drink_size_input == 2:
        # Medium Selected
        dsi = drink_size_dict.get('2')
        price = 2.00
        total_price = total_price + price
        print(dsi, "Selected\n")
    elif drink_size_input == 3:
        # Large Selected
        dsi = drink_size_dict.get('3')
        price = 3.00
        total_price = total_price + price
        print(dsi, "Selected\n") 
    elif drink_size_input == 4:
        return
    elif drink_size_input != "":
        print('Invalid option. Please enter a number between 1 and 4 inclusive.')
    
    d = Drink("Drink", price, di, dsi) 
    return d

def user_input_combo():
    #ask user for input and store it in combo object 
    #a combo must include one burger, one side, and one drink
    combo_size_dict ={
        '1':'Small',
        '2':'Medium',
        '3':'Large',
        '4':'Cancel Order'
    }
    
    global total_price

    for combo_size_id in combo_size_dict.keys():
        print(combo_size_id,combo_size_dict[combo_size_id]) 
        
    combo_size_input = int(input("\n Please select what size combo you would like. "))
    if combo_size_input == 1:
        # Small Selected
        csi = combo_size_dict.get('1')
        print(csi, "Selected\n") 
        price = 7.00
        total_price = total_price + price
    elif combo_size_input == 2:
        # Medium Selected
        csi = combo_size_dict.get('2')
        print(csi, "Selected\n")  
        price = 8.00
        total_price = total_price + price
    elif combo_size_input == 3:
        # Large Selected
        csi = combo_size_dict.get('3')
        print(csi, "Selected\n")
        price = 9.00
        total_price = total_price + price
    elif combo_size_input == 4:
        return
    elif combo_size_input != "":
        print('Invalid option. Please enter a number between 1 and 4 inclusive.')
    
    drink_dict ={
        '1':'Coke',
        '2':'Fanta',
        '3':'Sprite',
        '4':'Cancel Order'
    }

    for drink_id in drink_dict.keys():
        print(drink_id,drink_dict[drink_id]) 
        
    drink_input = int(input("\n Please select what drink you would like. "))
    if drink_input == 1:
        # Coke Selected
        di = drink_dict.get('1')
        print(di, "Selected\n")
    elif drink_input == 2:
        # Fanta Selected
        di = drink_dict.get('2')
        print(di, "Selected\n")
    elif drink_input == 3:
        # Sprite Selected
        di = drink_dict.get('3')
        print(di, "Selected\n")
    elif drink_input == 4:
        return
    elif drink_input != "":
        print('Invalid option. Please enter a number between 1 and 4 inclusive.')
    
    c = Combo("Combo", price, csi, di)
    return c

def print_menu():
    menu_dict ={
        '1':'Burger',
        '2':'Side',
        '3':'Drink',
        '4':'Combo',
        '5':'Complete Order',
        '6':'Exit/Quit'
    }
    
    for menu_id in menu_dict.keys():
        print(menu_id,menu_dict[menu_id]) 
    
    return menu_dict


def take_order():
    #ask user for name for the order 
    #repeat taking order until client is done 
    #display order details
    #display a thank you message
    option=True
    name = str(input("\n Please enter your first name: "))
    while option: 
        print("----------------------------------")
        print_menu() 
        print("----------------------------------")
        menu_dict ={
        '1':'Burger',
        '2':'Side',
        '3':'Drink',
        '4':'Combo',
        '5':'Complete Order',
        '6':'Exit/Quit'
    }
        option = int(input('\n Enter your choice: '))

        #Check what choice was entered and act accordingly
        if option == 1:
            mi = menu_dict.get('1')
            print("\n",mi, "Selected\n")
            global bo
            #bo = []
            #bo.append(user_input_burger())
            bo = user_input_burger()
        elif option == 2:
            mi = menu_dict.get('2')
            print("\n",mi, "Selected\n")
            global so
            so = user_input_side()
        elif option == 3:
            mi = menu_dict.get('3')
            print("\n",mi, "Selected\n")
            global do
            do = user_input_drink()
        elif option == 4:
            mi = menu_dict.get('4')
            print("\n",mi, "Selected\n")
            global co
            co = user_input_combo()
        elif option == 5:
            mi = menu_dict.get('5')
            o = Order(name)
            o.display_order()
            break
        elif option == 6:
            mi = menu_dict.get('6')
            print("\n Order Cancelled, Please Come Again!")
            break
        elif option != "":
            print('Invalid option. Please enter a number between 1 and 6 inclusive.')
          
take_order()
