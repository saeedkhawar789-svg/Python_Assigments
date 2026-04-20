#1 Login System (Username & Password Check).
while True:
    user = str(input("Enter username:"))
    password =int(input("Enter password:"))
    if password != 1234:
        print("wrong password,try again")
        continue
    if user == "admin":
        print("welcome admin")
    else:
        print("welcome user")
    break

#2 Print Even Numbers (1 to 10).
for i in range(1,11):
    if i %2!= 0:
        continue
    print(i)


#3 Marks Grading System (Pass/Fail/Excellent).
for i in range(5):
    marks=int(input("marks:"))
    if marks<0: 
        if marks>100:
            continue
    if marks>=80:
        print("Excellent")
    elif marks >= 40:
        print("Pass")
    else:
        print("Fail")

#4 Password Attempts (3 Tries Login System).
password="1234"
attempts=0
while attempts<3:
    user=input("enter password:")
    if user == password:
        print("Acces granted")
        break
    else:
        print("Acces denied")
        attempts+=1

#5 Number Search in Range (1 to 20).
num = int(input("Enter a number:"))
for i in range(1,21):
    if i == num:
        print("num given")
        break
else:
    print("Num are not given")
  
#6 Age Category Checker (Minor/Adult/Senior).
for i in range(5):
    age = int(input("Age:"))
    if age < 0:
        continue
    elif age >= 60:
        print("Senior")
    elif age > 18:
        print("Adult")
    else:
        print("Minor")

#7 Even Number Filter Until -1 Stop.
while True:
    num = int(input("Number:"))
    if num == -1:
        break
    if num %2!= 0:
        continue








