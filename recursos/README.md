# Recursos de programación

Los mismos archivos que aparecen en el PDF se pueden abrir y ejecutar con Python 3. Los ejemplos de este libro usan la biblioteca estándar.

## Ejemplos

Desde la carpeta que contiene `main.tex`, ejecuta un ejemplo indicando su archivo.

```bash
python3 recursos/ejemplos/03-01-area.py
python3 recursos/ejemplos/03-04-conversion-minutos.py
python3 recursos/ejemplos/03-caso-integrado.py
```

Para la conversión de minutos, ingresa `135`. La salida esperada es `2 h y 15 min`.

| Archivos | Qué muestran |
| --- | --- |
| `ejemplos/03-01-area.py` a `ejemplos/03-11-diccionario.py` | Los once ejemplos numerados del capítulo 3 |
| `ejemplos/03-caso-etapas.py` | Las tres primeras etapas del caso de presupuesto, en el orden de ejecución |
| `ejemplos/03-caso-integrado.py` | La versión completa del caso del capítulo 3 |
| `ejemplos/04-*.py` | Aserciones, validación, seguimiento, depuración, calidad y búsqueda del capítulo 4 |
| `pseudocodigo/` | Algoritmos de los capítulos 2 y 4 |
| `salidas/` | Resultados esperados de los programas completos de presupuesto |

## Proyecto integrador

Ejecuta estos comandos desde la raíz del proyecto.

```bash
cd recursos/proyecto
python3 presupuesto.py
python3 -m unittest -v
```

Con los materiales de ejemplo, el costo total es S/ 46,50 y el saldo es S/ 53,50. El programa escribe los importes con punto decimal. Las pruebas cubren el caso habitual, el presupuesto exacto e insuficiente, una lista vacía, entradas inválidas, un precio de cero y el formato monetario.

Tanto el ejemplo del capítulo 3 como el proyecto del capítulo 4 aceptan el presupuesto en céntimos y un iterable de ternas con nombre, cantidad y precio unitario en céntimos. `evaluar_compra(presupuesto, materiales)` devuelve `(total, saldo, viable)`, por ejemplo `(4650, 5350, True)`.

Para practicar con un caso adicional, adapta el proyecto a un registro de préstamos o a un inventario. En el cierre de cada capítulo se encuentran los ejercicios y las indicaciones para evaluar los resultados.
