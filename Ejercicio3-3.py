def mayor_producto(a,b,c,d):
    numeros = [a,b,c,d]
    prod = 0
    mayor_prod = 0
    i = 0
    while i < len(numeros):
        j = i + 1
        while j < len(numeros):
            prod = numeros[i] * numeros[j]
            if prod > mayor_prod:
                mayor_prod = prod
            j += 1
        i += 1
    return mayor_prod

# Creo una lista de numeros, declaro una variable prod para
# guardar el producto actual y declar otra variable para
# guardar el mayor producto