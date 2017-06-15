# Now our car rental function should use a map/dictionary

def car_rental():
    car_rental = {
        "Honda Civic": "Nice choice, enjoy your Honda Civic",
        "Ferrari": "Great!! It will cost only all your money...",
        "Mustang": "Oh Yeah!! You will have a fun time!!",
        "Other": "Sorry we don't have that. Will just give you something that moves"    
    }
    
    car = input("What car would you like to rent? ")
    
    if car in car_rental:
        print(car_rental[car])
        
    else: # For when the costumer asks for a car using words we don't have as keys
        print("Sorry we don't have that. Will just give you something that moves")
    

# Calling the function 
car_rental()