def nota_valida(nota):
    return type(nota) is int and 0 <= nota <= 20

for valor in (14, 0, 20, -1, 21, "catorce", 12.5, True):
    print(repr(valor), nota_valida(valor))
