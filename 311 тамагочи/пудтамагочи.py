import random

food = 100
dirt = 0
age = 0

food_menu = {"1": "пицца",
             "2": "брокколи"}

play_menu = {"1": "мяч",
             "2": "лазерная указка"}

name = input("Имя вашего питомца:")

while True:
    act = random.randint(1, 4)
    if act == 1:
        food -= random.randint(10, 30)
        if food < 0:
            food = 0

    if act == 2:
        print(name, "упал в лужу")
        dirt += 50
        if dirt > 100:
            dirt = 100

    if act == 3:
        age += 1

    if food == 0:
        print(f"{name} погиб в бою с голодом")
        break

    if dirt == 100:
        print(f"{name} зарос грязью и сбежал на помойку")
        break

    if age >= 25:
        print(f"{name} прожил долгую жизнь и ушел на пенсию")
        break

    if age < 5:
        stage = "Малыш"
    elif age < 15:
        stage = "Взрослый"
    else:
        stage = "Старейшина"

    print(f"{name}")
    print(f"стадия: {stage}")
    print(f"возраст: {age}")
    print(f"голод: {food}")
    print(f"грязь: {dirt}")

    print("feed - кормить")
    print("wash - мыть питомца")
    print("play - играть")
    
    act = ""
    while act not in ["feed", "wash", "play"]:
        act = input("=")
        
    if act == "feed":
        print("чем будем кормить?")
        print("1 - пицца")
        print("2 - брокколи")
        eda = ""
        while eda not in ["1", "2"]:
            eda = input("=")
        eda = food_menu[eda]

        rnd = random.randint(1, 100)
        if 1 <= rnd <= 40:
            food = min(food + 60, 100)
            print(f"{name} поел {eda}")
        elif 40 < rnd <= 80:

            
            food = min(food + 60, 100)
            print(f"{name} поел, но немного запачкался")
            dirt = min(dirt + random.randint(1, 40), 100)
        else:
            print(f"{name} надел {eda} на голову")
            dirt = min(dirt + random.randint(50, 80), 100)

    if act == "wash":
        dirt = 0
        print(f"{name} помыт")

    if act == "play":
        print("во что будем играть?")
        print("1 - мяч")
        print("2 - лазерная указка")
        igrushka = ""
        while igrushka not in ["1", "2"]:
            igrushka = input("=")
        igrushka = play_menu[igrushka]

        rnd = random.randint(1, 100)
        if 1 <= rnd <= 50:
            food = max(food - 15, 0)
            print(f"{name} весело побегал за инструментом {igrushka}")
        elif 50 < rnd <= 85:
            food = max(food - 20, 0)
            dirt = min(dirt + 30, 100)
            print(f"{name} слишком активно играл в {igrushka} и залез под шкаф за грязью")
        else:
            print(f"{name} сломал {igrushka} и загрустил")
