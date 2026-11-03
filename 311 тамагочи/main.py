import random

# параметры
food = 100
dirt = 0
energy = 100
happiness = 100  # Добавлено: счастье
days_alive = 0  # Добавлено: счетчик прожитых дней

food_menu = {"1": "пицца", "2": "брокколи"}
name = input("Имя вашего питомца: ")

while True:
    days_alive += 1  # Питомец прожил еще один день

    # ход тамагочи (случайные события в начале круга)
    act = random.randint(1, 5)  # Расширили пул событий

    if act == 1:
        # голод
        food = max(food - random.randint(10, 30), 0)
        energy = max(energy - random.randint(5, 15), 0)
        happiness = max(happiness - 10, 0)  # Голодный питомец грустит
        print(f"\n{name} проголодался и немного устал.")

    elif act == 2:
        # упал в лужу
        print(f"\n{name} упал в лужу!")
        dirt = min(dirt + 50, 100)
        happiness = max(happiness - 15, 0)  # Никому не нравится падать в лужи

    elif act == 3:
        # питомец заболел, если он слишком грязный
        if dirt > 70:
            print(f"\n{name} заболел из-за грязи! Он теряет здоровье и силы.")
            food = max(food - 20, 0)
            energy = max(energy - 30, 0)
            happiness = max(happiness - 30, 0)
        else:
            print(f"\n{name} весело бегает по комнате.")
            energy = max(energy - 10, 0)
            happiness = min(happiness + 10, 100)

    elif act == 4:
        # Питомец соскучился
        print(f"\n{name} заскучал без вашего внимания.")
        happiness = max(happiness - 20, 0)

    if act == 5:
        #Скучно питомцу
        print(name, "скучает")
        happiness -= random.randint(20, 55)
        if happiness < 0:
            happiness = 0

    # интерфейс
    print("-" * 30)
    print(f"Имя: {name} | Прожито дней: {days_alive}")
    print(f"Голод: {food}/100")
    print(f"Грязь: {dirt}/100")
    print(f"Энергия: {energy}/100")
    print(f"Счастье: {happiness}/100")  # Выводим счастье в интерфейс
    print("-" * 30)

    print("feed  - кормить")
    print("wash  - мыть питомца")
    print("play  - играть")
    print("sleep - уложить спать")

    user_act = ""
    while user_act not in ["feed", "wash", "play", "sleep"]:
        user_act = input("Действие = ").strip().lower()

    # МЕХАНИКА: Кормление
    if user_act == "feed":
        print("Чем будем кормить?")
        print("1 - пицца")
        print("2 - брокколи")
        eda = ""
        while eda not in ["1", "2"]:
            eda = input("Выбор = ")
        eda = food_menu[eda]

        rnd = random.randint(1, 100)
        if 1 <= rnd <= 40:
            food = min(food + 60, 100)
            happiness = min(happiness + 15, 100)  # Вкусная еда радует
            print(f"{name} с удовольствием съел {eda}!")
        elif 40 < rnd <= 80:
            food = min(food + 60, 100)
            print(f"{name} поел {eda}, но жутко испачкался.")
            dirt = min(dirt + random.randint(1, 40), 100)
        else:
            print(f"{name} не захотел есть и надел {eda} на голову!")
            dirt = min(dirt + random.randint(50, 80), 100)
            happiness = max(happiness - 10, 0)

    # МЕХАНИКА: Мытье
    elif user_act == "wash":
        dirt = 0
        energy = max(energy - 10, 0)
        print(f"{name} теперь чистый и блестит!")

    # МЕХАНИКА: Игра
    elif user_act == "play":
        if energy < 20:
            print(f"{name} слишком устал, чтобы играть! Сначала уложите его спать.")
        else:
            print(f"Вы поиграли с {name} в мяч!")
            energy = max(energy - 25, 0)
            dirt = min(dirt + 15, 100)
            food = max(food - 15, 0)
            happiness = min(happiness + 35, 100)  # Игры сильно поднимают счастье

    # МЕХАНИКА: Сон
    elif user_act == "sleep":
        print(f"{name} свернулся клубочком и уснул...")
        energy = 100
        food = max(food - 20, 0)
        happiness = min(happiness + 5, 100)  # Сон немного восстанавливает настроение

    # Условия поражения
    if food <= 0:
        print(f"\n{name} погиб в бою с голодом... Игра окончена.")
        print(f"Вы смогли заботиться о нем рекордное количество дней: {days_alive}!")
        break

    if energy <= 0 and food < 20:
        print(f"\n{name} упал от полного бессилия и истощения... Игра окончена.")
        print(f"Вы смогли заботиться о нем рекордное количество дней: {days_alive}!")
        break

    if happiness <= 0:
        print(f"\n{name} обиделся на вас и убежал искать лучшую жизнь... Игра окончена.")
        print(f"Вы смогли заботиться о нем рекордное количество дней: {days_alive}!")
        break





