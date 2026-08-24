#Day 5 
#-list
#-Tuple
#-set
#-Dictionary

#list:- A set of items/collection of items. It can store different types of data.

# marks=[99,98,90,92,'A',90.54]
# print(marks, type(marks))


#some function we can perform on our list
#a. len(): to find the length of list
# print(len(marks))

#b. index(): to find the values index
# print(marks[3])

#c. slicing : to make sub-list of original list
# print(marks[1:4])

# print(marks[-3:])

#d. append(): to add some values in the end of list
# marks.append(60)
# print(marks)

#e. insert(): to add some values according to index
# marks.insert(2,30)
#print(marks)

#f. clear(): to make empty the list
# marks.clear()
# print(marks,len(marks))

#g. pop(): to remove value according to index
# marks.pop(4)
# print(marks)


#Tuple:Immutable => this is similar to list but it is defined with parenthesis/ neither parenthesis nor brackets. We can't modify the tuple once created

# marks=(90,40,23,89,20,20)
# print(marks, type(marks))

#some operation that we perform on Tuple

#a. count(): to check how many times a value is present on tuple
# print(marks.count(20))

#b. index(): similar to list 
# print(marks[3])

#Set: is the collection of unique items. It is defined by curly braceses.
# marks={32,68,90,32,45,75,45}
# print(len(marks),marks)

# for score in marks:
#     print(score)

#Dictionary: is the collection of key value pairs. in dictionary the key are unique

# marks={"math":99, "Nepali":98, "English":80}
# print(marks, type(marks))

# #to access specific key 
# print(marks["English"])

# #to modify existing value
# marks["math"]=90
# print(marks["math"])

# #to add new item
# marks["Science"]=89
# print(marks)



#Exercise 5

# a. Given a list of rollno :
# [101,105,102,101,108,105,110]
# print all unique rollno in the list

# rollno={101, 105, 102,101,108,105,110}
# unique_roll=list(set(rollno))

# print(unique_roll)


# b. Given employees records in the form of a list of types where each tuple contain:
# [Emplouess ID, Name, Salary]

#Example: [
# (101, "Ram", 50000)
# (102, "Hari", 60000)
# (103, "Raju", 90000)
#]

#Ask user to enter employee id and search it inside record
 
employees=[
    (101, "Ram", 50000),
    (102, "Hari", 60000),
    (103, "Raju", 90000)
]

emp_id=int(input("Enter your Employee id.."))

found=False

for emp in employees:
    if emp[0]==emp_id:
        print("ID", emp[0])
        print("Name", emp[1])
        print("Salary", emp[2])
        found =True
        break
if not found:
    print("Employee not found!")