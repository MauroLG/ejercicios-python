# Ejercicio 5.9a

def multiplos_del_primero_for(nro1,nro2):
    m = 0
    for i in range(nro2):
        if m < nro2:
            m = nro1 * i
        if m >= nro2:
            return i

        
# Ejercicio 5.9b

def multiplos_del_primero_while(nro1,nro2):
    i = 0
    m = 0
    while m < nro2:
        m = nro1 * i
        if m < nro2:
            i += 1
    return i


# Ejercicio 5.9c

# De la manera que lo hice ambos hacen la misma cantidad de pasos, aunque while realiza
# 2 operaciones matemáticas, mientras el indice i del for aumenta en 1 automaticamente.
# La utilización del for es la representación más clara
