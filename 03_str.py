import string
# Виконайте наступні дії із рядком:
row=string.ascii_lowercase
print(row)
# Спочатку виведіть третій символ цього рядка.
print(row[2])
# У другому рядку виведіть передостанній символ цього рядка.
print(row[-2])
# У третьому рядку виведіть перші п'ять символів цього рядка.
print(row[:5])
# У четвертому рядку виведіть весь рядок, крім останніх двох символів.
print(row[:-2])
print(row[:len(row)-2])

# У п'ятому рядку виведіть всі символи з парними індексами (вважаючи, що індексація починається з 0, тому символи виводяться починаючи з першого).
print(row[::2])
# У шостому рядку виведіть всі символи з непарними індексами, тобто починаючи з другого символу рядка.
print(row[1::2])
# У сьомому рядку виведіть всі символи в зворотному порядку.
print(row[::-1])
# У восьмому рядку виведіть всі символи рядка через один в зворотному порядку, починаючи з останнього.
print(row[::-2])
# У дев'ятому рядку виведіть довжину цього рядка.
print(f"Довжина рядка: {len(row)}")
print(f"adderes => {id(row)}")
row=row[:7]
print(f"adderes => {id(row)}")      
print(row)

for code in range(16,127):
    print(code,"=>",chr(code), end="; ")

print("\n",ord("A"))

import string
print(string.printable)

# from string import printable
# print(printable)
# Порахувати кількість цифр в реченні
print(string.punctuation)
print(string.digits)
print(string.ascii_uppercase)

row=input("Input row=")
print(string.capwords(row))
count_digit=0
count_punct=0
for symbol in row:
    if symbol in string.digits:
        count_digit+=1
    if string.punctuation.find(symbol)!=-1:
        count_punct+=1


print(f"Count digits: {count_digit}")
print(f"Count punctuations: {count_punct}")


row1="We are learning Python! We are super stars, we  are students!"
print(row1.center(30,"*"))
print(row1.find("ing"))
print(row1.find("ung"))
#Знайти всі входження слова "We" 
row1=row1.lower()
substr="we"
index=row1.find(substr)
len_substr=len(substr)
print(index)
count_substr=0
while index>-1:
    index=row1.find(substr,index+len_substr)
    count_substr+=1
    print(index)

else:
    print("The End!")

print(f'count "{substr}" in str "{row1}" => {count_substr}')

str_with_number="-456"
print(str_with_number.isalnum())
print(str_with_number.isdecimal())
print(str_with_number.isdigit())
print(str_with_number.isnumeric())
print(row1.count("we"))

row2=row1.center(70," ")
print(f"\"{row2}\"")
print(f"\"{row2.strip()}\"")

print(row1)
words=row1.split()
print(words)
str_new=""
# with replace punctuation => space
# for symbol in row1:
#     if (symbol in string.punctuation):
#         str_new+=" "
#     elif prev_s==" ":
#         continue
#     else:
#         str_new+=symbol
#     prev_s=symbol
prev_s=" "
for symbol in row1:
    if (symbol in string.punctuation) or (prev_s==" " and symbol==" "):
        continue
    else:
        str_new+=symbol
    prev_s=symbol
print(f"str_new => {str_new}")

words=str_new.split(" ")
print(words)
print(f"count words => {len(words)}")
