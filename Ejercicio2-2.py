def calculo_tasa():
    cap_ini = int(input("Por favor ingrese su capital inicial en pesos: "))
    tasa = int(input("Por favor ingrese la tasa de interés: "))
    años = int(input("Por favor ingrese los años: "))
    
    monto_final = cap_ini * (1 + tasa/100) ** años
    
    print("Usted obtendrá " + str(monto_final) + " pesos")

calculo_tasa()