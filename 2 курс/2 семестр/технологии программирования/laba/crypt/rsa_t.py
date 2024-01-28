from sympy import randprime, primerange
from math import gcd


def find_two_primes():
    p1 = randprime(1, 100)
    p2 = randprime(1, 100)
    while p1 == p2:
        p2 = randprime(1, 100)
    return (p1, p2)


a = find_two_primes()
print(f'(p, q) = {a}')
mod = a[0] * a[1]
print(f'mod = {mod}')
phi = (a[0] - 1) * (a[1] - 1)
print(f'phi = {phi}')
spisok = list(primerange(1, phi))

for n in spisok:
    if gcd(n, phi) == 1:
        e = n
        break
values = [x for x in range(1, phi + 1)]
d = 0
for elem in values:
    if (int(elem) * e) % phi == 1:
        d += int(elem)
        break
print(f'e = {e}')
print(f'd = {d}')
open_key = (e, mod)
private_key = (d, mod)
print(f'open_key = {open_key}')
print(f'private_key = {private_key}')
b = list(input())
b = [ord(elem) for elem in b]
print("Before encrypt:")
print(b)
for i in range(len(b)):
    b[i] **= e
    b[i] %= mod
print("After decrypt:")
print(b)
print(''.join([chr(el) for el in b]))