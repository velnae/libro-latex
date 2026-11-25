stock = 4
if stock < 0:
    estado = "Dato inválido"
elif stock == 0:
    estado = "Agotado"
elif stock <= 5:
    estado = "Stock bajo"
else:
    estado = "Stock normal"
print(estado)
