def calcular_subtotal(cantidad, precio_centimos):
    """Devuelve el importe en céntimos de una línea válida."""
    return cantidad * precio_centimos

importe_cuadernos = calcular_subtotal(5, 450)
importe_lapices = calcular_subtotal(10, 120)
