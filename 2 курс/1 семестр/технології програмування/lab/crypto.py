a = int(input('a = '))
b = int(input('b = '))
d = int(input('d = '))
m = int(input('m = '))

def nod(a, b):
    # if (b > a):
    #     return nod(b, a)
    if (a % b == 0):
        return b
    return nod(b, a % b)


def solution(a, b, m, d = 0):
    if d == 0:
        print(str(a) + 'x = ' + str(b) + '(mod ' + str(m) + ')')
    else:
        print(str(a) + 'x + ' + str(d) + ' = ' + str(b) + '(mod ' + str(m) + ')')
        b = b - d

    c = nod(a, m)
    print('c = ' + str(c))
    if b % c != 0:
        print('нет решений')
        return

    l = [x for x in range(m)]

    s = []

    for i in l:
        if (a * i - b) % m == 0:
            s.append(i)

    if c == len(s):
        print("решения " + str(s))
    else:
        print('решай сам')

solution(a, b, m, d)
