def calcular_total(materiales):
    total = 0
    for nombre, cantidad, precio in materiales:
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("Nombre inválido")
        if type(cantidad) is not int or cantidad <= 0:
            raise ValueError("Cantidad inválida")
        if type(precio) is not int or precio < 0:
            raise ValueError("Precio inválido")
        total += cantidad * precio
    return total

def evaluar_compra(presupuesto, materiales):
    if type(presupuesto) is not int or presupuesto < 0:
        raise ValueError("Presupuesto inválido")
    total = calcular_total(materiales)
    saldo = presupuesto - total
    return total, saldo, saldo >= 0


def soles(centimos):
    signo = "-" if centimos < 0 else ""
    entero, fraccion = divmod(abs(centimos), 100)
    return f"{signo}S/ {entero}.{fraccion:02d}"


def main():
    presupuesto = 10000
    materiales = [("Cuadernos", 5, 450),
                  ("Lápices", 10, 120),
                  ("Cartulinas", 4, 300)]
    try:
        total, saldo, viable = evaluar_compra(presupuesto, materiales)
        for nombre, cantidad, precio in materiales:
            print(nombre, soles(cantidad * precio))
        print("Total:", soles(total))
        print("Compra viable" if viable else "Presupuesto insuficiente")
        print("Saldo:", soles(saldo))
    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
