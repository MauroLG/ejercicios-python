# Ejercicio 5.7a

def suma_divisores_de(n):
    suma = 0
    for i in range(1,n):
        if n % i == 0:
            suma += i
    return suma


# Ejercicio 5.7b

def numeros_perfectos(m):
    nros_perfectos = []
    for i in range(1,m + 1):
        if i == suma_divisores_de(i):
            nros_perfectos.append(i)
    return nros_perfectos

# Ejercicio 5.7c

# No logré hacerlo aún =(
