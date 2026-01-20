# Week 2 - Multi-Function Calculator
# Author: Vy S
# Description: A calculator for Bakery Management.

from practice import baking_time_calculator
from practice import daily_inventory_calculator
from practice import check_oven_workload
from practice import bill_calculator
from practice import weekly_baking_planner

def print_menu():
    print(
        "\n-----Bakery Tool Menu-------"
        "\n1. Baking Time Calculator"
        "\n2. Daily Inventory Calculator"
        "\n3. Check Oven Workload"
        "\n4. Receipt Calculator"
        "\n5. Weekly Baking Planner"
        "\nQ. Quit"     
    )
    
def show_menu():
    valid_choices = ("1", "2", "3", "4", "5", "q")
        
    while True:
        print_menu()
        choice = input("What do you want to do now? ").strip().lower()
        
        if choice not in valid_choices:
            print("Error: You need to choose one of the options from menu.")
            continue
        
        if choice == "q":
            print("Good Bye")
            break
        
        if choice == "1":
            baking_time_calculator()
        elif choice == "2":
            daily_inventory_calculator()
        elif choice == "3":
            check_oven_workload()
        elif choice == "5":
            weekly_baking_planner()
        elif choice == "4":
            cookie_name = "Red Velvet"
            price = 2.59
            quantity = 5
            bill = bill_calculator(cookie_name, price, quantity)
            
            print("\n---------Receipt------------")
            print(bill)       
            
show_menu()
       