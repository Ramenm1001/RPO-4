sp = [11, 22, True, "qwerty"]
#      0   1   2   3
# sp = list()
print(sp)
sp.append(123) # добавление в конец
print(sp)
sp.remove(22) # удаление по значению
print(sp)
x = sp.pop() # удаление по индексу
print(sp, x)
sp[0] += 10 # обращение к элементу
print(sp)
