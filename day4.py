#Day 4
#while loop

#program to print Hello python for 10 times 
# i=1
# while i<=3:
#     print("Hello Python!")
#     i+=1


#program to print 
# *
# **
# ***
# ****
# *****

# i=1
# while i<=5:
#     print("*" * i)
#     i+=1


#to print this structure
# *****
# ****
# ***
# **
# *

# i=5
# while i>0:
#     print("*" * i)
#     i-=1

#to print numbers from 10 to 1 in reverse order.
# i=10
# while i>0:
#     print(i)
#     i-=1

# to Print all even numbers from 2 to 20.
# i=1
# while i<=20:
#     if (i%2==0):
#         print(i)
#     i+=1


#For Loop
#print value from 0 to 10
# for i in range(11):
#     print(i)


#to print even number from 1 to 10
# for i in range(2,11):
#     if i%2==0:
#         print(i)

# for i in range(2, 11, 2):
#     print(i)

#Break and Continue
# Example of Break
# for i in range(1,51):
#     if (i==21):
#         break
#     if (i%3==0):
#         print(i)
# print("Out of Loop")

#exmaple of continue
for i in range(1,51):
    if(i==21):
        continue
    if(i%3==0):
        print(i)
print("step 21 is skiped")