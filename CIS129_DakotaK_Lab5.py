# CIS129_DakotaK_Lab5.py
# Dakota K
# CIS129 Prog & Problem Solv I
# Bottle Return Program: This script calculates the total # of bottles returned over 7 days and its payout.

#Script Creation Instructions
#Write a program that will allow a grocery store to keep track of the total number of bottles collected for seven days.
#The program will calculate the total number of bottles returned for the week and the amount paid out (the total returned times .10 cents). 
#The output of the program should include the total number of bottles returned and the total paid out.  
#The program will ask the user if they have more data to enter and will end the program if they do not. 

def bottle_return_program():
    # Step 1: Declare variables below
    total_bottles = 0  # Total bottles
    total_payout = 0  # Total payout
    today_bottles = 0  # Total bottles for a day
    keep_going = 'y'  # This is the loop control variable

    # Step 2: Loop to run program again
    while keep_going == 'y':  # Use the variable directly here
        total_bottles = 0  # Reset total_bottles for a new week
        
        # Step 3: Loop through 7 days to get the number of bottles returned each day
        for day in range(1, 8):
            today_bottles = int(input("Enter number of bottles for day #" + str(day) + ": "))
            total_bottles += today_bottles  # Accumulate total bottles
        
        # Step 4: Calculate total payout
        total_payout = total_bottles * 0.10
        
        # Step 5: Display the total number of bottles and total payout
        print("The total number of bottles collected is " + str(total_bottles))
        print("The total paid out is $" + str(round(total_payout, 1)))
        
        # Step 6: Ask if user wants to enter another week’s worth of data
        keep_going = input("Do you want to enter another week’s worth of data? (Enter y or n): ")

# Run the bottle return program
bottle_return_program()
