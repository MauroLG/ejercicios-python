def dia_semana(dia):
    if dia > 366:
        return
    semana = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
    # Los días se ingresan desde el 1 hasta el 366. Para que coincidan con las posiciones del array
    # "[0,1,2...]" le resto 1 al día.
    dias_restantes = dia - 1
    i = 0
    # Voy contando los dias hasta completar 1 semana, cuando completo una semana resto la misma a la cantidad de días restantes, cuando i alcanza al valor de días_restantes
    # devuelvo la posición i del array
    while i < dias_restantes:
        i += 1
        if i == 7:
            i = 0
            dias_restantes -= 7
    
    return semana[i]
