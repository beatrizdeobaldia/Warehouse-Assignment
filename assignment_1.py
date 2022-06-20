#Warehouse Assignment 

#Import library
import sys
from tkinter import X

#base class for the type of stock
class jewels:
    def __init__(self, name: str, quantity: int) -> None:
        self.name = name
        self.quantity = quantity


#Warehouse class - changes to the stock
class Warehouse(jewels):
    def __init__(self, name: str, quantity: int) -> None:
        super().__init__(name, quantity)

#Method to show amount of stock

    def show_stock(self) -> int:
        return self.quantity

#Method to add stock

    def add_stock(self) -> int:
        new_value = int(input('number of new arrivals'))
        return self.quantity + new_value

#Method to remove stock

    def substract_stock(self) -> int:
        minus_value = int(input('number of sold items'))
        return self.quantity - minus_value


#items - Define 3 types of stock
if __name__ == "__main__":
    rubi = Warehouse("rubi", 10)
    sapphire = Warehouse("sapphire", 15)
    emerald = Warehouse("emerald", 20)

#Interactive part

def welcome_user():
    print("Welcome! What would you like to do?")
    print("1. Remove stock")
    print("2. Add stock")
    print("3. Check product availability")
    print("4. Get product information")
    return input("What would you like to do? ")

run = welcome_user()
#REMOVE STOCK
while True:
    if run == '1':
        print("What jewel would you like to buy? a. rubi, b. sapphire, c. emerald")
        desired_product = input('Input letter: ')
        print("How many units? ")
        stock_amount = int(input('Quantity: '))
        #Check if rubis are available
        if desired_product == 'a':
            if stock_amount > rubi.quantity:
                print('quantity not available')
            else:
                print('The amount is available')
                rubi.quantity = rubi.quantity - stock_amount
        #check for sapphires
        elif desired_product == 'b':
            if stock_amount > sapphire.quantity:
                print('quantity not available')
            else:
                print('The amount is available')
                sapphire.quantity = sapphire.quantity - stock_amount
        #check for emeralds
        elif desired_product == 'b':
            if stock_amount > emerald.quantity:
                print('quantity not available')
            else:
                print('The amount is available')
                emerald.quantity = emerald.quantity - stock_amount

        run = welcome_user()
#ADD STOCK
    elif run == '2':
        print("What jewel would you like to add? a. rubi, b. sapphire, c. emerald")
        new_product = input('Input letter: ')
        print("How many units? ")
        stock_amount = int(input('Quantity: '))
        #add rubi
        if new_product == 'a':
            print('Thank you for the rubis!')
            print('Now we have', rubi.quantity + stock_amount, 'in the warehouse')
            rubi.quantity = rubi.quantity + stock_amount
        #add sapphires
        elif new_product == 'b':
            print('Thank you for the sapphires!')
            print('Now we have', sapphire.quantity + stock_amount, 'in the warehouse')
            sapphire.quantity = sapphire.quantity + stock_amount
        #add emeralds
        elif new_product == 'c':
            print('Thank you for the emeralds!')
            print('Now we have', emerald.quantity + stock_amount, 'in the warehouse')
            emerald.quantity = emerald.quantity + stock_amount
        run = welcome_user()
#CHECK AVAILABILITY OF PRODUCTS
    elif run == '3':
        print("Which product are you interested in viewing? a. rubi, b. sapphire, c. emerald")
        desired_product = input('Input letter: ')
        if desired_product == 'a':
            print('There are currently', rubi.quantity, 'of', rubi.name)
        elif desired_product == 'b':
            print('There are currently', sapphire.quantity, 'of', sapphire.name)
        elif desired_product == 'c':
            print('There are currently', emerald.quantity, 'of', emerald.name)

        run = welcome_user()

    #GET PRODUCT REPORT 
    elif run == '4':
        print('The warehouse report is:')
        print('There are currently', rubi.quantity, 'of', rubi.name)
        print('There are currently', sapphire.quantity, 'of', sapphire.name)
        print('There are currently', emerald.quantity, 'of', emerald.name)

    run = welcome_user()

        


