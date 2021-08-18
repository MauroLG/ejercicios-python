def calculo_tasa(cap_ini, tasa, años):
    monto_final = cap_ini * (1 + tasa/100) ** años
    return monto_final