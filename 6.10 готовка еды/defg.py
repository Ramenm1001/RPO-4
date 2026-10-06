meal = "шаурма"
price = 100

while True:
    print(meal, "стоимость:", price)
    print("3-добавить сыр")
    print("2-добавить помидоры")
    print("1-добавить соус")
    print("0-выход")
    act = input()

    if act == "1":
        price += 30
        meal += " больше соуса"
    elif act == "2":
        price += 40
        meal += "больше помидоров"
    elif act == "3":
        price += 50
        meal += "больше сыра"
    if act == "0":
        break

    
