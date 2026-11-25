def contiene(lista, buscado):
    for elemento in lista:
        if elemento == buscado:
            return True
    return False

# Peor caso: recorre n elementos.
assert contiene([4, 7, 9], 9)
assert not contiene([4, 7, 9], 2)
