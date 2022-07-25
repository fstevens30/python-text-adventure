# Setup
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
 
# Introduction
print("You awake in a pod inside of a large foyer. A soldier sets you free.\n")
name = input("What is your name, Soldier?\n")
print("Hurry up then, " + name + "! They're coming!")
print("You exit the building to a chaotic street.\n")
print("Can you find your way through?\n")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Would you like to step into the battlefield?\nyes/no\n")
    if response == "yes":
        print("You head onto the street. You hear screams and explosions.\n")
    elif response == "no":
        print("You are a fucking coward " + name + "! The soldier screams at you.\n")
        quit()
    else: 
        print("Come on mate, use your words!\n")
 
# Next part of game
response = ""
while response not in directions: # While loop to keep asking for input
    print("To your left, you see a giant alien.")
    print("To your right, there is an injured soldier.")
    print("There is more gunshots directly ahead on  the street with calls for help.")
    print("Behind you is the building you awoke in.\n")
    response = input("What direction do you move?\nleft/right/forward/backward\n")
    if response == "left":
        print("The alien immediately throws you against the wall, you see blood fill your helmet. Rest in peace " + name + ".")
        quit()
    elif response == "right":
        print("You run to help the wounded soldier.\n")
    elif response == "forward":
        print("You charge into the battlefield.\n")
        response = "" 
    elif response == "backward":
        print("You run back to cover. The soldiers shake their heads as they see you retreating.\n")
        quit()
    else:
        print("I didn't understand that.\n")