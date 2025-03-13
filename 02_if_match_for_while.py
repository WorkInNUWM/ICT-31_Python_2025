import random



"""
if вираз:  #твердження:  "Python", 23, true => true;   "", 0, None, false => false, логічні вирази (>,<,==,!=...  and or not in is)
    командна1
else:
    команда2
"""

"""
if вираз1:
    командна1
elif вираз2:
    команда2
...
else:
    команда N
"""

"""
тернарний оператор
"""

n1=5
n2=7
maximum = n1 if n1>n2 else n2
print(f'maximum({n1},{n2})={maximum}')

"""
maximum=> a,b,c
"""

a=5
b=34
c=-34
print("max =",max(a,b,c))
if a>b and a>c:
    max1=a
elif b>c and b>a:
    max1=b
elif c>a and c>b:
    max1=c
else:
    max1=a
    print("Всі числа рівні.")

print(f'max1({a},{b},{c}) => {max1}')


if "":
    print("it is fact")
else:
    print("it is empty")


"""
Python 3.10 => match
"""
number_day=int(input("Input number of day: "))
match number_day:
    case 1:
        print("Working day")
        print("It's not very good...")
    case 2:
        print("Working day")
    case 6:
        print("Holiday")
    case 7:
        print("Holiday")
    case _:
        print("Error!!!")

print("Next operator after match")

match number_day:
    case 1|2|3|4|5:
        print("Working day")
        print("It's not very good...")
    case 6|7:
        print("Holiday")
    case _:
        print("Error!!!")

print("Next operator after match")

a=1
b=10
suma=0
while a<=b:
    suma+=a
    print(f"a={a} suma={suma}")
    a=a+1
else:
    print("Good work!")

# using continue and break
a=1
b=10
suma=0
number=random.randint(1,10)
while a<=b:
    if a==7:
        a+=1
        continue
    if a==number:
        print(f"random number={number}")
        break
    suma+=a
    print(f"a={a} suma={suma}")
    a=a+1
else:
    print("Good work!")


"""
for змінна in послідовність:
    тіло циклу (команди ітерації)
else:
    команди (виконуються після успішного виконання циклу)
"""

"""
range(start, stop[, step]) -> range object
"""

print(range(3))
print(list(range(3)))

for number in range(3): # 0,1,2
    print(number)

print("*"*40)
for number in range(10): # 0,1,2,..,9
    print(number, end=" ")
else:
    print()


print("*"*40)
for number in range(1,11): # 1,2,..,9,10
    print(number, end=" ")
else:
    print()

print("*"*40)
for number in range(1,11,2): # 1,3,..,9
    print(number, end=" ")
else:
    print()

print("*"*40)
for number in range(10,0,-1): # 10,9,...m 1
    print(number, end=" ")
else:
    print()

# ==============================
print("$"*30)
number=random.randint(1,10)
for a in range(1,11):
    if a==7:
        a+=1
        continue
    if a==number:
        print(f"random number={number}")
        break
    suma+=a
    print(f"a={a} suma={suma}")
    a=a+1
else:
    print("Good work!")



# working sequence=> string

for symbol in "We are learning Python":
    print(symbol,end="$")
else:
    print()

