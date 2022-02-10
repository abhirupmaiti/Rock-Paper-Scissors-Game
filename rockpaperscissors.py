import random


def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
        else:
            print("Choose a correct input!")
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False
        else:
            print("Choose a correct input!")
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False
        else:
            print("Choose a correct input!")
    else:
        print("Choose a correct input!")


print("Computer's Turn: Rock(r🔮)||Paper(p📰)||Scissors(s✌🤞)?")
randNo = random.randint(1, 3)
if(randNo == 1):
    comp = 'r'
elif(randNo == 2):
    comp = 'p'
elif(randNo == 3):
    comp = 's'

while True:
    you = input("Your Turn: Rock(r🔮)||Paper(p📰)||Scissors(s✌🤞)?")
    a = gamewin(comp, you)
    print(f"Computer chose {comp}")
    print(f"You chose {you}")
    if a == None:
        print("The game is tie!😑😑")
    elif a == True:
        print("Congratulations You win this game!🤗🤗")
    elif a == False:
        print("Sorry you lose this game!😭😭")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break