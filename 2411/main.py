import random

pers = [["Не Магомед", 3], ["Вася", 1],
        ["Бочарников Александр", 3], ["Сергей Шарант", 3]]

while len(pers) > 1:
    p1, p2 = random.sample(pers, 2)
    extra1 = random.randint(1, 3)
    extra2 = random.randint(1, 3)
    if p1[1] + extra1 > p2[1] + extra2:
        pers.remove(p2)
        print(p1[0], "победил", p2[0])
    else:
        pers.remove(p1)
        print(p1[0], "победил", p2[0])

print(pers[0][0], "победил")

