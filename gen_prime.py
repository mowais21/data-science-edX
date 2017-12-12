def genPrimes():
    primes = []
    x=2
    prime = False

    while True:
        if x == 2:
            prime = True
        else:
            for p in primes:
                if (x % p != 0):
                    prime = True
                else:
                    prime = False
                    break
        if prime == True:
            primes.append(x)
            yield x
        x+=1
pr = genPrimes()
print(type(genPrimes()))
