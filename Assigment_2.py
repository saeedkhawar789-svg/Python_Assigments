#list 

my_list=["apple","banana","kiwi","orange","mango","peach"]

#a
my_list.append("grapes")
#b
my_list.insert(2,"pineapple")
#c
my_list.remove("kiwi")
#d
my_list[my_list.index("banana")]="banana juice"
#e
print(my_list[:4])
#f
print(my_list[::-1])


#task 2

my_num=[1,2,3,4,5,6,7,8,9,10]

#a
print("Even numbers:")
for n in my_num:
    if n%2==0:
        print(n)
#b
my_num.pop()
print(my_num)
#c
my_num.extend([11,12,13])
print(my_num)
#d
my_num.sort(reverse=True)
print(my_num)


#Tuple

my_tuple=(10,20,50,40,53,20,10)

#a
print(my_tuple.count(20))
#b
print(my_tuple.index(40))
#c
temp=list(my_tuple)
temp[temp.index(50)]=500
my_tuple=tuple(temp)
print(my_tuple)


#task 2 

t1=("A","B","C")
t2=(1,2,3)

#a
print(t1+t2)
#b
print(t1*3)
#c
print("B"in t1)


#Set

my_set={"red","blue","green"}

#a
my_set.add("yellow")
print(my_set)
#b
my_set.update(["black","white"])
print(my_set)
#c
my_set.remove("green")
print(my_set)
#d
try:
    my_set.remove("pink")
except KeyError:
    print("Color does not exist")

# e
set1 = {1,2,3}
set2 = {3,4,5}
print(set1|set2)


#task 2

user_set=set()

for i in range(5): #add 5 number for user input
    user_set.add(int(input()))

#a
user_set.add(next(iter(user_set)))

#b
print(len(user_set))

#c
print(max(user_set))
print(min(user_set))

#Dictionary

my_data={
    "brand":"Toyota",
    "model":"Corolla",
    "year":2020
}

#a
my_data["year"]=2024
#b
my_data["color"]="white"
#c
print(my_data.keys())
#d
print(my_data.values())
#e
my_data.pop("model")
#f
for k,v in my_data.items():
    print(k,v)


#task 2

students={
    "Muhammad":85,
    "Saeed":92,
    "khawar":78
}

#a
for s in students:
    students[s]+=5

#b
for s,m in students.items():
    if m>80:
        print(s)
#c
students["Ali"]=90
#d
for s,m in students.items():
    print(s,m)


