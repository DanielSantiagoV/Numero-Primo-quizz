from modulos.primos import es_primo #importamos la función es_primo

def es_palindromo(n): #definimos la función es_palindromo
    return str(n) == str(n)[::-1]

def encontrar_primos_palindromicos(limite): #definimos la función encontrar_primos_palindromicos
    return [n for n in range(10, limite +1 ) if es_primo(n) and es_palindromo(n)]

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

def encontrar_primos_palindromos(limite): #definimos la función encontrar_primos_palindromos
    primos = [n for n in range(2, limite + 1) if es_primo(n)]
    return [(primos[i], primos[i + 1]) for i in range(len(primos) - 1) if str(primos[i]) == str(primos[i])[::-1] and str(primos[i + 1]) == str(primos[i + 1])[::-1] ]