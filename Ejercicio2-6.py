def numeros_pares_entre():
    nro1 = int(input("Por favor ingrese un número: "))
    nro2 = int(input("Por favor ingrese otro número: "))
    if nro1 < nro2:
        for i in range(nro1 + 1, nro2):
            if(i % 2 == 0):
                print(i)
    elif nro1 > nro2:
        for i in range(nro2 + 1, nro1):
            if(i % 2 == 0):
                print(i)

numeros_pares_entre()