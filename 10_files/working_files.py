import shelve
import os


"""
   ['Python', 'Guido van Rossum'],
    ['Scala', 'Martin Odersky'],
    ['PHP', 'Rasmus Lerdorf'],
    ['Ruby', 'Yukihiro Matsumoto'],
    ['C', 'Dennis Ritchie'],
"""

filename = "10_files\\shelve_ex"
# # working with files for dictonary, record dict
# with  shelve.open(filename, 'c') as shelve_wr:
#     shelve_wr['Python'] = 'Guido van Rossum'
#     shelve_wr['Scala'] = 'Martin Odersky'
#     shelve_wr['C'] = 'Dennis Ritchie'

# with shelve.open(filename, 'r') as shelve_r:
#     key="Scala"
#     if key in shelve_r:
#         print(shelve_r[key])
#     print(shelve_r['Python'])
#     print(shelve_r['C'])

# with shelve.open(filename, 'r') as shelve_r:
#     value=shelve_r.get("C")
#     print(value)
#     value2=shelve_r.get("C++","None")
#     print(value2)


# with shelve.open(filename, 'r') as shelve_r:
#     for key in shelve_r:
#         print(key," ",shelve_r[key])


# with shelve.open(filename, 'r') as shelve_r:
#     for avtor in shelve_r.values():
#         print(avtor)

# with shelve.open(filename, 'c') as shelve_wandr:
#     shelve_wandr["C"]="Ritchie"


# with shelve.open(filename, 'r') as shelve_r:
#     for avtor in shelve_r.values():
#         print(avtor)


# os.mkdir("example1")
# os.mkdir("E:\\Example1")
# os.mkdir("E://Example1//exam")
if os.path.exists("E://Example1/exam/f2.txt"):
    os.rename("E://Example1/exam/f2.txt","E://Example1/exam/f1.txt")
else:
    print("ERROR")


filename="E:/Example1/exam/f1.txt"
with open(filename,'rt') as fileR:
    # rez=fileR.read()
    rez=fileR.readlines()

# print(rez)
print("*"*30)
with open("listSt.txt",'wt') as fileW:
    for row in rez:
        # print(row.rstrip("\n"))
        listInfo=row.rstrip("\n").split()
        # print(listInfo)
        if len(listInfo)>2:
            if len(listInfo[2])>=2:
                listInfo[1]=listInfo[1].upper()
            fileW.write(f"{listInfo[1]} {listInfo[2]} \n")
        # print(listInfo)

# print(rez)

