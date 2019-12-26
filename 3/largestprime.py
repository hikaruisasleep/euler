def primes(n):
    i = 2
    primelist = []
    while i * i < n:
        if n % i:
            i += 1
        else:
            n //= i
            primelist.append(i)
    if n > 1:
        primelist.append(n)
    return primelist

print(primes(600851475143)[-1])
