def primes(n):
    # Create a boolean array
    # "prime[0..n]" and initialize
    #  all entries it as true.
    # A value in prime[i] will
    # finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n + 1)]
    prime_list = [i for i in range(2, n + 1)]

    p = 2
    while p * p <= n:

        # If prime[p] is not
        # changed, then it is a prime
        if prime[p] == True:
            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
                try:
                    prime_list.remove(i)
                except ValueError:
                    continue
        p += 1

    return prime_list


def get_first_factor(n, primes_list):
    for prime in primes_list:
        if n % prime == 0:
            return prime

    return None


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    primes_list = primes(n)

    primes_list.sort(reverse=True)

    max_factor = get_first_factor(n, primes_list)

    if max_factor:
        print(max_factor)
