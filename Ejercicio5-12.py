def evaluacion_examenes(total_ejercicios, porcentaje_aprobacion):
    ejercicios_resueltos = 0
    
    while not ejercicios_resueltos == "*":
        ejercicios_resueltos = int(input("Ingresa la cantidad de ejercicios resueltos. Para finalizar ingresa '-1': "))
        if ejercicios_resueltos == -1:
            return
        porcentaje_ejercicios_resueltos = (ejercicios_resueltos * 100) / total_ejercicios
        if porcentaje_ejercicios_resueltos >= porcentaje_aprobacion:
            print(str(porcentaje_ejercicios_resueltos) + "%", "Aprobado")
        else:
            print(str(porcentaje_ejercicios_resueltos) + "%", "Desaprobado")

evaluacion_examenes(50, 60)