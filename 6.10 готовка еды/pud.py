meal = "лазанья"
price = 100
while True:
    print(meal, "стоимость", price)
    print("1- добавить сыр")
    print("2- добавить фарш")
    print("3- добавить тесто")
    print("4- добавить соус")
    print("5- штото")
    print("0- выход")

    act = input("ваш выбор")

    if act == "1":
        price += 30
        meal += " с сыром"

    if act == "2":
        price += 80
        meal += " с фаршем"
    
    if act == "3":
        price += 60
        meal += " с тестом"

    if act == "4":
        price += 20
        meal += " с соусом"

    if act == "5":
        price += 100
        meal += " с"

    if act == "0":
        print("итоговая цена", price)
        break

    
        

