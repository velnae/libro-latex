inventario = {"A01": 8, "A02": 3}
inventario["A01"] += 2
inventario["A03"] = 5
for codigo, cantidad in inventario.items():
    print(codigo, cantidad)
print(inventario.get("A04", 0))
