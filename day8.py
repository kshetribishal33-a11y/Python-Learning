#Constructor: is inbuilt function defined by __init__() function and it is executed when object is created.

# class Student:
#     def __init__(self,name,marks):
#         print("Student are added in Database.")
#         self.name=name
#         self.marks=marks

# s1=Student("Ram",98)
# print(s1.name, s1.marks)

# s2=Student("Laxman", 96)
# print(s2.name, s2.marks)


#Class and Instant attr
#class attribute==> variable which create inside of class and outside of __init__() is called class attr

# class Car:
#     wheels=4  #instance attr

# c1=Car()
# c2=Car()

# print(c1.wheels)
# print(c2.wheels)

#Instance attr==> variable which create inside of __init__() callde instance attr
# class Car:
#     def __init__ (self, name, color):
#         self.name=name #instance attr
#         self.color=color  #instance attr

# c1=Car("BMW","Green")
# c2=Car("Thar","Black")

# print(c1.name,c1.color)
# print(c2.name, c2.color) 

#class attr lai class dekhi change garda
# class Car:
#     wheels=4

# c1=Car()
# c2=Car()

# Car.wheels=6
# print(c1.wheels)
# print(c2.wheels)


#class attr lai object dekhi change garda
# class Car():
#     wheels=4

# c1=Car()
# c2=Car()

# c1.wheels=6
# print(c1.wheels)
# print(c2.wheels)
# print(Car.wheels)


#Method==>is a function that belong to object
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def hello(self):
#         print("Hello, ",self.name)

#     def get_Marks(self):
#         return self.marks

# s1=Student("Bishal",90)
# s1.hello()
# print(s1.get_Marks())


#practice
#Create Student class that take name and marks of 3 subjects as arguments in constructor. Then create a method to print the average

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
      

    def get_average(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hi", self.name, "Your avg score is:", sum/3)

    def avg(self):
        aveg=sum(self.marks)/len(self.marks)
        print("Hi", self.name, "Your avg score is:", aveg)

s1=Student("Ram",[98,90,95])
s1.avg()
s1.name="Bishal"
s1.avg()


