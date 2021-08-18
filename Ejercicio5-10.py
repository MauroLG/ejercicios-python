import math

def numeros_primos_hasta(n):
    for i in range(2,n):
        if(math.factorial(i - 1) + 1) % i == 0:
            print(i)

numeros_primos_hasta(100)