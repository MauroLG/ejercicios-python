import math

# Ejercicio 4.1a

def numero_par(nro):
    if nro % 2 == 0:
        print(str(nro) + " es un número par.")
    else:
        print(str(nro)+ " no es un número par.")

numero_par(6)
numero_par(13)

# Ejercicio 4.1b

def numero_primo(nro):
    # Por teorema de Wilson un número es primo si y solo si
    # (n-1)! + 1 es multiplo de n
    if(nro == 1):
        return print("1 no es un número primo.")
    if (math.factorial(nro - 1) + 1) % nro == 0:
        print(str(nro) + " es un número primo.")
    else:
        print(str(nro) + " no es un número primo.")

numero_primo(13)
numero_primo(21)
