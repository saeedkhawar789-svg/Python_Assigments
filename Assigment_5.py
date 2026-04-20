#Q2
def outer(a,b):
    def inner():
        return a+b
    result=inner()+5
    return result
    
print(outer(12,2))

#Q3
def num_sum(n):
    if n==0:
        return 0
    else:
        return n+num_sum(n-1)

print(num_sum(10))

#Q1

def Palindrome_num():
    num=input("Enter a Number:")
    rev=num[::-1]
    if num==rev:
       print("Palindrome")
    else:
       print("Not Palindrome")

Palindrome_num()

#Q4
def leap(year):
    if year%400==0:
        print("Leap Year")
    elif year%100==0:
        print("Not a Leap Year")
    elif year%4==0:
        print("Leap Year")
    else:
        print("Not a Leap Year")

year=int(input("Enter a year:"))
leap(year)


# Q5
def even_num():
    n=int(input("Enter a number:"))
    for i in range(1,n+1):
        if i%2==0:
            print(i,end=" ")
    print()

def table(n,i=1):
    if i>10:
       return
    print(n*i)
    table(n,i+1)

def calculator():
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    op=input("Enter operator(+,-,*,/,avg,pow,%):")

    def div():
        if num2!=0:
            print("Division=",num1/num2)
        else:
            print("Cannot divide by zero")

    def average():
        print("Average=",(num1+num2)/2)

    def power():
        print("Power=",num1**num2)

    def percentage():
        if num2!=0:
            print("Percentage=",(num1/num2)*100)
        else:
            print("Cannot calculate percentage")

    if op=="+":
        print("Sum=",num1+num2)
    elif op=="-":
        print("Difference=",num1-num2)
    elif op=="*":
        print("Product=",num1*num2)
    elif op=="/":
        div()
    elif op=="avg":
        average()
    elif op=="pow":
        power()
    elif op=="%":
        percentage()
    else:
        print("Invalid operator")



def large_num():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=int(input("Enter third number: "))

    if a>=b and a>=c:
        print("Largest number=",a)
    elif b>=a and b>=c:
        print("Largest number=",b)
    else:
        print("Largest number=",c)


#MENU 
while True:
    print("1.Print even numbers up to N")
    print("2.Print multiplication table")
    print("3.Calculator")
    print("4.Find largest among three numbers")
    print("5.Exit")

    choice=int(input("Enter your choice:"))

    match choice:
        case 1:
            even_num()
        case 2:
            n=int(input("Enter a number: "))
            table(n)
        case 3:
            calculator()
        case 4:
            large_num()
        case 5:
            print("Program terminated")
            break
        case _:
            print("Invalid choice")
            
