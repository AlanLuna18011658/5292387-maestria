# Alumno: Alan Alejandro Luna González
# ID: 5292387
# Entregable: U6 A1 - Implementar un algoritmo de retroceso para resolver sudokus.
# Asignatura: Análisis y Diseño de Algoritmos.


# se valida si un múmero puede colocarse en la posición: fila, columna
def validacion(tablero, fila, columna, numero):
  inicio_fila = fila - fila % 3
  inicio_columna = columna - columna % 3

  return all(tablero[fila][i] != numero and tablero[i][columna] != numero
             and tablero[inicio_fila + i // 3][inicio_columna + i % 3] != numero for i in range(9))

# resolución mediante la técnica de backtracking
def sudoku(tablero):
  for fila in range(9):
    for columna in range(9):
      if tablero[fila][columna] == 0:
        for numero in range(1, 10):
          if validacion(tablero, fila, columna, numero):
            tablero[fila][columna] = numero
            if sudoku(tablero):
              return True
            tablero[fila][columna] = 0
        return False
  return True

sudoku_1 = [
    [5, 0, 0, 9, 1, 3, 7, 2, 0],
    [3, 0, 0, 0, 8, 0, 5, 0, 9],
    [0, 9, 0, 2, 5, 0, 0, 8, 0],
    [6, 8, 0, 4, 7, 0, 2, 3, 0],
    [0, 0, 9, 5, 0, 0, 4, 6, 0],
    [7, 0, 4, 0, 0, 0, 0, 0, 5],
    [0, 2, 0, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 8, 9, 1, 6, 0, 0],
    [8, 5, 0, 7, 2, 0, 0, 0, 3]
]

sudoku_2 = [
    [6, 9, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 0, 0, 9, 6, 0, 0, 0],
    [0, 8, 0, 7, 5, 3, 0, 9, 0],
    [0, 2, 0, 3, 7, 4, 5, 6, 1],
    [3, 6, 0, 0, 0, 5, 0, 2, 0],
    [0, 0, 0, 9, 6, 0, 3, 7, 8],
    [0, 0, 6, 0, 3, 1, 0, 8, 4],
    [0, 4, 5, 8, 0, 7, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 5, 7]
]

for tablero in (sudoku_1, sudoku_2):
  sudoku(tablero)
  for fila in tablero:
    print(*fila)
  print()