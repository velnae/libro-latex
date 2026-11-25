def subtotal(cantidad, precio_centimos):
    return cantidad * precio_centimos

assert subtotal(4, 350) == 1400
assert subtotal(0, 350) == 0
assert subtotal(1, 0) == 0
