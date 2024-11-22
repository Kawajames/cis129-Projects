
# CIS129_DakotaK_Lab12.py
# Dakota Kartchner
# 11/13/2024
# CIS129 Prog and Problem Solving

class Pet:
    # Constructor
    def __init__(self, name='', pet_type='', age=0):
        self.name = name
        self.type = pet_type
        self.age = age

    # Mutators
    def setName(self, name):
        self.name = name

    def setType(self, pet_type):
        self.type = pet_type

    def setAge(self, age):
        self.age = age

    # Accessors
    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getAge(self):
        return self.age


def main():
    # Create a Pet object
    animal = Pet()

    # Get user input for the pet's details
    input_name = input("Enter a pet name: ")
    animal.setName(input_name)

    input_type = input("Enter a pet type: ")
    animal.setType(input_type)

    input_age = int(input("Enter a pet age: "))
    animal.setAge(input_age)

    # Display the pet's information
    print("\nThe pet name is:", animal.getName())
    print("The pet type is:", animal.getType())
    print("The pet age is:", animal.getAge())


# Run the main function
if __name__ == "__main__":
    main()
