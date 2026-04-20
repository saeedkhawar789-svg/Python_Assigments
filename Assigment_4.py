# Q1: Check number is Positive, Negative or Zero.
def number(num):
    
    if num>0:
        return "Positive"
    elif num <0:
        return "Negative"
    else:
        return "Zero"

print(number(89))
print(number(-45))


# Q2: Grade calculator based on marks.
def grade(marks):

    if marks >= 80:
        return "A*"
    elif marks >= 70:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

print(grade(93)) 
print(grade(34))


# Q3: Electricity bill calculator.
def bill(units):
    if units> 300:
        return units*20
    elif units >=200:
        return units*15
    elif units >=100:
        return units*10
    else:
        return units*5

print(bill(200))
print(bill(300))


# Q4: Factorial and Fibonacci series.
def Factorial(num):
    result=1
    for i in range(1,num+1):
        result*=i
    return result

print(Factorial(7))


def Fibonacci(num):
    a, b = 0, 1
    for i in range(num):
        print(a, end=" ")
        a, b = b, a + b
   
Fibonacci(12)

print(number(67))

