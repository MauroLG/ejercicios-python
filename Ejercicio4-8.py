def astrologia():
    nombre_signos = ["Aries","Tauro","Géminis","Cancer","Leo","Virgo","Libra","Escorpio","Sagitario","Capricornio","Acuario","Piscis"]
    fecha_signos = [
                    [21, "marzo", 20, "abril"],
                    [21,"abril",20,"mayo"],
                    [21,"mayo",21,"junio"],
                    [22,"junio",23,"julio"],
                    [24,"julio",23,"agosto"],
                    [24,"agosto",23,"septiembre"],
                    [24,"septiembre",22,"octubre"],
                    [23,"octubre",22,"noviembre"],
                    [23,"noviembre",21,"diciembre"],
                    [22,"diciembre",20,"enero"],
                    [21,"enero",19,"febrero"],
                    [20,"febrero",20,"marzo"],
                   ]
    dia = int(input("Por favor ingresa el día que naciste (ejemplo: 18): "))
    mes = input("Por favor ingresa el mes que naciste (ejemplo: marzo): ").lower()

    # Chequeo si el día y la fecha recibida se encuentran dentro del rango que determino con la condición del if.
    for i in range(len(fecha_signos)):
        if (dia >= fecha_signos[i][0] and mes == fecha_signos[i][1]) or (dia <= fecha_signos[i][2] and mes == fecha_signos[i][3]):
                return print("Tu signo es " + nombre_signos[i])

astrologia()