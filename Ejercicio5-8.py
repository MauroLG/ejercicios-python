def ingresa_numeros():
    print("Ingresa una suceción de números, uno a la vez. Ingresa '-1' cuando quieras finalizar.")
    numeros = []
    texto = "Ingresa un número: "
    recibido = 0
    suma = 0
    promedio = 0
    while not recibido == -1:
        recibido = int(input(texto))
        if recibido == -1:
            for i in range(len(numeros)):
                suma += numeros[i]
            promedio = suma/len(numeros)
            return (len(numeros), suma, promedio)
        numeros.append(int(recibido))
        texto = texto.replace("un", "otro")
    
print(ingresa_numeros())