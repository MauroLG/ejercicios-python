import random

def adivinar_numero():
    numero_random = random.randrange(100)
    numero = int(input("Se ha generado un numero aleatorio, ¡a ver si podés adivinarlo!\nIngresá un número del 0 al 100: "))
    while not numero_random == numero:
        if numero < numero_random:
            numero = int(input("El numero que ingresaste es menor. \nIngresa otro: "))
        if numero > numero_random:
            numero = int(input("El numero que ingresaste es mayor. \nIngresa otro: "))
    return print("¡Adivinaste el número!")

adivinar_numero()