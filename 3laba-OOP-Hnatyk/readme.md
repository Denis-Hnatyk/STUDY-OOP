# Звіт до роботи
## Тема: Знайомство з ООП
### Мета роботи: Ознайомитись з об'єктами та властивостями class в мові програмування Python
---
### Виконання роботи
- Результати виконання завдання;
    1. Створили свій клас "MyName":
```python
import random
import string
class MyName:
    total_names = 0 

    def __init__(self, name=None) -> None:
        self.name = name if name is not None else "Anonymous"  
        MyName.total_names += 1  
        self.my_id = self.total_names

    @property
    def whoami(self):
        """Class property
        return: повертаємо імя 
        """
        return f"My name is {self.name}"

    @property
    def my_email(self) -> str:
        """Class property
        return: повертаємо емейл
        """
        return self.create_email()

    def create_email(self) -> str:
        """Instance method
        """
        return f"{self.name.lower()}@itcollege.lviv.ua"

    @classmethod
    def anonymous_user(cls):
        """Class method
        """
        return cls("Anonymous")  

    @staticmethod
    def say_hello(message="Hello to everyone!"):
        """Static method
        """
        return f"You say: {message}"
    
    def crpass(le= 8):
        """Створення паролю, унікального для кожної людини
        """
        characters = string.ascii_letters + string.digits + string.punctuation #бібліотека string дає можливість вибрати рандомний символ
        return ''.join(random.choice(characters) for _ in range(le))


names = []
ans = "1"
while ans == "1":
    q = input("Введіть ім'я людини: ")
    q = q.replace(" ", "").lower()
    if q == "":
        q = MyName.anonymous_user().name 
    names.append(q)
    ans = input("Продовжуємо? (1/0) ")
print("\n")
imena = {name: MyName(name) for name in names}
for name in imena:
    print(f"Привіт, {name}!\nТвоя електронна пошта - {imena[name].create_email()}.\nТвій унікальний пароль - {MyName.crpass()}!\n")

print(f"Загальна кількість користувачів = {MyName.total_names}")
"""Бляха це ж можна було через while зробити. Бож чо я тік зараз допер.............. Нічого, так тоже норм"""
#print("Let's Start!") - Пише "Let`s start" в консоль
#names = ("Bohdan", "Marta", None) - Вказуємо Імена, які використовуються в класі
#all_names = {name: MyName(name) for name in names} - Створює окремий об'єкт для кожного імені
#
#for name, me in all_names.items(): - виводиму інфу про кожне ім'я тудимс-сюдимс
#    print(f"""{">*<"*20} 
#This is object: {me}  
#This is object attribute: {me.name} / {me.my_id} 
#This is {type(MyName.whoami)}: {me.whoami} / {me.my_email} 
#This is {type(me.create_email)} call: {me.create_email()} 
#This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
#This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names} 
#{"<*>"*20}""") 
#
#print(f"We are done. We create {me.total_names} names! ??? Why {MyName.total_names}?") - Виводить імена всі, які створили
"""Закоментував весь код, щоб написати свій xD
Додав коментарі, які показують розуміння, що за що відповідає"""
```
    1. Програма вивела значення:
![alt text](https://github.com/BobasB/it_college/raw/main/reports/pictures/logo-lit.jpg "ІТ Коледж")

    1. Результат у текстовому форматі
```text
Введіть ім'я людини: Denis Hnatyk
Продовжуємо? (1/0) 1
Введіть ім'я людини: Oleg Vanivskiy
Продовжуємо? (1/0) 1
Введіть ім'я людини: Petya Pyatochkin
Продовжуємо? (1/0) 1
Введіть ім'я людини: Ольга Василівна
Продовжуємо? (1/0) 1
Введіть ім'я людини: 
Продовжуємо? (1/0) 0


Привіт, denishnatyk!
Твоя електронна пошта - denishnatyk@itcollege.lviv.ua.    
Твій унікальний пароль - wm_&w:[=!

Привіт, olegvanivskiy!
Твоя електронна пошта - olegvanivskiy@itcollege.lviv.ua.  
Твій унікальний пароль - wMYK'4n*!

Привіт, petyapyatochkin!
Твоя електронна пошта - petyapyatochkin@itcollege.lviv.ua.
Твій унікальний пароль - 5xI1o02>!

Привіт, ольгавасилівна!
Твоя електронна пошта - ольгавасилівна@itcollege.lviv.ua. 
Твій унікальний пароль - 9wi<s#rk!

Привіт, Anonymous!
Твоя електронна пошта - anonymous@itcollege.lviv.ua.      
Твій унікальний пароль - d,.&%r\2!

Загальна кількість користувачів = 6
```
    1. Початковий код дав наступний результат:
![alt text](https://github.com/BobasB/it_college/raw/main/reports/pictures/logo-lit.jpg "ІТ Коледж")
### Висновок: 

Під час виконання цієї роботи, я ознайомився з об'єктами та властивостями class в мові програмування Python