#day3 
# - Arithmetic Operator
# -Assignment Operator
# -Logical Operator
# -Conditional Operator

#Arithmetic Operator

# print(5**3)  #Output: 125
# print(5//3)  #output: 1
# print(5%3)   #output: 2

#Assignment Operator
# x=3
# x+=4
# print(x)

# x-=2
# print(x)

# x//=2 #x=x//2
# print(x)


#operator precendence
#this is the rule that describe which expression should be solve first in the multiple collection of expression .
#Example
# ans=2+5*3-4/2

#Operator precendence says we give priority * and / then + and -. But if the * and / or - and + are comes in on expression we gose left to right

#it solve this expression as:
# 2+15-2
# 15

# print(ans)

# #Logical Operator
# #AND
# #produce result true when both codition is true in given condition
# #example:
# print(3>2 and 2>3) #output:false


# #OR
# #Produce result true when only one condition is true in given condition
# #example:
# print(3>2 or 4<9) #true


# #Not
# #It provide the opposite result of actual result
# #Example
# print(not(3>2)) #output:false

#Conditionals if else
#Program to check the grade of student

marks=float(input("Enter Your Percentage: "))

if marks>=80:
    print("You got Distinction.")
elif marks>69 and marks<80:
    print("You got First Devision")
elif marks>59 and marks>69:
    print("You got Second Devision")
else:
    print("You are fail")