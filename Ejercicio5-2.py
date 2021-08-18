def factores_primos(k):
    f_primos = []
    for i in range (2, k+1):
        while k % i == 0:
            f_primos.append(i)
            k = k / i
            if(k == 1):
                return f_primos