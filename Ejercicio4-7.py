def numero_romano(nro):
    # Creo 2 listas que coinciden sus valores traducidos mediante el indice.
    # Creo todos los números romanos, así como también los números anteriores donde debo ubicar 
    # un numero romano delante para simplificar el código. 
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numeros_romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    convertido = ""
    # A medida que recorro el array 'numeros', concateno las letras a la variable 'convertido', luego al 'nro' le resto el número de la posición que estoy leyendo del array 'numeros'
    for i in range(len(numeros)):
        while (numeros[i] <= nro):
            convertido += numeros_romanos[i]
            nro -= numeros[i]
    return convertido