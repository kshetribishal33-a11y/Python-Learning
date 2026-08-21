#1. Print all odd number from 1 to 10
# for i in range(1,11,2):
#     print(i)

# for i in range(11):
#     if i%2!=0:
#         print(i)

#2.Print the table of 57
# i=1
# while i<=10:
#     print("57 *", i,"=",57*i)
#     i+=1


#3.Print all multiplies of 3 from 1 to 50 but skip 15

# for i in range(1,51):
#     if i==15:
#         continue
#     if i%3==0:
#         print(i)

#4. Take two integer a and b as input and find & print the first number between 1 to 1000 that is divisible by both numbers

# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))

# i=1
# while i<=1000:
#     if(i%a==0 and i%b==0):
#         print(i)
#         break
#     i+=1

#Number guessing game
number=10
attempts=0

while True:
    guess= int(input("Guess a number: "))
    attempts+=1
    if guess>number:
        print("Highest")

    elif guess<number:
        print("Lowest")
    elif guess==number:
        print("Congratulation! You guessed in", attempts ,"attempts")
        break
