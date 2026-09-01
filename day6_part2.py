#Module Function
#math function
# import math
# print(math.factorial(5))
# print(math.sqrt(25))
# print(math.ceil(2.1))
# print(math.pow(4,5))
# print(math.floor(2.9))

#random function
# import random
# print(random.randint(1,5))
# print(random.random())

#datetime function
# from datetime import datetime
# now=datetime.now()
# print(now)

# date=datetime.now().date()
# print(date)

# time=datetime.now().time()
# print(time)

# form_date=datetime.now()
# print(form_date.strftime("%d/%m/%Y"))

#Practice Exercise

# 1. WAF to check if a number is odd or even
# def check():
#     num=int(input("Enter a number: "))
#     if num%2==0:
#         print("Number is Even.")
#     else:
#         print("Number is Odd.")
# check()

# 2. WAF the count the number of vowels in string
# def count():
#     x=input("Enter your string: ")
    
#     count=0
#     for ch in x.lower():
#         if ch in "aeiou":
#             count+=1

#     return count
# result=count()

# print(f"Number of Vowels: {result}")

#WAF to print if a number is prime or not using while loop
# def prime_check():
#     num=int(input("Enter a number: "))

#     count=0
#     i=1
#     while i<=num:
        
#         if num%i==0:
#             count+=1
#         i+=1    
#     return count
# result=prime_check()
# if result==2:
#     print("Number is prime.")
# else:
#     print("Number is not Prime.")


#WAF to print if a number is prime or not using for loop


# def prime_check():
#     num=int(input("Enter a number: "))
#     count=0

#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#         i+=1   

#     return count

# result=prime_check()

# if result==2:
#     print("Number is prime.")
# else:
#     print("Number is not Prime.")

#WAF to return the average marks if a list of marks is passed as paramerter

# def average_marks(marks):
#     total=sum(marks)
#     count=len(marks)
#     average=total/count
#     return average
# result=average_marks([71,69,82,88,79,91])
# print(f"The average is {result}")

#WAF to return greatest number in list
# def max_num():
#     numbers=list(map(float, input("Enter numbers: ").split()))
#     greatest=numbers[0]

#     for num in numbers:
#         if num>greatest:
#             greatest=num

#     return greatest
# result=max_num()
# print(f"The greatest number is {result}")

