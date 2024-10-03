#CIS129_DakotaKartchner_Lab4.py
#CIS129 - Module 4 lab+
#Dakota Kartchner
#Created 9/24/2024
#Description - This program calculates120500 the bonus amounts for the store and employees based on profit amount

#Below is the situation being asked in the lab
"""
A retail company assigns a $6,000 store bonus if monthly sales
are more than $110,000; else if monthly sales are greater than or
equal to $100,000 the store bonus is $5,000, else if monthly
sales are greater than or equal to $90,000 the store bonus is
$4,000, else if monthly sales are greater than or equal to
$80,000, the store bonus is $3,000 otherwise a $0 amount or no
store bonus is awarded. They are using a percent of sales
increase to determine if employees get individual bonuses. If
sales increased by an amount greater than or equal to 5% (0.05)
then all employees get $75, else if sales increased by an amount
greater than or equal to 4%, employees get $50, else if sales
increased by an amount greater than or equal to 3% employees get
$40 otherwise they get $0.
"""

# The main function
def main():
    # Declare local variables
    monthlySales = 0.0  # monthly sales amount
    storeAmount = 0.0   # store bonus amount
    empAmount = 0.0     # employee bonus amount
    salesIncrease = 0.0  # percent of sales increase


    monthlySales = getSales("Enter the monthly sales amount: ") #call to get sales
    salesIncrease = getIncrease("Enter the percent increase in sales: ") # call to getIncrease
    storeAmount = calcStoreBonus(monthlySales) # call to getIncrease
    empAmount = calcEmpBonus(salesIncrease) # call to calcEmpBonus
    printBonus(storeAmount, empAmount) # call to printBonus

# This function gets the monthly sales
def getSales(prompt):
 monthlySales = float(input(prompt))
 return monthlySales

# This function determines the storeAmount bonus
def calcStoreBonus(monthlySales):
    if monthlySales >= 110000:
        storeAmount = 6000
    elif monthlySales >= 100000:
        storeAmount = 5000
    elif monthlySales >= 90000:
        storeAmount = 4000
    elif monthlySales >= 80000:
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount

# This function gets the percent of increase in sales
def getIncrease(prompt):
    salesIncrease = float(input(prompt))
    salesIncrease = salesIncrease / 100
    return salesIncrease

# This function determines the empAmount bonus
def calcEmpBonus(salesIncrease):
    if salesIncrease >= 0.05:
        empAmount = 75
    elif salesIncrease >= 0.04:
        empAmount = 50
    elif salesIncrease >= 0.03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount

# This function prints the bonus information
def printBonus(storeAmount, empAmount):
    print("The store bonus amount is $", storeAmount)
    print("The employee bonus amount is $", empAmount)
    if (storeAmount == 6000) and (empAmount == 75):
        print('Congrats! You have reached the highest bonus amounts possible!')

 # calls main
main()
