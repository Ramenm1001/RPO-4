import random

# параметры
food = 100
dirt = 0

name = input("Имя вашего питомца:")

while True:
    # ход тамагочи
    act = random.randint(1, 3) # 33%
    if act == 1:
        # голод
        food -= random.randint(10, 30) # от 10 до 30
        if food < 0:
            food = 0

    if act == 2:
        # упал в лужу
        print(name, "упал в лужу")
        dirt += 50
        if dirt > 100:
            dirt = 100
        # dirt = min(dirt + 50, 100)

    # интерфейс
    print(f"{name}")
    print(f"голод: {food}")
    print(f"грязь: {dirt}")

    print("feed - кормить")
    print("wash - мыть питомца")
    act = ""
    while act not in ["feed", "wash"]:
        act = input("=")
    if act == "feed":
        rnd = random.randint(1, 100)
        if 1 <= rnd <= 40:
            food = min(food + 60, 100)
            print(f"{name} поел")
        elif 40 < rnd <= 80:
            food = min(food + 60, 100)
            print(f"{name} поел, но немного запачкался")
            dirt = min(dirt + random.randint(1, 40), 100)
        else:
            print(f"{name} надел кашу на голову")
            dirt = min(dirt + random.randint(50, 80), 100)

    if act == "wash":
        dirt = 0
        print(f"{name} помыт")




