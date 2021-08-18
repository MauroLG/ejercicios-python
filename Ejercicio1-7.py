def repetir_palabra():
    palabra = input("Por favor ingrese una palabra: ")
    for _ in range(1000):
        print(palabra, end=" ")

repetir_palabra()