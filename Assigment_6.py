#Q1 and Q2
import pickle
import json

while True:
    print("1.Employee Data")
    print("2.Student Data")
    print("3.Exit")

    choice=int(input("Enter your choice:"))

    if choice==1:
        data={
            "name":input("Enter employee name:"),
            "id":int(input("Enter employee id:")),
            "salary":int(input("Enter salary:"))
        }

        with open("data.pkl","wb") as file:
            pickle.dump(data,file)

        with open("data.pkl","rb") as file:
            data=pickle.load(file)

        print(data)
        print(type(data))

    elif choice==2:
        students=[]
        n=int(input("Enter number of students:"))

        for i in range(n):
            name=input("Enter student name:")
            marks=int(input("Enter marks:"))
            students.append({"Name":name,"Marks":marks})

        with open("students.json","w") as file:
            json.dump(students,file)

        with open("students.json","r") as file:
            data=json.load(file)

        print(data)
        print(type(data))

    elif choice==3:
        print("Exit")
        break

    else:
        print("Invalid choice")




