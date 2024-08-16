def game():
    if answer == "yes":
        print("Initialization Complete")
    if answer == "no":
        print("Initialization Failed")


answer = input("Do you want to start the game")
game()