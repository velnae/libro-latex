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

def evaluar_compra(presupuesto, total):
    if type(presupuesto) is not int or presupuesto < 0:
        raise ValueError("Presupuesto inválido")
    diferencia = presupuesto - total
    if diferencia >= 0:
        return "Compra viable", diferencia
    return "Presupuesto insuficiente", diferencia

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
        total = calcular_total(materiales)
        estado, diferencia = evaluar_compra(presupuesto, total)
        for nombre, cantidad, precio in materiales:
            print(nombre, soles(cantidad * precio))
        print("Total:", soles(total))
        print(estado)
        etiqueta = "Saldo:" if diferencia >= 0 else "Exceso:"
        print(etiqueta, soles(abs(diferencia)))
    except ValueError as error:
        print("Error:", error)

if __name__ == "__main__":
    main()
