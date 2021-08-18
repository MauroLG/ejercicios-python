def numeros_triangulares():
    n = int(input("Por favor ingrese un numero: "))
    i = 1
    total = 1
    aux = 2
    while i < n + 1:
        print("{i} - {total}".format(i=i, total=total))
        total = total + aux
        aux = aux + 1
        i = i + 1

# La función que hice yo realiza más operaciones (pasos) ya que utiliza un número auxiiar.
# En cuanto a operaciones matemáticas, la ecuación que da el ejercicio 
# realiza 3 operaciones en una linea como suma, multiplicación y división, mientras
# que la función mia solo realiza sumas.

def numeros_triangulares_ecu():
    n = int(input("Por favor ingrese un numero: "))
    i = 1
    total = 1
    while i < n + 1:
        print("{i} - {total}".format(i=i, total=total))
        i = i + 1
        total = round(i * (i + 1) / 2)

print(numeros_triangulares_ecu())
