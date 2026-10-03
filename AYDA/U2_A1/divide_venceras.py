
# funcion que calcula x elevado a la n para utilizar el metodo de divide y vnecerás
# se corta el exponente a la mitad

def divide_venceras(x, n):

    if n == 0:

        return 1 # n numero elevado a la 0 es 1

    if n % 2 == 0:

        return divide_venceras(x * x, n // 2) # si n es par

    else:

        return x * divide_venceras(x * x, n // 2) # si n es impar

print(divide_venceras(2, 0))
print(divide_venceras(2, 1))
print(divide_venceras(2, 2))
print(divide_venceras(2, 3))
