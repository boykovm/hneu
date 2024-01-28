import math
from random import randint
from sympy import randprime, primerange

# phrase = input("Input phrase for encryption: ")
key_len = int(input('Input key len: '))




def generate_prime_numbers(key_len):
    l = []
    count = 3

    while len(l) != key_len:
        isprime = True

        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                isprime = False
                break

        if isprime:
            l.append(count)

        count += 1
    return l

prime_numbers = generate_prime_numbers(key_len)
p_1 = prime_numbers[randint(0, len(prime_numbers) - 1)]
p_2 = prime_numbers[randint(0, len(prime_numbers) - 1)]

print(p_1, p_2)

mod = p_1 * p_2
phi = (p_1 - 1) * (p_2 - 1)

spisok = list(primerange(1, phi))

for n in spisok:
    if gcd(n, phi) == 1:
        e = n
        break

def ex(prime_number = 3):
    b = list("Hello Wold!")
    b = [ord(elem) for elem in b]
    print("Before encrypt:")
    print(b)
    for i in range(len(b)):
        # b[i] *= e  # неправильно
        b[i] = b[i] ** prime_number  # нужно - возведение в степень
        b[i] %= mod
    print("After encrypt:")
    print(b)
    for i in range(len(b)):
        b[i] = b[i] ** d  # и при дешифровке возведение в степень
        b[i] %= mod
    print("After decrypt:")
    print(b)

ex(p_1)