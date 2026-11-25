def entero_no_negativo(valor, campo):
    if type(valor) is not int or valor < 0:
        raise ValueError(f"{campo}: entero no negativo requerido")
    return valor


def evaluar_compra(presupuesto, materiales):
    """Devuelve (total, saldo, viable) para los importes en céntimos."""
    entero_no_negativo(presupuesto, "Presupuesto")
    total = 0
    for nombre, cantidad, precio in materiales:
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("Nombre de material inválido")
        if type(cantidad) is not int or cantidad <= 0:
            raise ValueError("Cantidad: entero positivo requerido")
        entero_no_negativo(precio, "Precio")
        total += cantidad * precio
    saldo = presupuesto - total
    return total, saldo, saldo >= 0


def soles(centimos):
    signo = "-" if centimos < 0 else ""
    entero, fraccion = divmod(abs(centimos), 100)
    return f"{signo}S/ {entero}.{fraccion:02d}"


def mostrar_informe(resultado):
    total, saldo, viable = resultado
    print("Total:", soles(total))
    print("Saldo:", soles(saldo))
    print("Compra viable" if viable else "Presupuesto insuficiente")


def main():
    materiales = [("Cuadernos", 5, 450),
                  ("Lápices", 10, 120),
                  ("Cartulinas", 4, 300)]
    try:
        mostrar_informe(evaluar_compra(10000, materiales))
    except ValueError as error:
        print("Datos inválidos:", error)


if __name__ == "__main__":
    main()
