def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

def factoriales():
    valores = []
    seguir = "S"
    i = 0
    valores.insert(i, int(input("Por favor ingrese al menos un número: ")))
    while seguir == "S":
        seguir = input("Desea seguir ingresando números? Ingrese S (sí) o N (no): ")
        if seguir == "S":
            i = i + 1
            valores.insert(i, int(input("Por favor ingrese otro número: ")))
        elif seguir == "N":
            for v in valores:
                print("El factorial de {v} es:".format(v=v), end=" ")
                print(str(factorial(v)))
        else: 
            print("Usted ha ingresado una opción incorrecta. Se cerrará el programa")

factoriales()