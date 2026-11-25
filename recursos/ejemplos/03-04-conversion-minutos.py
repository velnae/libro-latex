try:
    minutos = int(input("Minutos enteros: "))
    if minutos < 0:
        print("Ingrese un valor no negativo.")
    else:
        horas = minutos // 60
        resto = minutos % 60
        print(f"{horas} h y {resto} min")
except ValueError:
    print("La entrada debe ser un entero.")
