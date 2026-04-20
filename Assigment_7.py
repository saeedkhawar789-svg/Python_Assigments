print("Q 1,2")
#Q 1,2
class std:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def print_info(self):
        print(self.name,self.roll_no)

    def update_marks(self,marks):
        self.marks=marks

    def show_result(self):
        print("Marks:",self.marks)

s1=std("Ali:", 101)
s1.print_info()
s1.update_marks(85)
s1.show_result()
 
print("\nQ 3")
       
#Q 3
class person:
    def __init__(self,name):
        self.name=name

class teacher(person):
    def __init__(self,name,subject):
        self.name=name
        self.subject=subject

    def print_info(self):
        print(self.name,self.subject)

t1=teacher("My name is Ahmed","\nI teach Mathematics")
t1.print_info() 

print("\nQ 4")

#Q 4
class Father:
    def father_skill(self):
        print("Father skill: Driving")

class Mother:
    def mother_skill(self):
        print("Mother skill: Cooking")

class Child(Father,Mother):
    def show_skills(self):
        self.father_skill()
        self.mother_skill()

c1=Child()
c1.show_skills()

print("\nQ 6")

#Q 6
class BankAccount:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        if balance<0:
            self.balance=0
        else:
            self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"Deposited:{amount}")

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"Withdrawn:{amount}")
        else:
            print("Insufficient balance!")

    def display_info(self):
        print(f"Account Holder:{self.account_holder}")
        print(f"Balance:{self.balance}")

b1=BankAccount("Saeed Khawar", 2000)

b1.display_info()
b1.deposit(500)
b1.withdraw(100)
b1.display_info()

print("\nQ 5")

#Q 5
class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no

        if 0<= marks <=100:
            self.marks=marks
        else:
            self.marks=0

    def calculate_grade(self):
        if 80<=self.marks<=100:
            return "A"
        elif 60<= self.marks<=79:
            return "B"
        elif 40<= self.marks<=59:
            return "C"
        else:
            return "Fail"

    def display_info(self):
        print(f"Name:{self.name}")
        print(f"Roll No:{self.roll_no}")
        print(f"Marks:{self.marks}")
        print(f"Grade:{self.calculate_grade()}")


s1=Student("Ali",101,400)
s2=Student("Sara",102,72)
s3=Student("Khan",103,38)
s4=Student("Zara",104,150)  

s1.display_info()
print()

print("\nQ 7")
#Q7
class Patient:
    def __init__(self,name,age):
        self.name=name
        self.age=age


class Doctor():

    def __init__(self,name,specialization,availability):
        self.name=name
        self.specialization=specialization
        self.availability=availability



class Appointment:
    def __init__(self,patient,doctor):
        self.patient=patient
        self.doctor=doctor


class Surgeon(Doctor):
    def __init__(self,name,availability,surgery_fee):
        super().__init__(name,"Surgeon",availability)
        self.surgery_fee=surgery_fee

    



class Physician(Doctor):
    def __init__(self,name,availability,consultation_fee):
        super().__init__(name,"Physician",availability)
        self.consultation_fee=consultation_fee


class Bill:
    def __init__(self,appointment):
        self.appointment=appointment

    def calculate(self,hours=1):
        doc=self.appointment.doctor
        if isinstance(doc,Surgeon):
            return doc.surgery_fee*hours
        elif isinstance(doc,Physician):
            return doc.consultation_fee
        else:
            return 0



p1 = Patient("Saeed Khawar",17)
s1 = Surgeon("Dr.Sameen","yes",5000)
ph1 = Physician("Dr.Ali","yes",200)

appt1=Appointment(p1,s1)
appt2=Appointment(p1,ph1)

bill1=Bill(appt1)
bill2=Bill(appt2)


print(f"Bill for surgery:{bill1.calculate(2)}")
print(f"Bill for consultation:{bill2.calculate()}")
