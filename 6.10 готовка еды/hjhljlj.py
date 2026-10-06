meal = "пицца"
price = 100

while True:
    print(meal, "стоимость:", price)

    print("1-доюавить сыр")
    print("2-добавиь доп мясо")
    print("3-довать острый соус")
    print("4-заново")
    print("0-выход")
    act = input()

    if act == "1":
        price += 50
        meal += "с сыром"
    if act == "2":
        price += 100
        meal += "с мяском"
    if act == "3":
        price += 75
        meal += "с остротой"
    if act == "0":
        break
    if act == "4":
        meal = "пицца"  
        price = 100      
        continue
