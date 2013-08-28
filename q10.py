## The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

## Find the sum of all the primes below two million.

def prime(n):
     if n%2 == 0:
         return False
     for i in range(3, int(n**0.5)+1, 2):
         if n%i == 0:
             return False
     return True


def num10(n):
    L = [2]
    for i in range(3, n+1, 2):
        if prime(i):
            L.append(i)
    sum = 0
    for i in L:
        sum += i
    return sum

print num10(2000000)
