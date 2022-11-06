def primos(x):
    numeros = list(range(2, x + 1))
    d = 0
    while numeros[d] ** 2 <= x:
        for n in numeros:
            if n != numeros[d]:
                if n % numeros[d] == 0:
                    numeros.remove(n)
        d += 1
    return numeros


def filter_factor_only_condition(x, primo):
    if x % primo == 0:
        return True
    return False


def get_filter_only_factors_primos(x, primos_list):
    filter_primos = []

    for primo in primos_list:
        if filter_factor_only_condition(x, primo):
            filter_primos.append(primo)
    return filter_primos


t = int(input().strip())
for a0 in range(t):
    x = int(input().strip())
    primos_list = primos(x)
    filter_only_factors_primos = get_filter_only_factors_primos(x, primos_list)

    try:
        max_factor = max(filter_only_factors_primos)
        print(max_factor)
    except ValueError:
        continue
