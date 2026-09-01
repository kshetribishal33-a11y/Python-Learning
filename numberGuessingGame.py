import random

def play_game():
    lucky_num=random.randint(1,30)
    attempts=0

    while True:
        user_num=int(input("Enter you lucky number: "))
        attempts+=1

        if user_num==lucky_num:
            print(f"Congratulation! you won the game in {attempts} attempts👏👏")
            break

        elif user_num>lucky_num:
            print("Too High")

        elif user_num<lucky_num:
            print("Too Low")
    print("\nThanks for playing🙏")

play_game()