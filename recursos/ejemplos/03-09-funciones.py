def subtotal(cantidad, precio_centimos):
    return cantidad * precio_centimos

def mostrar_importe(centimos):
    print(f"Importe: S/ {centimos / 100:.2f}")

total = subtotal(4, 350)
mostrar_importe(total)


assert subtotal(4, 350) == 1400
assert subtotal(0, 350) == 0
