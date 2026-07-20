import random

target = random.randint(1,100)

while True:
    userchoice = input("Guess the target or Quit(Q) :  ")
    if(userchoice == "Q"):
       break
    userchoice = int(userchoice)
    if(userchoice == target):
         print("success : Correct Guess !")
         break
    if(userchoice < target):
         print("your number is too small .take a bigger guess......")
    else:
         print("your number is too big .take a small guess......")
print("_________GAME OVER___________")