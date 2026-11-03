import random
print("")
name = "Папич"
food = 100
dirt = 0
water = 100
money = 500
food_menu = { "1": "нейтрализующий салатик", "2": "майонез", "3": "морковка", "4": "палочки кузя", "5": "картофель фри( НЕ ИЗ макдональдс"}
#выбирает папич
while True:
    act = random.randint(1 , 10)
    if act == 1:
        food -= random.randint( 10, 30)
        if food < 0:
            food = 0
    elif act == 10:
        dirt =+ 50
        print(name, "упал в майонезную лужу")
    
    if dirt > 100:
        dirt = 100
    #меню действий
    print(f"{name}")
    print("")
    print(f"голод: {food}")
    print(f"загрязнение: {dirt}")
    print(f"жажда: {water}")
    print("")
    print("feed - кормить")
    print("wash - мыть папича")
    print("drink - дать напиток")
    print("")
    print("donate - дать папичу деньги")
    print("WORK - выйти на подработку")
    act = ""
    while act not in [ "feed", "wash", "drink", "donate", "work"]:
        act = input("=")
    if act == "feed":
        print("выберите еду")
        print("1 - нейтраклизующий салатик")
        print("2 - майонез")
        print("3 - морковка")
        print("4 - палочки кузя")
        print("5 - картофель фри правильного приготовления")
        food_choice = ""
        while food_choice not in [ "1", "2", "3", "4", "5"]:
            food_choice = input("=")
        if food_choice == "2":
            print(f"папич съел майонез и умер")
            print(f"игра окончена")
            break
        rnd = random.randint(1, 100)
        if 1 <= rnd <= 40:
            food = min( food + 60, 100)
            print(f"{name} поел")
        elif 40 < rnd <= 80:
            food = min(food + 60, 100)
            print(f"{name} поел но немного запачкался")
            dirt = min(dirt + random.randint(1, 40), 100)
        else:
            print(f"{name} вылил майонез на голову")
            dirt = min( dirt + random.randint(50, 80), 100)
    if act == "wash":
        dirt = 0
        print(f"{name} помыт")
    if act == "drink":
        print("меню напитков:")
        print("")
        print("1 - майонез")
        print("2 - апельсиновый сок")
        print("3 - жиычик")
        drink_choice = ""
        while drink_choice not in [ "1", "2", "3"]:
            drink_choice = input("=")
        if drink_choice == "1":
            water = min(water + 40, 100)
            dirt = min(dirt + 100, 100)
            print(f"{name} захлебнулся майонезом и умер")
            break
        elif drink_choice == "2":
            water = min(water + 60, 100)
        elif drink_choice == "3":
            water = min(water + 60, 100)
    if act == "donate":
        print("выберите сумму доната:")
        print("")
        print("1 - 100 рублей")
        print("2 -  300 рублей( быть принцем не так уж и легко)")
        print(" 3 - 500рублей")
        print(" 4 - 5000 рублей")
        don_choice = ""
        while don_choice not in [ "1", "2", "3", "4"]:
            don_choice = input("=")
        if don_choice == "1":
            if money >= 100:
                money -= 100
                print("вы задонатили 100 рублей, этого слишком мало. Папич умирает от недостатка")
                break
            else:
                print("у вас недостаточно денег. папич умер")
                break
        elif don_choice == "2":
            if money >= 300:
                money -= 300
                print("вы задонатили 300 рублей, папич купил себе морковь и подавился")
                break
            else:
                print(" вы ничего не донатили, папичу не хватает денег на помыться")
                dirt = min(dirt + 60, 100)
        elif don_choice == "3":
            if money >= 500:
                    money -= 500
                    dirt = 0
                    food =+ 50
            else:
                    print("у вас недостаточно денег, папич умер от злости и голода")
        elif don_choice == "4":
            if money >= 5000:
                money -= 5000
                dirt = 0
                print("папичу хватит морковки до конца жизни. он завершил стримерскую карьеру")
                break
            else:
                print("вам не хватило денег")
    if act == "work":
        print(" вы ушли на подработку чтобы заработать денег... Папич один дома")
        print("1 - подработка 3 часа. 250 рублей")
        print("2 - подработка на 5 часов. 800 рублей")
        print("3 - подработка на 12 часов. 1750")
        work_choice = ""
        while work_choice not in [ "1", "2", "3"]:
            work_choice = input("=")
        if work_choice == "1":
            money += 250
            water= max( 0, water - 15)
            food= max ( 0, food - 20)
            dirt = min( 100, dirt + 25)
            print( "пока вы отсуствовали {name} был один.")
            print( "жажда", water)
            print( "голод", food)
            print( "загрязнение", dirt)
            print( "вы заработали 250 рублей", money)
        if work_choice == "2":
            money += 800
            water= max( 0, water - 45)
            food= max ( 0, food - 50)
            dirt = min( 100, dirt + 50)
            print( "пока вы отсуствовали {name} был один.")
            print( "жажда",  water)
            print( "голод",  food)
            print( "загрязнение",  dirt)
            print( "вы заработали 800 рублей", money)
        if work_choice == "3":
            money += 1750
            water= max( 0, water - 70)
            food= max ( 0, food - 75)
            dirt = min( 100, dirt + 70)
            print( "пока вы отсуствовали {name} был один. он сошел с ума и умер")
            print( "жажда", water)
            print( "голод", food)
            print( "загрязнение", dirt)
            print( "вы заработали 1750 рублей", money)
            break
if water <= 0 or food <= 0 or dirty >= 100:
    print("папич умиер")
    print("")
    print("игра окончена")
        
        
                
                
            
        
