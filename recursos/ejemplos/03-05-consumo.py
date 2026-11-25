lectura_inicial = 120
lectura_final = 148
TARIFA_CENTIMOS = 75
consumo = lectura_final - lectura_inicial
importe = consumo * TARIFA_CENTIMOS
print(f"Consumo: {consumo} kWh")
print(f"Importe: S/ {importe / 100:.2f}")
