def mayor_menor():
    n1 = float(input("num 1: "))
    n2 = float(input("num 2: "))
    n3 = float(input("num 3: "))

    if n1>=n2 and n1>=n3:
        maxi = n1
    elif n2>=n1 and n2>=n3:
        maxi = n2
    else:
        maxi = n3

    if n1<=n2 and n1<=n3:
        mini = n1
    elif n2<=n1 and n2<=n3:
        mini = n2
    else:
        mini = n3

    print("el mayor es", maxi)
    print("el menor es", mini)

mayor_menor()
