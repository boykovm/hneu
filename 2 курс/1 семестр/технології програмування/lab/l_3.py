n1, n2 = map(int, input('Введіть в одному рядку два числа ').split())

m = max(abs(n1), abs(n2))

s = None

i = 1
while i <= m:
    if n1 % i == 0 and n2 % i == 0:
        s = i
    i += 1

print(f'НСД чисел {n1} і {n2} - це {s}')
