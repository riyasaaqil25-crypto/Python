print("==========================")
print(" Welcome To Ride Builder! ")
print("==========================")
print()

print("step 1: Pick Ur Vehicle")
print(" 1 - Bike")
print(" 2 - Car")
print()

choice = int(input("Enter 1 or 2: "))
print()

if choice == 1:
    print("Step 2: Pick your bike type")
    print(" 1 - scooty")
    print(" 2 - mountain bike")
    print()

    bike_type = int(input("enter 1 or 2: "))
    print()

    if bike_type == 1:
        print("You picked : Scooty")
        print("Top speed  : 80km/h")
        print("Top speed  : City Roads")
    else:
        print("You picked. : Mountain Bike")
        print("Top speed   : 40km/h")
        print("Best for    : Offroad-Trails")

elif choice == 2:
    print("Step 2: Pick your car type")
    print(" 1 - Sedan")
    print(" 2 - SUV")
    print()

    car_type = int(input("Enter 1 or 2: "))
    print()

    if car_type == 1:
        print("You picked  : sedan")
        print("Seats       : 5 passengers")
        print("Best for    : Family trips")
    else:
        print(" You picked : SUV")
        print("Seats.      : 7 passengers")
        print("Best for    : Off-Road adventures")

else:
    print("That was not a valid choice.")
    print("Please enter 1 for Bike or 2 for Car.")

print()
print("=============================")
print(" Your custom ride is ready!  ")
print("      Enjoy the journey.     ")
print("=============================")