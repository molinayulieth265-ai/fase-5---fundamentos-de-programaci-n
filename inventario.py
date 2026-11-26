inventario = [
    ["A001", "Arroz", 10, 20],
    ["A002", "Aceite", 15, 10],
    ["A003", "Azucar", 5, 15],
    ["A004", "Cafe", 8, 12],
    ["A005", "Leche", 25, 20]
]

def calcular_reabastecimiento(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

print("REPORTE DE REABASTECIMIENTO")
print("--------------------------------")

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_reabastecimiento(stock_actual, stock_minimo)

    print("Articulo:", nombre)
    print("Cantidad a solicitar:", cantidad_pedir)
    print("--------------------------------")
