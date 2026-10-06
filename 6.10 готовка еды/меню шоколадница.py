print ("Добро пожаловать в ресторан шоколадницу закажите завтрак")
meal = ""
price = 0
while True:
    print (meal,"Стоимость:", price)
    print ("1-Английский завтрак")
    print ("0-Завершить заказ")
    act = input ()
    if act == "1":
        price += 270
        meal +=" Англиский завтрак"
        while True:
            print ("Добавки")
            print ("1.1-Добавить глазунью")
            print ("1.2-Добавить тост")
            print ("1.0-отказаться")
            act = input ()
            if act == "1.1":
                price += 45
            meal +=" с глазуньем"
            if act == "1.2":
                price += 30
            meal +=" с дополнительным тостом"
            if act == "1.0":
                break
            
    if act == "0":
        break
    
