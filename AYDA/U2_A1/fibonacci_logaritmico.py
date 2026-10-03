
# unificación de algoritmo para lograr calcular el n-esimo número de Fibonacci en tiempo logarítmico.
# se combina matriz.py y divide_venceras.py

from matriz import matriz

# función que calcula la matriz base de fibonacci elevada a la n
def fibonacci_logaritmico(n):

    if n == 1:
        return 0, 1, 1, 1 # matriz base

    a, b, c, d = fibonacci_logaritmico(n // 2) # se corta el exponente a la mitad
    a, b, c, d = matriz(a, b, c, d, a, b, c, d) # se eleva la matriz al cuadrado

    if n % 2 == 0:
        return a, b, c, d # si n es par
    return matriz(a, b, c, d, 0, 1, 1, 1) # si n es impar

if __name__ == "__main__":
    print(fibonacci_logaritmico(2))
