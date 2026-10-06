meal = "Пельмени"
price = 100
while True:
    print (meal, "стоимость:", price)
    print ("1-добавить сметану")
    print ("2-добавить майонез")
    print ("3-добавить сыр")
    print ("4-добавить мясо со свининой")
    print ("5-добавить мясо с говядиной")
    print ("6-добавить мясо с курицой")
    print ("7-добавить тесто")
    print ("8-добавить масло")
    print ("9-добавить сливки")
    print ("10-добавить Олега-бомжа")
    print ("11-добавить крысу")
    print ("12-добавить рыбу-фугу")
    print ("0-выход")
    act = input ()
    if act == "1":
        price += 50
        meal += " со сметаной"
    elif act == "2":
        price += 50
        meal += " с майонезом"
    elif act == "3":
        price += 50
        meal += " с сыром"
    elif act == "4":
        price += 50
        meal += " со свининой"
    elif act == "5":
        price += 50
        meal += " с говядиной"
    elif act == "6":
        price += 50
        meal += " с курицой"
    elif act == "7":
        price += 50
        meal += " с тестом"
    elif act == "8":
        price += 50
        meal += " с маслом"
    elif act == "9":
        price += 50
        meal += " со сливками"
    elif act == "10":
        price += 1
        meal += " с Олегом-бомжом"
    elif act == "11":
        price += 1500
        meal += " с крысой"
    elif act == "12":
        price += 78523458739823934854865347894859468648994857856
        meal += " с рыбой-фугу"
    else:
        act == "0"
        break
    
    
