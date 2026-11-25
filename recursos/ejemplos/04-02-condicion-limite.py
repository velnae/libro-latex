# Versión defectuosa:
def compra_viable(total, presupuesto):
    return total < presupuesto

# La primera versión rechaza una compra exacta.
assert not compra_viable(1000, 1000)


# Corrección: la igualdad también es válida.
def compra_viable(total, presupuesto):
    return total <= presupuesto

assert compra_viable(1000, 1000)
assert not compra_viable(1001, 1000)
