def entrada():
    edad = int(input("dame tu edad: "))

    if edad < 0:
        print("error de edad")
    elif edad < 12:
        print("el costo es $50")
    elif edad <= 17:
        print("el costo es $80")
    else:
        print("el costo es $120")

entrada()
