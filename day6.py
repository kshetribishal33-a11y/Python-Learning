#Function ==> is a reusable block of code that perform a specific tassk. Function help make program shorter, organized, and easier to maintain.
# Example:
# def sum(x,y):
#     print(x+y)
# sum(2,5)

# def add(a,b):
#     print("Sum is:", a+b)
# a=float(input("Enter 1st Num  "))
# b=float(input("Enter 2nd Num  "))

# add(a,b)

#program to print the number is even or odd using function
# def is_even():
#     num=int(input("Enter your Number: "))

#     if num%2==0:
#         print("Even Number.")
#     else:
#         print("Odd Number")
# is_even()

#Program to check the greater number among 2 number
# def greater():
#     a=float(input("Enter 1st num "))
#     b=float(input("Enter 2nd num "))

#     if a>b:
#         print("a is greater.")
#     else:
#         print("b is greater.")

# greater()

#Program to print the table of random number
# def table():
#     num=int(input("Enter you num: "))
#     count=1
#     while count<=10:
#         print(f"{num} * {count} = ",num*count)
#         count+=1
# table()



#function to convert celsius to fahrenheit with return value

# def temp_converter():
#     while True:
#         print("\n====Temprature Converter=======")
    
#         print("1. Celsius to Fahrenheit.")
#         print("2. Fahrenheit to Celsius.")
#         print("3. Exit.")
#         choice=input("Choose what do you want: ")
#         if choice=="1":
#             c=float(input("Enter the Celsius value: "))
#             result= (c*1.8)+32
#             print(f"{c}°C = {result}°F")
#         elif choice=="2":
#             f=float(input("Enter the Fahrenheit value: "))
#             result= (f-32)/1.8
#             print(f"{f}°F = {result}°C")

#         elif choice=="3":
#             print("Thank You!")
#             break

#         else:
#             print("Out of Range!!")

# temparture=temp_converter()

#function to find factorial
def fact():
    num=int(input("Enter number: "))
    factorail=1

    for i in range(1, num+1):
        factorail=factorail*i
    print(f"Factorial  {num} is {factorail}")
fact()