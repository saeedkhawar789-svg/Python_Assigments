#Q1 Variable Declaration and Printing.

a=1
b=2
c=3

print(a,b,c)

#Q2 Sum of Three Numbers.

a=1
b=2
c=3
x=a+b+c
print("sum:",x)

#Q3 Swapping of Two Variables.

x=10
y=20

temp=x
x=y
y=temp

print(x,y)

#Q4 List of Subjects (Indexing & Loop).

Subjects=["Math","Physics","Chemistry","Biology","English","Computer"]
print("First subject:",Subjects[0])
print("Last subject:",Subjects[-1])
print("All subjects:",Subjects)

for i in range(len(Subjects)):
    print(f"Subject {i+1}:",Subjects[i])

#Q5 Type Conversion (String to Integer & Float).

num_str="25"
num_int=int(num_str)
num_float=float(num_str)
print(type(num_str))
print(type(num_int))
print(type(num_float))