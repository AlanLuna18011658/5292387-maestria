# Alumno: Alan Alejandro Luna González
# ID: 5292387
# U6 A1 - Algoritmo usando la técnica de Ramificación y Poda que resuelva el problema de la mochila.
# Asignatura: Análisis y Diseño de Algoritmos.


valores = [79, 32, 47, 18, 26, 85, 33, 40, 45, 59]
pesos = [85, 26, 48, 21, 22, 95, 43, 45, 55, 52]
capacidad_maxima = 101
mejor_valor, mejor_solucion = 0, []

# ordena los objetos, los de mayor valor por cada unidad de peso
orden_objetos = sorted(range(len(valores)), key=lambda i: valores[i] / pesos[i], reverse=True)

# función que prueba las combinaciones, descartando las no funcionales
def ramificacion_poda(posicion_actual, peso_acumulado, valor_acumulado, objetos_seleccionados):
  global mejor_valor, mejor_solucion

  # si es la mejor combinación, se guarda
  if valor_acumulado > mejor_valor:
    mejor_valor = valor_acumulado
    mejor_solucion = objetos_seleccionados

  # si se revisan todos los objetos
  if posicion_actual == len(orden_objetos):
    return

  # poda, se suman el valor de todos los objetos que faltan
  valor_maximo_restante = sum(valores[i] for i in orden_objetos[posicion_actual:])
  # si aun sumando todo lo restante no superamos el mejor valor ya encontrado, se detiene
  if valor_acumulado + valor_maximo_restante <= mejor_valor:
    return

  indice_objeto = orden_objetos[posicion_actual] # decisión

  # camino 1, toma el objeto solamente si cabe en la mcohila
  if peso_acumulado + pesos[indice_objeto] <= capacidad_maxima:
    ramificacion_poda(
      posicion_actual + 1,
      peso_acumulado + pesos[indice_objeto],
      valor_acumulado + valores[indice_objeto],
      objetos_seleccionados + [indice_objeto + 1]
    )

  # camino 2, no toma el objeto
  ramificacion_poda(
    posicion_actual + 1,
    peso_acumulado,
    valor_acumulado,
    objetos_seleccionados
  )

ramificacion_poda(0, 0, 0, [])
print(mejor_valor)
print(sorted(mejor_solucion))