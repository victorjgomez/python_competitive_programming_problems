import math
from typing import List
from functools import reduce

def es_primo(numero: int) -> bool:
    if numero < 2:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

def get_digits(number: int) -> List[int]:
    digits = []
    number = abs(number)
    while number > 0:
        digits.append(number % 10)
        number //= 10
    return digits

def validate_list_digits_prime(list_digits: List[int]) -> bool:
    for d in list_digits:
        if not es_primo(d):
            return False
    return True

def calcular_mcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def obtener_indicadores_primos(n: int) -> List[bool]:
    prod = 2
    indicadores_primos = inicializar_lista_booleana(n + 1)
    indicadores_primos[2] = True
    for primo in range(3, n + 1, 2):
        resultado_mcd = calcular_mcd(prod, primo)
        if resultado_mcd == 1:
            prod *= primo
            indicadores_primos[primo] = True
    return indicadores_primos

def inicializar_lista_booleana(n: int) -> List[bool]:
    return [False] * n

def get_solution(first: int, last: int) -> int:
    count = 0
    list_indicador_primos = obtener_indicadores_primos(last)
    for i in range(first, last + 1):
        if list_indicador_primos[i]:
            list_digits = get_digits(i)
            if validate_list_digits_prime(list_digits):
                count += 1
    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    first = int(data[0])
    last = int(data[1])
    print(get_solution(first, last))

if __name__ == "__main__":
    main()
