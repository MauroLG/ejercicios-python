def promedio_notas():
    notas = []
    promedio = 0
    frase = "Ingrese una nota: "
    while True:
        notas.append(int(input(frase)))
        opcion = input("¿Deséa agregar más notas? (Si-No): ").lower()
        if opcion == "si":
           frase = frase.replace("una", "otra")
        else:
            i = 0
            while i < len(notas):
                promedio += notas[i]
                i += 1
            promedio = promedio/(i)
            return print(promedio)

promedio_notas()