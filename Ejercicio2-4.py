# Defino función para convertir F a C
def farenheit_a_celsius(grados_f):
    grados_c = (grados_f - 32) * 5/9
    return grados_c

def tabla_conversion():
    i = 0
    while i <= 120:
        # Llamo a la función y le paso los valores que va tomando 'i' en el loop while que serían los grados a convertir.
        # Redondeo a dos decimales
        conversion = round(farenheit_a_celsius(i), 2)
        print("Grados Farenheit: {i} | Grados Celsius: {conversion}".format(i=i,conversion=conversion))
        i = i + 10

tabla_conversion()