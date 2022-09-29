a = int(input("Введіть кількість строк матриці "))
b = int(input("Введіть кількість стовпців матриці "))

m = []

for i in range(a):
    l = []
    for j in range(b):
        s = "введіть значення матриці для значення {} {} ".format(i+1, j+1)
        l.append(int(input(s)))
    m.append(l)

small = m[0][0]
summa = [0 for x in range(b)]

for i in range(a):
    for j in range(b):
        if i // 2 == 0:
            summa[j] += m[i][j]
        if small > m[i][j]:
            small = m[i][j]

print("Найменше число = {}".format(small))

for i in range(len(summa)):
    print("сума елементів стовбця {} кожного непарного рядка дорівнює {}".format(i + 1, summa[i]))
