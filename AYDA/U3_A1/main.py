# Nombre: Alan Alejandro Luna González
# ID: 5292387
# Entregable: U3 A1 - Implementación de algoritmo de búsqueda a profundidad
# Asignatura: Análisis y Diseño de Algoritmos


# aristas del grafo no conexo
aristas = [(0, 29),
           (0, 46),
           (0, 21),
           (0, 14),
           (0, 38),
           (0, 31),
           (1, 41),
           (1, 31),
           (1, 21),
           (1, 17),
           (2, 9),
           (2, 26),
           (2, 5),
           (2, 25),
           (2, 4),
           (3, 18),
           (3, 30),
           (3, 47),
           (4, 28),
           (4, 9),
           (4, 8),
           (5, 44),
           (5, 12),
           (6, 37),
           (6, 10),
           (7, 23),
           (7, 22),
           (7, 39),
           (9, 19),
           (9, 28),
           (9, 27),
           (11, 33),
           (13, 25),
           (13, 38),
           (13, 29),
           (14, 26),
           (14, 28),
           (14, 39),
           (15, 22),
           (15, 31),
           (15, 19),
           (15, 41),
           (16, 46),
           (16, 26),
           (16, 38),
           (16, 27),
           (17, 40),
           (17, 29),
           (18, 45),
           (18, 42),
           (18, 35),
           (18, 33),
           (18, 47),
           (20, 36),
           (20, 49),
           (20, 42),
           (22, 26),
           (22, 34),
           (23, 31),
           (23, 32),
           (23, 40),
           (24, 31),
           (24, 44),
           (25, 38),
           (26, 31),
           (27, 32),
           (29, 48),
           (29, 41),
           (30, 47),
           (30, 37),
           (33, 36),
           (33, 49),
           (34, 48),
           (35, 45),
           (36, 45),
           (37, 49),
           (37, 45),
           (37, 47),
           (38, 41),
           (40, 48),
           (41, 44),
           (42, 49),
           (43, 48),
           (45, 47)]

# lista vacía para cada uno de los 50 nodos
grafo = {nodo: [] for nodo in range(50)}

# registro de conexiones en ambas direcciones, es un grafo no dirigido
for a, b in aristas:
    grafo[a].append(b)
    grafo[b].append(a)


# función para buscar en profundidad (DFS)
def dfs(grafo, nodo_padre, grupo):
    grupo.append(nodo_padre)

    # revisión de todos sus vecinos
    for nodo_hijo in grafo[nodo_padre]:

        # vecinos no visitados
        if nodo_hijo not in grupo:
            dfs(grafo, nodo_hijo, grupo)


# se guardan los nodos agrupados para no repetirlos
visitados = []

# busqueda de grupos en el grafo
for nodo in grafo:

    # si el nodo está libre y no ha sido agrupado
    if nodo not in visitados:
        grupo = []

        # busqueda de todos los nodos conectados
        dfs(grafo, nodo, grupo)

        # lista de nodos procesados
        visitados += grupo

        print(sorted(grupo), "Total:", len(grupo))