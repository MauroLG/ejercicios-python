import math

def intervalo_a_seg(h, m, s):
    s += h * 3600
    s += m * 60
    return s

def intervalo_a_hms(s):
    total_s = s
    h = round(math.modf(s/3600)[1])
    m = round(math.modf((math.modf(s/3600)[0]*3600)/60)[1])
    s = round(math.modf((math.modf(s/3600)[0]*3600)/60)[0]*60)
    return print("{h} hora/s, {m} minuto/s y {s} segundo/s".format(total_s=total_s, h=h, m=m, s=s))

def suma_intervalos():
    intervalo1 = []
    intervalo2 = []
    tipo = ["las horas", "los minutos", "los segundos"]
    for i in range(3) :
        intervalo1.insert(i, int(input("Por favor ingrese " + tipo[i] + " del primer intervalo: ")))
        intervalo2.insert(i, int(input("Por favor ingrese " + tipo[i] + " del segundo intervalo: ")))
    seg_intervalo1 = intervalo_a_seg(intervalo1[0], intervalo1[1], intervalo1[2])
    seg_intervalo2 = intervalo_a_seg(intervalo2[0], intervalo2[1], intervalo2[2])
    print("La suma de los intervalos es de", end=" ")
    intervalo_a_hms(seg_intervalo1 + seg_intervalo2)

suma_intervalos()
