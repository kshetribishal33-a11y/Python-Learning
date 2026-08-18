#Day 1 (Part 1)
#1. Display
#2. Variable
#3. Input
#4. Coments


#print any thing 
print("Hello world!", "I am a Programmer")

print("Bishal Khadka Kshetri")

#variable
name="Bishal Khadka"
age=19
print(name,age)
#output: Bishal Khadka 19

#we can change the value of variable but the output will be new chagned value

name="Bishal"
age=20
print(name,age)
#output : Bishal 20


# to check the variable type

print(type(age))
#output: int

gpa=3.5
print(type(gpa))
#output: float

# isStudent=True
# print(type(isStudent))
#output: bool


#Input
name=input("Enter Name: ")
print("Hello, My name is ",name)

#we can also use concatination
fullname=input("Enter Your Name: ")
print("Hello, My name is "+fullname)

# Exercise 1
# in your program: 
# add a person with first name as Tony and last name as Stark 
# tony's age is 53 and height is 1.85m

# tony is superhero. Take his superhero name as input and print it

firstName="Tony"
lastName="Stark"
age=53
height="1.85m"

superheroName=input("Enter the superhero name: ")

print("Name ",firstName, lastName)
print("Age  ",age)
print("Height  ",height)
print("Superhero name: ",superheroName)