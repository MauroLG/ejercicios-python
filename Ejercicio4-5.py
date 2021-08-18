# Ejercicio 4.5a

def bisiesto(a):
    a_bisiesto = False
    if a % 100 == 0:
        if a % 4 == 0 and a % 400 == 0:
            a_bisiesto = True
        else:
            a_bisiesto = False
    elif a % 4 == 0:
        a_bisiesto = True
    else:
        a_bisiesto = False
    return a_bisiesto


# Ejercicio 4.5b

def cant_dias(m, a):
    # Lista [mes, dias]. Febrero tiene dos posibles cantidad de días.
    meses = [[1, 31],[2, 28, 29], [3, 31], [4, 30], [5, 31], [6, 30], [7, 31], [8, 31], [9, 30], [10, 31], [11, 30], [12, 31]]
    # Verifico si el año es bisiesto o no para luego, en caso de que el mes sea febrero, devolver el mes de 29 o 28 días según corresponda.
    a_bisiesto = bisiesto(a)
    for i in range(len(meses)):
        if meses[i][0] == m:
            if m == 2 and a_bisiesto == True:
                return meses[i][2]
            else:
                return meses[i][1]

# Ejercicio 4.5c

def fecha_valida(d, m, a):
    if d == 0:
        return False
    if d <= cant_dias(m, a):
        return True
    else:
        return False

# Ejercicio 4.5.d

def dias_fin_de_mes(d, m, a):
    if fecha_valida(d, m, a) == True:
        return cant_dias(m, a) - d

# Ejercicio 4.5.e

def dias_fin_de_a(d, m, a):
    # Chequeo si la fecha es válida. Si no lo es, freno la función.
    if fecha_valida(d, m, a) == False:
        return fecha_valida(d, m, a)
    meses = [[1, 31],[2, 28, 29], [3, 31], [4, 30], [5, 31], [6, 30], [7, 31], [8, 31], [9, 30], [10, 31], [11, 30], [12, 31]]
    # Genero una variable de días restantes del año y le asigno como valor inicial los días restantes del mes que recibo
    d_restantes_a = dias_fin_de_mes(d, m, a)
    # La variable i es la posición del mes en el array y m es el mes recibido. Al haber contado ya los días restantes del mes
    # el valor de m (que siempre es +1 que la posición) lo utilizo para que i comience con la posición siguiente al mes recibido.
    i = m
    # Mientras la posición de mi array sea menor a la última chequeo si el año es bisiesto y si el mes siguiente a contar completo es Febrero
    # si lo es, sumo el valor de la posición correspondiente a los 29 días, y sino, sea el año o no bisiesto y cualquier mes, sumo el valor de la posición de los dias.
    while i < meses[11][0]:
        if(bisiesto(a) == True and i == 1):
                d_restantes_a += meses[i][2]
        else:
                d_restantes_a += meses[i][1]
        i += 1
    return d_restantes_a



# Ejercicio 4.5.f
def dias_transcurridos(d, m, a):
    if fecha_valida(d, m, a) == False:
        return fecha_valida(d, m, a)
    d_a = 0
    if bisiesto(a) == True:
        d_a = 366
    else:
        d_a = 365
    return d_a - dias_fin_de_a(d, m, a)
    


# Ejercicio 4.5.g
def tiempo_transcurrido(d1, m1, a1, d2, m2, a2):
    # Chequeo si las fechas dadas son válidas
    if fecha_valida(d1, m1, a1) == False or fecha_valida(d2, m2, a2) == False:
        return False
    # tta = tiempo transcurrido en años
    # ttd = tiempo transcurrido en dias
    # ttm = tiempo transcurrido en meses
    tta = a2 - a1
    ttd = 0
    ttm = 0
    # Si el mes de la primer fecha es anterior al mes de la segunda fecha, la cantidad de años se mantiene igual ya que la diferencia es de más de 12 meses
    # Si el mes de la primer fecha es posterior al mes de la segunda fecha, la cantidad de años se reduce en 1 ya que la diferencia es menor a 12 meses
    # Si los meses son los mismos y si los días de la primer fecha son anteriores a los de la segunda o son iguales, la cantidad de años se mantiene igual ya que
    # la diferencia de años será de 1 año entero o más.
    # Si los meses son los mismos y los días de la primer fecha son posteriores a los de la segunda fecha, la cantidad de años reduce en 1 ya que la diferencia
    # no es de un año completo.
    if m1 < m2:
        tta = tta
    elif m1 > m2:
        tta -= 1
    else:
        if d1 < d2 or d1 == d2:
            tta = tta
        else:
            tta -= 1
    # Si el mes de la primer fecha es anterior al mes de la segunda fecha, cuento la cantidad de meses de diferencia
    # Si el mes de la primer fecha es posterior al mes de la segunda fecha, cuento la cantidad de meses restantes hasta llegar al último mes de año
    # y luego cuento la cantidad de meses hasta llegar al mes de la segunda fecha
    temp_m1 = m1
    if m1 < m2:
        while(temp_m1 < m2):
            ttm += 1
            temp_m1 += 1
    elif m1 > m2:
        while(temp_m1 < 12):
            ttm += 1
            temp_m1 += 1
        i = 0
        while(i < m2):
            i += 1
            ttm += 1
    # Si la cantidad de días de la primer fecha es mayor a la cantidad de días de la segunda fecha sumo la cantidad de días que restan a llegar
    # a fin de ese mes y la cantidad de días del segundo mes. A su vez la cantidad de meses contados se reduce en uno si los meses no son los mismos 
    # ya que el mes no transcurre completamente.
    # Si la cantidad de dias de la primer fecha es menor a la cantidad de días de la segunda fecha o si son iguales, simplemente calculo la diferencia entre ambos.
    if d1 > d2:
        ttd = dias_fin_de_mes(d1,m1,a1) + d2
        if not m1 == m2:
            ttm -= 1
    else:
        ttd = d2 - d1

    return ttd,ttm,tta

print(tiempo_transcurrido(19,6,1990,18,5,2020))

