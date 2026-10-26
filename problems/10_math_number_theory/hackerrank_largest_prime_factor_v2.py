def primos(n):
    primes = []
    isPrime = [1 for i in range(n)]
    isPrime[0] = isPrime[1] = 0

    for i in range(n):
        if isPrime[i]:
            primes.append(i)
            h = 2
            while i * h < n:
                isPrime[i * h] = 0
                h += 1

    return primes


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

