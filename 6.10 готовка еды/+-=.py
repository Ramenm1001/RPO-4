x = 0
YES = {"да", "д", "yes", "y", "1"}
NO = {"нет", "н", "no", "n", "2"}
x = int(input("x: "))
print (x)
print ("1-прибавить число\b 2-уменьшить число")
while True:
    act = input().strip().lower()
    if act in YES:
        b = int(input("сколько прибавить?" ))
        x += b
        print(x)
        br = input("закончить: ").strip().lower()
        if br in YES:
            break
        else:
            print(f"ok x={x}")
    elif act in NO:
        c = int(input("сколько убавить?" ))
        x -= c
        print(x)
        br = input("закончить: ").strip().lower()
        if br in YES:
            break
        else:
            print(f"ok x={x}")


