import random

name = input("Введите имя тамагочи: ")

# Параметры питомца
food = 100      # сытость
hp = 100        # здоровье
dirt = 0        # грязь (0 — чисто, 100 — очень грязно)
game = 100      # счастье / желание играть
money = 10000   # монеты

def show_status():
    #Выводит состояние питомца.
    print("\n" + "=" * 30)
    print(f" {name}")
    print(f" Сытость:  {food}/100")
    print(f"  Здоровье: {hp}/100")
    print(f" Чистота:  {100 - dirt}/100")
    print(f" Счастье:  {game}/100")
    print(f" Монеты:   {money}")
    print("=" * 30)

def clamp(value, low=0, high=100):
    #Не даёт значению выйти за пределы [low, high].
    return max(low, min(high, value))

def check_death():
    #Проверяет, не погиб ли питомец
    if hp <= 0:
        print(f"\n {name} погиб... Игра окончена.")
        return True
    return False

#Действия питомца (случайные события)
def event_fall_in_puddle():
    global dirt
    print(f" {name} упал в лужу!")
    dirt = clamp(dirt + random.randint(25, 63))

def event_dirty_eating():
    global dirt
    print(f"  {name} испачкался во время еды.")
    dirt = clamp(dirt + random.randint(10, 30))

def event_hungry():
    global food, hp
    print(f" {name} проголодался и немного ослаб.")
    food = clamp(food - random.randint(10, 30))
    hp = clamp(hp - random.randint(1, 5))

def event_bored():
    global game
    print(f" {name} скучает.")
    game = clamp(game - random.randint(5, 20))

#Действия игрока
def feed():
    global food, dirt, money

    print(f"\n Чем покормить {name}?")
    print("1 — Лёгкий перекус   (+25, 25 монет)")
    print("2 — Сытный обед      (+50, 60 монет)")
    print("3 — Пир на весь мир  (+до 100, 120 монет)")

    choice = input("Ваш выбор: ").strip()

    # (порция, цена)
    if choice == "1":
        gain, price = random.randint(20, 25), 25
    elif choice == "2":
        gain, price = random.randint(45, 50), 60
    elif choice == "3":
        gain, price = 100, 120
    else:
        print(" Неизвестный выбор — кормление отменено.")
        return

    if money < price:
        print(f" Не хватает монет! Нужно {price}, а у вас {money}.")
        return

    money -= price
    food = clamp(food + gain)
    print(f" Вы покормили {name} (порция за {price} монет).")

    # шанс испачкаться при еде — 30%
    if random.random() < 0.3:
        event_dirty_eating()

def wash():
    global dirt
    dirt = clamp(dirt - random.randint(30, 60))
    print(f" Вы помыли {name}.")

def play():
    global game, food, money, dirt

    # Питомец и так рад, что с ним играют
    game = clamp(game + random.randint(15, 30))
    food = clamp(food - random.randint(5, 15))

    print(f"\n Вы играете с {name}. Какую игру выбрать?")
    print("1 — Обычная игра (растёт счастье)")
    print("2 — Пари на монеты (орёл/решка)")
    print("3 — Угадай число (приз за удачу)")

    mode = input("Ваш выбор: ").strip()

    #Режим 1: обычная игра
    if mode == "1":
        print(f" Вы просто поиграли с {name}. Настроение выросло!")

    #Режим 2: пари на монеты
    elif mode == "2":
        bet = min(money, 100)
        if bet <= 0:
            print(" Нечего ставить — монет нет.")
            return
        secret = random.randint(1, 2)
        print(f" {name} предлагает пари на {bet} монет: орёл(1) или решка(2)?")
        guess = input("Твой выбор: ").strip()
        if guess == str(secret):
            money += bet
            print(f" Победа! +{bet} монет.")
        else:
            money -= bet
            print(f" Проигрыш. -{bet} монет.")

    #Режим 3: угадай число
    elif mode == "3":
        print(f" {name} загадал число от 1 до 5. Угадай!")
        try:
            guess = int(input("Твоё число: ").strip())
        except ValueError:
            print(" Нужно ввести число.")
            return
        secret = random.randint(1, 5)
        if guess == secret:
            prize = random.randint(50, 150)
            money += prize
            print(f" Угадал! Число было {secret}. +{prize} монет.")
        else:
            print(f" Мимо. Было {secret}. Питомец расстроился.")
            game = clamp(game - random.randint(1, 5))

    else:
        print(" Неизвестная игра — просто поболтали.")
def heal():
    global hp, money
    if money < 200:
        print(" Не хватает монет на лечение!")
        return
    money -= 200
    hp = clamp(hp + random.randint(15, 30))
    print(f" Вы полечили {name}.")

# Основной цикл 
print(f"\nДобро пожаловать! Заботьтесь о {name}.\n")

turn = 0
while True:
    turn += 1
    print(f"\n Ход {turn} ")

    # 1. Случайное событие с питомцем (шанс ~50%)
    if random.random() < 0.5:
        event = random.randint(1, 4)
        if event == 1:
            event_fall_in_puddle()
        elif event == 2:
            event_dirty_eating()
        elif event == 3:
            event_hungry()
        elif event == 4:
            event_bored()

    # 2. Естественное угасание параметров каждый ход
    food = clamp(food - random.randint(1, 5))
    game = clamp(game - random.randint(1, 5))
    if dirt > 70:
        hp = clamp(hp - random.randint(1, 3))  # грязь вредит здоровью
    if food < 20:
        hp = clamp(hp - random.randint(1, 3))  # голод вредит здоровью

    show_status()

    if check_death():
        break

    # 3. Меню игрока
    print("Что будем делать?")
    print("1 —  Покормить ")
    print("2 —  Помыть")
    print("3 —  Поиграть")
    print("4 —  Полечить (200 монет)")
    print("0 —  Выйти из игры")

    choice = input("Ваш выбор: ").strip()

    if choice == "1":
        feed()
    elif choice == "2":
        wash()
    elif choice == "3":
        play()
    elif choice == "4":
        heal()
    elif choice == "0":
        print(f" Вы вышли из игры. {name} будет скучать!")
        break
    else:
        print(" Неизвестная команда, ход пропущен.")

    # Проверка смерти после действий
    if check_death():
        break