#Mini Project: Student Record Management System

students=[]
student_ids=set()
student_marks={}

while True:
    print("===== Student Record Management System====")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student by ID")
    print("4. Show Highest Marks")
    print("5. Exit")

    choice= input("Enter Your Chice...:")

    if choice=="1":
        student_id = int(input("Enter Student ID:"))

        if student_id in student_ids:
            print("Student Already Exists!")

        else:
            name=input("Enter Student Name: ")
            marks=int(input("Enter Student Marks: "))

            student = (student_id, name, marks)

            students.append(student)
            student_ids.add(student_id)
            student_marks[name] = marks

            print("Student Added Successfully!")

    elif choice=="2":
        if len(students)==0:
            print("No student record found.")
        else:
            print("Student Records:")
            for student in students:
                print(
                    "ID:", student[0],
                    "| Name:", student[1],
                    "| Marks:", student[2]
                )

    elif choice=="3":
        search_id = int(input("Enter Student ID to search: "))

        found=False

        for student in students:
            if student[0]==search_id:
                print("\nStudent Found")
                print("ID:", student[0])
                print("Name:", student[1])
                print("Marks:", student[2])
                found=True
                break
        if not found:
            print("Student not Found.")

    elif choice=="4":
        if len(student_marks)==0:
            print("No record availabe")
        else:
            highest_marks=max(student_marks.values())

            print("\nHighest Marks:", highest_marks)

            for name, marks in student_marks.items():
                if marks==highest_marks:
                    print("Topper:", name)

    elif choice=="5":
        print("Program Ended.")
        break
    else:
        print("Invalid Choice!")
         