import time

# Ejercicio 5.3a

def password():
    password = "cursofec2020"
    sol_password = input("Por favor ingrese la contraseña: ")
    while not password == sol_password:
       sol_password = input("Password incorrecto. Por favor vuelva a ingresar la contraseña: ")
    print("La contraseña es correcta.")



# Ejercicio 5.3b

def password2():
    password = "cursofec2020"
    sol_password = input("Por favor ingrese la contraseña: ")
    i = 0
    while not password == sol_password:
        if i == 3:
            return print("Se han producido demasiados intentos.")
        sol_password = input("Password incorrecto. Por favor vuelva a ingresar la contraseña: ")
        i += 1
    return print("La contraseña es correcta.")


# Ejercicio 5.3c

def password3():
    password = "cursofec2020"
    sol_password = input("Por favor ingrese la contraseña: ")
    i = 0
    pausa = 2
    while not password == sol_password:
        if i == 3:
            return print("Se han producido demasiados intentos.")
        sol_password = input("Password incorrecto. Por favor vuelva a ingresar la contraseña: ")
        if not password == sol_password:
            time.sleep(pausa)
            pausa += 1
        i += 1
    return print("La contraseña es correcta.")

# Ejercicio 5.3d

def password4():
    password = "cursofec2020"
    sol_password = input("Por favor ingrese la contraseña: ")
    i = 0
    pausa = 2
    aviso_acceso = False
    while not password == sol_password:
        if i == 3:
            return aviso_acceso
        sol_password = input("Password incorrecto. Por favor vuelva a ingresar la contraseña: ")
        if not password == sol_password:
            time.sleep(pausa)
            pausa += 1
        i += 1
    aviso_acceso = True
    return aviso_acceso


