import random
def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=='r':
        if you=='p':
            return True
        elif you=='s':
            return False 
        else:
            print("Choose a correct input!")           
    elif comp=='p':
        if you=='s':
            return True
        elif you=='r':
            return False
        else:
            print("Choose a correct input!")            
    elif comp=='s':
        if you=='r':
            return True
        elif you=='p':
            return False 
        else:
            print("Choose a correct input!")
    else:
        print("Choose a correct input!")                   
print("Computer's Turn: Rock(rš®)||Paper(pš°)||Scissors(sāš¤)?")
randNo=random.randint(1,3)
if(randNo==1):
    comp='r'
elif(randNo==2):
    comp='p' 
elif(randNo==3):
    comp='s'
you=input("Your Turn: Rock(rš®)||Paper(pš°)||Scissors(sāš¤)?")      
a=gamewin(comp,you)
print(f"Computer chose {comp}")
print(f"You chose {you}")
if a==None:
    print("The game is tie!šš")
elif a==True:
    print("Congratulations You win this game!š¤š¤")
elif a==False:
    print("Sorry you lose this game!š­š­")        

