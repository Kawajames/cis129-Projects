# CIS129_DakotaK_Lab7.py 
# Dakota K
# CIS129 Prog & Problem Solv I
# Theater Seating Lab: This program calculates income from ticket sales for multiple theater sections. 
# It asks the user for ticket sales, validates input, and displays subtotals for each section and a final total. 

# Constants for each section names
SECTION_A = "A"
SECTION_B = "B"
SECTION_C = "C"

# Constants for each ticket prices
PRICE_A = 20
PRICE_B = 15
PRICE_C = 10

# Constants for each seat count
SEATS_A = 300
SEATS_B = 500
SEATS_C = 200

def display_welcome():
    print("Welcome to the Theater Seating Sales Calculator!")
    print("Section " + str(SECTION_A) + ": $" + str(PRICE_A) + " per ticket, " + str(SEATS_A) + " seats available")
    print("Section " + str(SECTION_B) + ": $" + str(PRICE_B) + " per ticket, " + str(SEATS_B) + " seats available")
    print("Section " + str(SECTION_C) + ": $" + str(PRICE_C) + " per ticket, " + str(SEATS_C) + " seats available")

def get_valid_tickets_sold(section_name, max_seats):
    while True:
        try:
            tickets_sold = int(input("Enter tickets sold for Section " + str(section_name) + " (0-" + str(max_seats) + "): "))
            if 0 <= tickets_sold <= max_seats:
                return tickets_sold
            else:
                print("Please enter a number between 0 and " + str(max_seats) + ".")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_income(tickets_sold, ticket_price):
    return tickets_sold * ticket_price

def main():
    display_welcome()

    # Get the tickets sold for each section
    # Section A
    tickets_sold_a = get_valid_tickets_sold(SECTION_A, SEATS_A)
    income_a = calculate_income(tickets_sold_a, PRICE_A)
    print("Subtotal for Section " + str(SECTION_A) + ": $" + str(income_a))

    # Section B
    tickets_sold_b = get_valid_tickets_sold(SECTION_B, SEATS_B)
    income_b = calculate_income(tickets_sold_b, PRICE_B)
    print("Subtotal for Section " + str(SECTION_B) + ": $" + str(income_b))

    # Section C
    tickets_sold_c = get_valid_tickets_sold(SECTION_C, SEATS_C)
    income_c = calculate_income(tickets_sold_c, PRICE_C)
    print("Subtotal for Section " + str(SECTION_C) + ": $" + str(income_c))

    # Calculate total income
    total_income = income_a + income_b + income_c
    print("Summary of Ticket Sales:")
    print("Tickets sold for Section " + str(SECTION_A) + ": " + str(tickets_sold_a))
    print("Tickets sold for Section " + str(SECTION_B) + ": " + str(tickets_sold_b))
    print("Tickets sold for Section " + str(SECTION_C) + ": " + str(tickets_sold_c))
    print("Total income from ticket sales: $" + str(total_income))

main()
