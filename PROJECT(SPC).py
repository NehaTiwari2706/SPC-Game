#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP 15
#
# Created:     12-04-2022
# Copyright:   (c) HP 15 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# STONE PAPER SCISSOR
import random

def gameWin(comp , You):
    if comp == You :
        return None

    elif comp == 's' :
        if You == 'c' :
            return False
        elif You == 'p' :
            return True
    elif comp == 'c' :
        if You == 's' :
            return True
        elif You == 'p' :
            return False
    elif comp == 'p' :
        if You == 'c' :
            return True
        elif You == 's' :
            return False


print("Computer Turn : stone(s) , paper(p) or scissor(c)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'p'
if randNo == 3:
    comp = 'c'
You = input("Your Turn :stone(s) , paper(p) or scissor(c)? ")

a = gameWin(comp , You)

print(f"Computer Chose {comp}")
print(f"You Chose {You}")

if a == None:
    print("The Game is a Tie")
elif a == True:
    print("You Win!")
else:
    print("Computer win!")


