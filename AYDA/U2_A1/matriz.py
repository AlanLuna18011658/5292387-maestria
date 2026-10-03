# Nombre: Alan Alejandro Luna González
# ID: 5292387
# Entregable: U2 A1 - Programación de algoritmo de divide y vencerás que calcule los números de Fibonacci en tiempo logarítmico. 
# Asignatura: Análisis y Diseño de Algoritmos

# función que realiza la multiplicación de dos matrices 2 por 2
def matriz(a1, b1, c1, d1, a2, b2, c2, d2):
    
    a = a1 * a2 + b1 * c2
    b = a1 * b2 + b1 * d2
    c = c1 * a2 + d1 * c2
    d = c1 * b2 + d1 * d2
    
    return a, b, c, d

# función que calcula el n-esimo número de Fibonacci
# se multiplica n veces seguidas
def fibonacci(n):
    a, b, c, d = 1, 0, 0, 1 # matriz identidad
    
    for i in range(n):
        a, b, c, d = matriz(a, b, c, d, 0, 1, 1, 1) # matriz base
        
    return b # el valor de b es el n-esimo número de Fibonacci

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
