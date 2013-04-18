## A Pythagorean triplet is a set of three natural
## numbers, a  b  c, for which,

## a2 + b2 = c2
## For example, 32 + 42 = 9 + 16 = 25 = 52.

## There exists exactly one Pythagorean triplet for
## which a + b + c = 1000.
## Find the product abc.

def num9():
    for c in range(999, 0, -1):
        for b in range(c-1, 0, -1):
            a = 1000-b-c
            if a < 0:
                continue
            if a**2 + b**2 == c**2:
                return a*b*c, a, b, c

print num9()
