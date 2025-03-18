def es_primo(n): #definimos la función es_primo
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def encontrar_primos_gemelos(limite): #definimos la función encontrar_primos_gemelos  
    primos = [n for n in range(2, limite + 1) if es_primo(n)]
    return [(primos[i], primos[i + 1]) for i in range(len(primos) - 1) if primos[i + 1] - primos[i] == 2]