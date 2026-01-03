
# Create the function to calculate daily baking time:
def baking_time_calculator():
    print("------ Baking Time Calculator--------")
    
    # Ask the user how many minutes are needed to bake one batch of cookies
    minutes_per_batch = int(input("How many minutes do you need to bake one batch of cookies? "))
    if minutes_per_batch <= 0:
        print("Please enter a valid positive number for baking time")
        return 
    
    # Ask the user how many batches of cookies need to be baked each day
    batches_per_day = int(input("How many batches of cookies do you need to bake daily? "))
    if batches_per_day <= 0:
        print("Please enter a valid positive number for the batches of cookies.")
        return 
    
    # Calculte the total baking time in minutes per day
    total_minutes = minutes_per_batch * batches_per_day
    
    # Covert total minutes into hours and remaning minutes
    hours = total_minutes // 60
    minutes = total_minutes % 60
    
    # Adjust labels for proper singular or plural grammar
    hours_label = "hour" if hours == 1 else "hours"
    minutes_label = "minute" if minutes == 1 else "minutes"
    
    # Display the final result
    print(f"You need {hours} {hours_label} and {minutes} {minutes_label}" 
          f" to bake {batches_per_day} batches of cookies on daily schedule.")
    
# Call the function to run the program       
baking_time_calculator()    
    
# Create the function to calculate daily inventory calculator
def daily_inventory_calculator():
    print("\n-----------Daily Inventory Calculator-------------")
    
    