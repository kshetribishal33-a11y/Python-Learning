#Simple Number Guessing game in Python

number=11
attempts=0

while True:
    guess=int(input("Guess a number... "))
    attempts+=1

    if guess>number:
        print("Highest")
    elif guess<number:
        print("Lowest")
    elif guess==number:
        print("Congratulation! You guessed in", attempts, "attempts👏")
        break

