# Ejecicio 1.6a

def operaciones(nro1, nro2):
    print("Suma:")
    print(nro1 + nro2)
    print("Resta:")
    print(nro1 - nro2)
    print("División:")
    print(nro1 * nro2)
    print("Multiplicación:")
    print(nro1 / nro2)

#Ejercicio 1.6b

def tabla_de_multiplicar(n):
    for i in range(1, 11):
        print(str(n) + " x " + str(i) + " = " + str(n*i))
