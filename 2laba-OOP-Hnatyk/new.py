# 1 APP
a = "змінна з текстом"
b = 1 # числова Змінна
c = ["a", 1, 1.25, "Слово"] # List
d = {"a": "Слово", "b": 1} # Dict
e = ("a", ) # Tuple
f = {"ss", } # Set
print(f"Перша програма\nТип а - {type(a)}, тип b - {type(b)}, Тип c - {type(c)}, Тип d - {type(d)}, Тип e - {type(e)}, Тип f - {type(f)}.\n")
# 2 APP
print("Друга програма\nПерша константа", False)
# 3 APP
print("\nТретя прогрма")
print(abs(-12.5), f"є рівним {abs(12.5)}")
# 4 APP
print("\nЧетверта програма")
letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(f"На позиції {i} знаходиться буква {letters[i]}")
# 5 APP
A = True
print("\nп'ята програма\nЗначить А=True" if A else "Значить А=False")
# 6 APP
print("\nШоста програма")
A = 0
print(f"Ділимо 10/{A}")
try:
    print(f"А = 0...", 10/A)
except Exception as e:
    print("Ділення на 0. Неможна так, в школі вчились, нє?")
finally:
    A = input("Якесь число яке не дорівнює 0 напиши ")
    try:
        A = int(A)
    except:
        print("Сарянчік, але тебе не виправити. ББ")
    try:
        print(f"А так мона. Маладєц! Результат - {int(10/A)}")
    except:
        exit

# 7 APP
print('\nСьома програма')
# Додам всі лінії в список, щоби не засирати весь термінал
lasd = []
with open("D:\\STUDY OOP\\STUDY-OOP\\2laba-OOP-Hnatyk\\README.md", "r") as f:
    for line in f:
        lasd.append(line)
# Тут можна любу строку вививести as you know, або взагалі весь лист, але мені шкода терміналу і скріни будуть не красиві. Тому вивожу 14 (15) рядок, бо там норм симовли інакше будуть не панятні якісь знаки питань
print(lasd[14])

# 8 APP
print("\nВосьма програма")
funct = lambda name, surname: f"{name} {surname} Дуже погано спав сьогодні. Пожалійте його, поставте 5 балів ツ"
print(funct("Денис", "Гнатик"))

# Бонусна програма
print("\nБонусна програма")
import random, os
try:
    qus = input("Чи готові ви зіграти в українську рулетку? (Відповідь y = yes, n = no) ")
    if qus != "N" and qus != "n" and qus != "y" and qus != "Y":
        print(f"{os.getlogin()} не попав по клавіатурі. АХАХАХ куда тобі в ігри грати? Йди моторику рук вкачай.")
except:
    pass
if qus == "y" or qus == "Y":
    print(f"Ого. {os.getlogin()} сміливий!")
    rand = random.randint(0,7)
    sug = int(input(f"Давай, вибирай число від 0 до 7, {os.getlogin()} "))
    if sug == rand:
        print("Вітаю! Ти мертвий. Як так-то? 1/7 шанс і він прокнув... В казино б ше так везло, як тут. Чи не так? ")
    if sug != rand:
        print("Ти програв. Дуже неочікувано, тбх.")
if qus == "n" or qus == "N":
    print("ХАХАХАХАХАХАХ чувак злякався програми на пайтоні. Сходи в качалку, може там сміливість підцепиш, бо ну це крінжа якась...")
    