import random

print("Rock, Paper, Scissors")
print("""`;-.          ___,
  `.`\_...._/`.-"`
    \        /      ,
    /()   () \    .' `-._
   |)  .    ()\  /   _.'
   \  -'-     ,; '. <
    ;.__     ,;|   > \
   / ,    / ,  |.-'.-'
  (_/    (_/ ,;|.<`
    \    ,     ;-`
     >   \    /
    (_,-'`> .'
jgs      (_,'""")

while True:
    print("Enter choice \n1 for Rock \n2 for Paper \n3 for Scissors \n0 to quit")

    choice = int(input("Your turn: "))

    while choice > 3 or choice < 0:
        choice = int(input("Invalid input. Enter again: "))

    if choice == 0:
        print("Thanks for playing!")
        break

    comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print("Computer chooses: " + comp_choice_name)

    if ((choice == 1 and comp_choice == 2) or
            (choice == 2 and comp_choice == 1)):
        print("Paper wins")
        result = "Paper"
    elif ((choice == 1 and comp_choice == 3) or
          (choice == 3 and comp_choice == 1)):
        print("Rock wins")
        result = "Rock"
    else:
        print("Scissors wins")
        result = "Scissors"

    if result == comp_choice_name:
        print("Computer wins!")
    else:
        print("You win!")

    print("Do you want to play again? (Y/N)")
    ans = input()

    if ans == 'n' or ans == 'N':
        break
print("Merci")
