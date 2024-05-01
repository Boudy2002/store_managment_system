import sqlite3

import Functions
import Interface
from Customer import Customer

try:
    conn = sqlite3.connect('Database')
    cursor = conn.cursor()
except sqlite3.Error as error:
    print(error)

while True:
    choice = int(input("Welcome to the store\nPlease enter your choice:\n1-Customer\n2-Employee\n"))
    if choice == 1:
        choice = int(input("Do you have an Account?\n1.Yes\n2.No\n"))
        if choice == 1:
            email = input("Please enter your Email : ")
            password = input("Please enter your Password")
            if (Functions.checkCredentials(email, password)):
                Interface.customerInterface(Functions.getCustomer(email))
        elif choice == 2:
            firstName = input("Please enter your first name : ")
            lastName = input("Please enter your last name : ")
            email = input("Please enter your email address : ")
            password = input("Please enter your password : ")
            address = input("Please enter your address : ")
            city = input("Please enter your city : ")
            state = input("Please enter your state : ")
            zipCode = input("Please enter your zipCode : ")
            customer = Customer(firstName, lastName, email, address, city, state, zipCode, password)
            Interface.customerInterface(customer)
        else:
            print("Invalid Input\nplease try again")
    elif choice == 2:
        pass
    else:
        print("Invalid Input\nPlease try again")
