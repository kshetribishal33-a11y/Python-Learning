#Constructor: is inbuilt function defined by __init__() function and it is executed when object is created.

class Student:
    def __init__(self,name,marks):
        print("Student are added in Database.")
        self.name=name
        self.marks=marks

s1=Student("Ram",98)
print(s1.name, s1.marks)

s2=Student("Laxman", 96)
print(s2.name, s2.marks)

