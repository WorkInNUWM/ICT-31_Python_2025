import math
print("Hello")
print("Hi")

x=34
print(x.bit_count())
y=bin(x)
print(y)
print(x.bit_length())
print(x.to_bytes())
print(ord("a"))
print(chr(98))

print(complex(2+5j))
print(eval("3+4*6/2"))
print(sum([2,3,4]))

x=input("x=")
print(type(x),x)
x=int(x)
print(type(x),x)

y=int(input("y="))
# print("rez=",x+y, sep="", end="\t")
print(x,"/",y,"=",x/y, sep="")
print("Дано числа {0}, {1} => {0}/{1}={2:*^10,.2f}!".format(x,y,x/y))
print("Дано числа %d, %d => %d/%d=%5.2f!"%(x,y,x,y,x/y))
# print("x/y=x/y".format(x,y,x/y), sep="")
print("rez3=",math.log(x,y), sep="")
n=3456789
print(f"Число {n}^2={n**2:@^30_d}!")


