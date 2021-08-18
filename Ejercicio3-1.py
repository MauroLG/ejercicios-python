import math
# Ejercicio 3.1a

def intervalo_a_seg(h, m, s):
    s += h * 3600
    s += m * 60
    return s

# Ejercicio 3.1b

def intervalo_a_hms(s):
    total_s = s
    h = round(math.modf(s/3600)[1])
    m = round(math.modf((math.modf(s/3600)[0]*3600)/60)[1])
    s = round(math.modf((math.modf(s/3600)[0]*3600)/60)[0]*60)
    print("{total_s} segundos son {h} hora/s, {m} minuto/s y {s} segundo/s".format(total_s=total_s, h=h, m=m, s=s))
