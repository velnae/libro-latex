presupuesto = 10000
cantidad = 5
precio = 450
subtotal = cantidad * precio
print(subtotal)  # 2250

if subtotal <= presupuesto:
    print("Compra viable")
else:
    print("Presupuesto insuficiente")

materiales = [("Cuadernos", 5, 450),
              ("Lápices", 10, 120),
              ("Cartulinas", 4, 300)]
total = 0
for nombre, cantidad, precio in materiales:
    total += cantidad * precio
print(total)  # 4650
