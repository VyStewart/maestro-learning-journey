
# Tool 01: Create the function to calculate daily baking time:
def baking_time_calculator():
    print("------ Baking Time Calculator--------")
   
    minutes_per_batch = int(input("How many minutes do you need to bake one batch of cookies? "))
    if minutes_per_batch <= 0:
        print("Please enter a valid positive number for baking time")
        return 
    
    batches_per_day = int(input("How many batches of cookies do you need to bake daily? "))
    if batches_per_day <= 0:
        print("Please enter a valid positive number for the batches of cookies.")
        return 
    
    total_minutes = minutes_per_batch * batches_per_day
    hours = total_minutes // 60
    minutes = total_minutes % 60
    
    hours_label = "hour" if hours == 1 else "hours"
    minutes_label = "minute" if minutes == 1 else "minutes"
    
    print(f"You need {hours} {hours_label} and {minutes} {minutes_label}" 
          f" to bake {batches_per_day} batches of cookies on daily schedule.")
        
#baking_time_calculator()    
    
# Tool02: Create the function to calculate daily inventory calculator
def daily_inventory_calculator():
    print("\n-----------Daily Inventory Calculator-------------")
    
    baked_cookies = int(input("How many cookies do you bake every day? "))
    sold_cookies = int(input("How many cookies do you sell per day? "))
    
    if baked_cookies < 0 or sold_cookies < 0:
        print("Error: Value must be zero or greater.")
        return
    elif sold_cookies > baked_cookies:
        print("Error: Sold cookies cannot exceed baked cookies.")
        return

    full_box = sold_cookies // 9
    remain_cookies = sold_cookies % 9
    leftover = baked_cookies - sold_cookies
        
    box_label = "box" if full_box == 1 else "boxes"
    remain_cookies_label = "cookie" if remain_cookies <= 1 else "cookies"
    leftover_label = "cookie" if leftover <= 1 else "cookies"
        
    print(f"Today you sold {full_box} {box_label} "
           f"and {remain_cookies} {remain_cookies_label}. "
            f"And lefover is {leftover} {leftover_label}. ")
        
#daily_inventory_calculator()

# Tool03: Create the function to check ovens workload,
def check_oven_workload():
    print("\n---------Check Ovens Workload----------")
    
    batch = 18
    
    cookies = int(input("How many cookies do you plan on baking per day? "))
    if cookies <= 0:
        print("Error: The input cookies need to be greater than zero.")
        return
    
    daily_batches = cookies // batch
    if daily_batches == 0:
        print("Error: Not enough cookies for one full batch.")
        return
    
    batches_label = "batch" if daily_batches == 1 else "batches"     
        
    extra_oven = input("Do you you an extra oven available to use? ").lower()
    if ("y" not in extra_oven) and ("n" not in extra_oven):
        print("Error: Yes or No answer")
        return   
    
    if "n" in extra_oven:
        print(
            F"You bake {daily_batches} {batches_label} of cookies today. "
            f"With only one oven available. it will handle the entire workload."
            )
        return
        
    if daily_batches % 2 == 0:
        print(
            f"You bake {daily_batches} {batches_label} of cookies today. "
            f"The workload is balanced between two oves."
            )
    else:
            print(
                f"You bake {daily_batches} {batches_label} of cookies today. "
                f"The workload is split between two ovens. "
                f"But one oven will bake one extra batch. "
                )
       
#check_oven_workload()

# Tool 04: Create the function for Receipt Calculator
def bill_calculator(cookie, price, quantity):
    tax_rate = 0.085
    
    if price <= 0 or quantity <= 0:
        message = "Error: Price and quantinty value need to be greater than zeto"
        return message
    
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax    
  
    receipt = f"""
    Cookie      : {cookie}
    Price       : ${price:.2f}
    Quantity    : {quantity}   
    Subtotal    : ${subtotal:.2f}
    Tax         : ${tax:.2f}
    Total       : ${total:.2f}
    """
    return receipt
    
result = bill_calculator("Red Velvet", 2.45, 5)
#print("\n---------Receippt----------")
#print(result)

# Tool 05: Create the function for Weekly Baking Planner 
def weekly_baking_planner():
    print("\n---------Weekly Baking Schedule (7 Days)-----------")
    
    one_batch = 18
    total_cookies = 0
    total_batches = 0
    
    for day in range(1, 8):
        cookies = int(input(f"Day {day}: how many cookies do you bake? "))
        if cookies <= 0:
            print("Error: Cookies value needs to be greater than zero.")
            continue
        
        total_cookies += cookies
        today_batches = cookies // one_batch
        total_batches += today_batches
        
        cookies_label = "cookie" if total_cookies == 1 else "cookies"
        batches_label = "batch" if total_batches == 1 else "batches"
 
    daily_cookies = round(total_cookies / 7)
    daily_label = "cookies"
    
    print (
      f"\nTotal cookies baked this week: {total_cookies} {cookies_label}."
      f"\nTotal batches baked this week: {total_batches} {batches_label}."
      f"\nAverage cookies per day: {daily_cookies} {daily_label}."
      )              