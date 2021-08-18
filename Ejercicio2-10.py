def fichas_juego(n):
    i = 0
    j = 0
    # Creo un número auxiliar que me ayude a no repetir las fichas del juego
    aux = n - 1
    while i < n + 1:
        while j < n:
            print("|" + str(i) + "|" + str(j) + "|")
            j = j + 1
        print("|" + str(i) + "|" + str(j) + "|")
        i = i + 1
        # Aqui al finalizar el while, "j" siempre toma el valor de n. 
        # El auxiliar le resta empezando por n - 1, uno menos por cada while que se complete
        # para que j no repita fichas ya mostradas
        j = j - aux
        aux = aux - 1

fichas_juego(12)