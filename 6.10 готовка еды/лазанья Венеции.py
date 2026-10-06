"""
x = 0
while True:
    print(f"Число [x]")
    print("1-прибавить число")
    act = input()
    if act == "1":
     plus = int(input("Сколько прибавить? "))
     x += plus
"""         

meal = "Лазанья"
price = 0
while True:
    print(meal, "стоимость:", price)
    print("1-добавить слой")
    print("2-добавить сыр")
    print("3-добавить фарш")
    print("4-добавить томаты")
    print("5-добавить соус болоньезе")
    print("6-добавить лук и морковь с чесноком") 
    print("6-добавить масло оливковое и растительное и сливочное") 
    print("7-добавить соль, перец, травы, еще сыра") 
    print("0-выход")
    act = input()
    if act == "1":
      price += 100
      meal += " лист Италии"
    if act == "2":
      price += 1500
      meal += " c сыром"
    if act == "3":
      price += 900
      meal += " c мяском"
    if act == "4":
      price += 200
      meal += " c черри"
    if act == "5":
      price += 1100
      meal += " c соусом"
    if act == "6":
      price += 540
      meal += " c овощами"
    if act == "7":
      price += 190
      meal += " cо вкусом Италии"
    if act == "0":
       break
    
      
    
    
