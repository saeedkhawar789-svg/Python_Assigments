# Q1: Calculator using math module
import math

print("<<Menue>>")
print("1. Square Root")
print("2. Power")
print("3. Factorial")
print("4. Ceil")
print("5. Floor")
print("6. Exit")

calc = int(input("Choose operation: "))

num = float(input("Enter a number: "))

if calc == 1:
    print(math.sqrt(num))

elif calc == 2:
    p = float(input("Enter power: "))
    print(math.pow(num, p))

elif calc == 3:
    print(math.factorial(int(num)))

elif calc == 4:
    print(math.ceil(num))

elif calc == 5:
    print(math.floor(num))

elif calc == 6:
        print("exit")

else:
    print("Invalid choice ")


from datetime import datetime
import time

while True:
    now = datetime.now()      
    current_time = now.strftime("%H:%M:%S")
    print("Current Time:", current_time)
    
    current_date = now.strftime("%Y-%m-%d")
    print("Current Date:", current_date)
    
    year = now.year
    print("Year:", year)

    month = now.month
    print("Month:", month)

    time.sleep(1)
    




  
    
    


















import datetime
import time
print(datetime.date.today())

while True:
    now=datetime.datetime.now()
    print(now.strftime("%H,%M,%S"))
    time.sleep(1)