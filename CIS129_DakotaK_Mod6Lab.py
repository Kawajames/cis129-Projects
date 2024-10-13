# CIS129_DakotaK_Mod6Lab.py
# Dakota K
# CIS129 Prog & Problem Solv I
# Hotdog Cookout Calculator: This script calculates the minimum number of hot dog and bun-
# packages needed for a cookout based on the number of attendees and hot dogs per person, and it displays any leftovers.

# Global Constants for hot dogs per package and buns per package
DOGS = 10
BUNS = 8

def get_total_hotdogs():
    """This script will calculate the total number of hot dogs needed based on user input."""
    # Ask user for the number of attendees and hot dogs per attendee
    attendees = int(input("Enter the number of attendees: "))
    hot_dogs_per_person = int(input("Enter the number of hot dogs per person: "))
    
    # Calculates the total number of hot dogs required
    total = attendees * hot_dogs_per_person
    return total

def show_results(total_hotdogs):
    """This script will calculate and display the required packages and leftover hot dogs and buns."""
    # Calculates the hot dogs leftovers and minimum packages needed
    dogs_left = (DOGS - total_hotdogs % DOGS) % DOGS
    min_dogs = (total_hotdogs // DOGS) + (1 if dogs_left > 0 else 0)

    # Calculates the buns leftovers and minimum packages needed
    buns_left = (BUNS - total_hotdogs % BUNS) % BUNS
    min_buns = (total_hotdogs // BUNS) + (1 if buns_left > 0 else 0)

    # Display the results
    print("Minimum packages of hot dogs needed: " + str(min_dogs))
    print("Minimum packages of hot dog buns needed: " + str(min_buns))
    print("Hot dogs remaining: " + str(dogs_left))
    print("Hot dog buns remaining: " + str(buns_left))

# Main program stuff
def main():
    total_hotdogs = get_total_hotdogs()
    show_results(total_hotdogs)

# Execute the program
if __name__ == "__main__":
    main()
