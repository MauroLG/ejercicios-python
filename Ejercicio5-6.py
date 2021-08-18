# Ejercicio 5.6a

def es_potencia_de_dos(n):
    i = 0
    while 2 ** i <= n:
        if 2 ** i == n:
            return True
        i += 1
    return False

# Ejercicio 5.6b

def suma_potencias(n1,n2):
    suma = 0
    for i in range(n1,n2):
        if es_potencia_de_dos(i) == True:
            suma += i
    return suma