import random

# Option in tuple because we are not changing it

options = ("rock","paper","scissor")

# If game is running

running = True

while running:

    player = None

    computer = random.choice(options)

    #If player inputs invalid options
    while player not in options:

        player = input("Enter the choice (rock),(paper),(scissor): ")
  
    print(f"player {player}")
    print(f"computer {computer}")
    
    # taking all winning conditions.
    if player == computer:
        print("It's TIE !!!")

    elif player == "rock" and computer == "scissor":
        print("HURRAY! YOU WIN.")

    elif player == "paper" and computer == "rock":
        print("HURRAY! YOU WIN.")

    elif player == "scissor" and computer == "paper":
        print("HURRAY! YOU WIN.")
     
    # else for losing condition
    else:
        print(":-( YOU LOSE!!!")

        #break the condition if user dont want to play again
    if not input("Would you like to play again ? (y/n)").lower() == "y":
        running = False

print("Thanks for playing.")