# Ejercicio 2.5a
def par_o_impar(nro):
    if nro % 2 == 0:
        return 0
    else:
        return 1

# Ejercicio 2.5b

def impar_o_par(nro):
    if not(nro % 2 == 0):
        return 0
    else:
        return 1

# Ejercicio 2.5c

def digito_unidad(nro):
    return int(repr(nro)[-1])

# Ejercicio 2.5d

def multiplo_10(nro):
    return nro - int(repr(nro)[-1])





