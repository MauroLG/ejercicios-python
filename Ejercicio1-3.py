import math

# Ejercicio 1.3.a
def perimetro_rectangulo(b, h):
    return (b + h) * 2

# Ejercicio 1.3.b
def area_rectangulo_bh(b, h):
    return b * h

# Ejercicio 1.3.c

def area_rectangulo_coor(x1,x2,y1,y2):
    return ((x2 - x1) *(y2 - y1))

# Ejercicio 1.3.d

def perimetro_circulo(radio):
    return (2 * math.pi * radio)

# Ejercicio 1.3.e

def area_circulo(radio):
    return (math.pi * radio**2)

# Ejercicio 1.3.f

def volumen_esfera(radio):
    return (4/3 * math.pi * radio**3)

# Ejercicio 1.3.g

def calcular_hipotenusa(cateto1, cateto2):
    return math.sqrt(cateto1**2 + cateto2**2)
