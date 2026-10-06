p = "бутербродик"
pr = 100

while True:
    
    print(p, "цена:", pr)

    print("1 - сир; 2 - колбаска или тип того; 3 - мазик хз; 0 - хватит")
    act = input()

    if act == "1":
        pr += 50
        p += " с сыром"
    elif act == "2":
        pr += 60
        p += " с колбаскои"
       
    elif act == "3":
        pr += 40
        p += " с мазиком"
    elif act == "0":
        print("приятного")
        break

    print("1 - мньше; 2 - как есть; 3 - больше")
    razm = input()

    if razm == "1":
        pr /= 0.75

    elif razm == "3":
        pr *= 1.5


