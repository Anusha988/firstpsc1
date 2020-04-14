Print the Game Instruction to the User/Player 
print("Winning Rules of the Rock Paper Scissor Game as follows: \n"
                                +"\tRock  vs Paper   -> Paper wins \n"
                                +"\tRock  vs Scissor -> Rock wins \n"
                                +"\tPaper vs Scissor -> Scissor wins \n") 




# Print a Thanks Message to the user
print("\nThanks for playing Rock Paper Scissor Game \n")
# Print the Game Instruction to the User/Player
print("Winning Rules of the Rock Paper Scissor Game as follows: \n"
      + "\tRock  vs paper   -> paper wins \n"
      + "\tRock  vs scissor -> Rock wins \n"
      + "\tpaper vs scissor -> scissor wins \n")

while True:

    # Get the response from User to Play Again
    ans = input("Do you want to play again ? (Y/N) > ")

    # Check the response from User and continue the loop
    # Othewise break the loop to close the game
    if (ans == 'n' or ans == 'N'):
        break

# Print a Thanks Message to the user
print("\nThanks for playing Rock Paper Scissor Game \n")
# Print the Game Instruction to the User/Player
print("Winning Rules of the Rock Paper Scissor Game as follows: \n"
      + "\tRock  vs paper   -> paper wins \n"
      + "\tRock  vs scissor -> Rock wins \n"
      + "\tpaper vs scissor -> scissor wins \n")

while True:

    # Tell User to enter either Rock, Paper, Scissor
    print("Enter choice \n 1. rock \n 2. paper \n 3. scissor \n")

    # Get the response from the User
    user_choice = input("User turn: > ")

    # Print the response from the User
    print("User has choosen : " + user_choice + "\n")

    # Get the response from User to Play Again
    ans = input("Do you want to play again ? (Y/N) > ")

    # Check the response from User and continue the loop
    # Othewise break the loop to close the game
    if (ans == 'n' or ans == 'N'):
        break

# Print a Thanks Message to the user
print("\nThanks for playing Rock Paper Scissor Game \n")


