notas = [13, 16, 11]
notas.append(12)
if notas:
    promedio = sum(notas) / len(notas)
    print(f"Promedio: {promedio:.2f}")
    print("Primera nota:", notas[0])
