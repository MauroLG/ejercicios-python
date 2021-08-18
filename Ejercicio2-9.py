def fichas_domino():
    i = 0
    j = 0
    # Creo un número auxiliar que me ayude a no repetir las fichas domino
    aux = 5
    while i < 7:
        while j < 6:
            print("|" + str(i) + "|" + str(j) + "|")
            j = j + 1
        print("|" + str(i) + "|" + str(j) + "|")
        i = i + 1
        # Aqui al finalizar el while, "j" siempre toma el valor 6. 
        # El auxiliar le resta empezando por 5, uno menos por cada while que se complete
        # para que j no repita dominos ya mostrados
        j = j - aux
        aux = aux - 1

fichas_domino()