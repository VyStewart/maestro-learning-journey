
# Create the function to calculate daily baking time:
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
        
baking_time_calculator()    
    
# Create the function to calculate daily inventory calculator
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
        
daily_inventory_calculator()

#Create the function to check ovens workload,
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
       
check_oven_workload()