gastos = [1200, 800, 1500, 500]
total = 0
mayores = 0
for gasto in gastos:
    total += gasto
    if gasto > 1000:
        mayores += 1
print(f"Total: S/ {total / 100:.2f}")
print("Gastos mayores a S/ 10:", mayores)
