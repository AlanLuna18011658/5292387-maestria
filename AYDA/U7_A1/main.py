# Alumno: Alan Alejandro Luna González
# ID: 5292387
# Entregable: U7 A1 - Problema de la mochila, corte de cuerda y programación dinámica
# Asignatura: Análisis y Diseño de Algoritmos

# mochila

valor = [79, 32, 47, 18, 26, 85, 33, 40, 45, 59]
peso = [85, 26, 48, 21, 22, 95, 43, 45, 55, 52]
mejor_valor = [0] * 141 # mejor valor para cada capacidad (0 a 140)
mejor_objeto = [[] for capacidad in range(141)]

for indice, (peso_objeto, valor_objeto) in enumerate(zip(peso, valor), 1):
    for capacidad in range(140, peso_objeto - 1, -1):
        if mejor_valor[capacidad - peso_objeto] + valor_objeto > mejor_valor[capacidad]:
            mejor_valor[capacidad] = mejor_valor[capacidad - peso_objeto] + valor_objeto
            mejor_objeto[capacidad] = mejor_objeto[capacidad - peso_objeto] + [indice]

print("mochila:", mejor_valor[140], mejor_objeto[140])

# corte de cuerda

precio = [1, 4, 10, 12, 15, 20, 21, 32, 31, 41, 51]
mejor_precio = [0] * 12
mejor_corte = [[] for largo in range(12)]

for largo in range(1, 12):
    for pieza in range(1, largo + 1):
        if precio[pieza - 1] + mejor_precio[largo - pieza] > mejor_precio[largo]:
            mejor_precio[largo] = precio[pieza - 1] + mejor_precio[largo - pieza]
            mejor_corte[largo] = [pieza] + mejor_corte[largo - pieza]

print("cuerda:", mejor_precio[11], mejor_corte[11])

# parentización de matrices

dimension = [5, 10, 3, 12, 5, 50, 6]
numero_matrices = len(dimension) - 1
costo = {(matriz, matriz): 0 for matriz in range(numero_matrices)}

for matrices_en_cadena in range(2, numero_matrices + 1):
    for inicio in range(numero_matrices - matrices_en_cadena + 1):
        fin = inicio + matrices_en_cadena - 1
        costo[inicio, fin] = min(
            costo[inicio, corte] + costo[corte + 1, fin] + dimension[inicio] * dimension[corte + 1] * dimension[fin + 1]
            for corte in range(inicio, fin)
        )

print("matrices:", costo[0, numero_matrices - 1])