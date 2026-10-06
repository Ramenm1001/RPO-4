'''x = 0

while True:
   print(f'xисло {x}')
   print('1 - прибавить число')
   print('0 — выйти')

   act = input()

   if act == '1':
       plus = int(input('Сколько прибавить? '))
       x += plus
   elif act == '0':
    break'''
meal = 'Пицца'
price = 100
while True:
    print(meal, 'стоимость:', price)

    print('1 - dobavit sir')
    print('2 - dobavit gribi')
    print('3 - dobavit sous')
    print('4 - dobavit cgeotyre')
    print('0 - vihod')
    act = input()

    if act == '1':
        price += 50
        meal += " s sirom"
    if act == '2':
        price += 50
        meal += ' s gribami'
    if act == '3':
        price += 30
        meal += ' s sousom'
    if act == '4':
        price += 10000
        meal += ' s cgeotyrjq'
    if act == '0':
        break
