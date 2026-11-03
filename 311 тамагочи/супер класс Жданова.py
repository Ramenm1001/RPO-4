import random
name = 'Диор Армани'
food = 100
dirt = 0
while True:
  
    menu = {'1': 'домошнятинка', '2': 'сырный суп', '3': 'Говядина в майонезе'}


    print(f'{name}')
    print(f'голод: {food}')
    print(f'грязь: {dirt}')
    print('feed - кормить')
    print('wash - мыца')
    act = ""
    while act not in [ 'feed', 'wash' ]:
        act = input('Выбранное действие - ')
    if act == 'feed':
        print('Меню: ')
        print('1 - Домошнятинка')
        print('2 - сырный суп')
        print('3 - Говядина в майонезе')
        fod = 0
        while fod not in [ 1, 2, 3]:
           fod = int(input('Выбранная еда - '))
           
        act = random.randint(1, 3)
        if act == 1:
            food -= random.randint(10, 30)
            if food < 0:
                food = 0
        elif act == 2:
               dirt =+ 50
               food -= random.randint(15, 35)
               if food < 0:
                   food = 0
               print(f'{name} съездил в Бобруйск')
               if dirt > 100:
                    dirt = 100
        rnd = random.randint(1, 100)
        if 1 <= rnd <= 40:
            food = min(food + 60, 100)
            print(f'{name} поел')
        elif 40 < rnd <= 80:
            food = min(food + 60, 100)
            dirt = min(dirt + random.randint(1, 40), 100)
            print(f'{name} поел как свинья')
        else:
            print(f'{name} съездил в Бобруйск')
            dirt = min(dirt + random.randint(50, 80), 100)

    elif act == 'wash':
        dirt = 0
        print(f'{name}, не воняет')
    if food <= 0:
        print(f'{name} был слишком голоден, украл из Дикси еды и его посадили. Он умер в тюрьме')
        break
    if dirt >= 100:
        print(f'{name} стал слишком вонять, от него ушел Мафаня и он умер от грусти')
        break
        

