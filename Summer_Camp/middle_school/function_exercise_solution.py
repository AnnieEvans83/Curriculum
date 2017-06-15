# Can we write the car rental options inside a function?

def car_rental():
    car = input("What car would you like to rent? ")

    if car == "Honda Civic":
        print("Nice choice, enjoy your Honda Civic")

    elif car == "Ferrari":
        print("Great!! It will cost only all your money...")

    elif car == "Mustang":
        print("Oh Yeah!! You will have a fun time!!")

    else:
        print("Sorry we don't have that. Will just give you something that moves")
        
# Calling the function 
car_rental()