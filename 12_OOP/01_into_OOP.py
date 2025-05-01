# Вступ в ООП
# ============визначення класу=======
from typing import overload
class Human:
    """Клас Людина"""
    # змінні (атрибути) класу
    count_human=0
    info_human="You are human!!!"
    # properties, fields, attr => атрибути екземпляра класу
    # def __init__(self):
    #     self.name="Olga"
    #     self.age=20
    # конструктор
    def __init__(self, name="Olga", age=20):
        self.name=name
        self.age=age
        Human.count_human+=1
        print(f"Created new human #{Human.count_human}!")

    # деструктор
    def __del__(self):
        Human.count_human-=1
        print(f"Last {Human.count_human} humans!")

    # метод екземпляра класу
    def print_info(self):
        print(f"human => {self.name} {self.age}")

    def say_something(self,words="Hello"):
        print(f'{self.name} say: "{words}" ')

    # рядкове представлення обєкта для використання фунцією print
    def __str__(self):
        return f"Human {self.name} has {self.age} yeas old!"

    # рядкове представлення обєкта, що використовуються для create by function repr
    def __repr__(self) -> str:
        return f"Human({self.name},{self.age})"
# =============використання класу==========
human1 = Human()
# Human.count_human+=1
human2= Human()
# Human.count_human+=1
print(human1.count_human) # не бажаний спосіб
print(human2.count_human) # не бажаний спосіб
print(Human.count_human) #бажаний спосіб
human1.count_human=7
print(human1.count_human)
print(human2.count_human)
print(Human.count_human)
# ============================
print(f"human1 => {human1.name} {human1.age}")
human2.age=21
human2.name="Oksana"
print(f"human2 => {human2.name} {human2.age}")
# ============ виклик конструктора з аргументами =========
human3=Human("Ігор",22)
human4=Human(age=21,name="Дмитро")
print(f"human3 => {human3.name} {human3.age}")
print(f"human4 => {human4.name} {human4.age}")
print(human3) # without __str__  =>  <__main__.Human object at 0x0000027678AA5F90>
print(human4) # without __str__  =>  <__main__.Human object at 0x000002767889B100>

# list1=list([3,4,5])
# print(list1)
# Human.print_info() #without self
human1.print_info()
human2.print_info()

# without __repr__ [<__main__.Human object at 0x000001AECEE31160>, <__main__.Human object at 0x000001AECEDB5090>, <__main__.Human object at 0x000001AECEDB5F90>, <__main__.Human object at 0x000001AECEBAB100>]
group_humans=[human1,human2, human3, human4] 
print(group_humans)
print("Виведення інформації про людей із group_humans:")
for human in group_humans:
    print(human)

# deleted obj
del human3 
human_with_repr=human1
print(id(human_with_repr))
print(id(human1))

human_with_repr=repr(human1) #new object
print(id(human_with_repr))
print(id(human1))

human2.say_something("Hi, how are you")
# NameError: name 'human3' is not defined. Did you mean: 'human1'?
# human3.say_something("I am fine!") 
human4.say_something("So-so!")
human1.say_something()