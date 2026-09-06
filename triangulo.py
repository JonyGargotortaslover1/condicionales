def triangulo():
    a=float(input("lado 1: "))
    b=float(input("lado 2: "))
    c=float(input("lado 3: "))

    if a+b<=c or a+c<=b or b+c<=a:
        print("no forma triangulo")
    elif a==b and b==c:
        print("equilatero")
    elif a==b or a==c or b==c:
        print("isosceles")
    else:
        print("escaleno")

triangulo()
