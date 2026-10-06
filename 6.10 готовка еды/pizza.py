#by Yaromir Knelc
YES = {"да", "д", "yes", "y", "1"}
NO = {"нет", "н", "no", "n", "2"}

INGREDIENTS = {
    "мясо": 120,
    "сыр": 80,
    "колбаса": 100,
    "грибы": 70,
    "помидоры": 50,
    "перец": 60,
    "оливки": 90,
    "лук": 40,
    "ананас": 110,
    "бекон": 130,
}

base_price = 250
total_price = base_price
pizza = {}

print("Конструктор пиццы")
print(f"Базовая цена пиццы: {base_price} руб.")
print("Доступные ингредиенты:")
for name, price in INGREDIENTS.items():
    print(f"  {name} - {price} руб.")

while True:
    ing = input("Какой ингредиент добавить? (или 'готово' для завершения): ").strip().lower()

    if ing in {"готово", "конец", "стоп", "finish", "exit"}:
        break

    if ing not in INGREDIENTS:
        print("Такого ингредиента нет. Попробуй снова.")
        continue

    while True:
        qty = input(f"Сколько порций '{ing}'? (1 / 2=дабл / 3=трипл): ").strip().lower()

        if qty in {"1", "один", "обычный", "single"}:
            mult = 1
        elif qty in {"2", "два", "дабл", "double"}:
            mult = 2
        elif qty in {"3", "три", "трипл", "triple"}:
            mult = 3
        else:
            print("Введи 1, 2 или 3.")
            continue
        break

    pizza[ing] = pizza.get(ing, 0) + mult
    cost = INGREDIENTS[ing] * mult
    total_price += cost
    print(f"Добавлено: {ing} x{mult} (+{cost} руб.)")
    print(f"Текущая цена: {total_price} руб.")

print("=" * 35)
print("ВАШ ЗАКАЗ:")
print(f"  База: {base_price} руб.")
for ing, qty in pizza.items():
    if qty == 1:
        label = ""
    elif qty == 2:
        label = " (дабл)"
    else:
        label = " (трипл)"
    print(f"  {ing}{label} - {INGREDIENTS[ing] * qty} руб.")
print(f"ИТОГО: {total_price} руб.")
print("=" * 35)
