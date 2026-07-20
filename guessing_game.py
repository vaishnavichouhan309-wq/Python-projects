import random

easy_words = ["apple", "train","tiger","money","india"]
medium_words = ["python","bottle", "monkey","planet","laptop"]
hard_words = ["elephant", "diamond", "umberlla", "computer","mountain"]

print("Welcome to the password game")
print("Choose a hard , medium , and easy")

level = input('enter level :').lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid choice. Defaulting to easy level")
    secret = random.choice(easy_words)

attempts = 0
print("\n Guess the secret password")  

while True:
    guess = input("enter your guess:").lower()
    attempts +=1

    if guess == secret:
        print(f'Congratulation ! You guessed the password it in {attempts}attempts.')
        break

    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"
        print("Hint :" + hint)

print("GAME OVER.")