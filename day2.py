#day 2
#Type Casting & Type Conversion

# This is Type Casting or Explicit Casting
#str to int
age="20"
age=int(age)
print(age)
print(type(age))

# int to str
marks=90
marks=str(marks)
print(marks)
print(type(marks))


rollNo=input("Enter Your RollNo.: ")
new_rollNo=int(rollNo) +1
print(new_rollNo)
print(type(new_rollNo))

#This is Type Conversion ir Implicit Casting
print(2+5.5)
#output: 7.5 


# Exercise 
# Sum Promgram => a,b => sum

a=input("Enter a: ")
b=input("Enter b: ")

sum=a+b
print("Sum is: ",sum)

# String Methods

# some Methods are:
name="Ram Khadka"

print(name.upper())
print(name.lower())
print(name.find("ka"))
print(name.replace("Ram","Hari"))
print(name)

# Keywords
print('x' in name) #false
print('h' in name) #true


# Exercise 2
# Take price of 3 product as input and
# - print the total bill amount
# - print the average price

# take a superhero name as input and check if it start's with 'S'/'s' or not


price1=float(input("Enter the price of watch: "))
price2=float(input("Enter the price of earphone: "))
price3=float(input("Enter the price of charger: "))

totalbill=price1+price2+price3
print("Total Bill Amount is: ",totalbill)

averagebill=totalbill/3
print("Average Bill is: ",averagebill)

name=input("Enter SuperHero Name: ")
print('S' in name)