a = int(input("Введіть кількість строк матриці "))
b = int(input("Введіть кількість стовпців матриці "))

m = []

for i in range(a):
    l = []
    for j in range(b):
        s = "введіть значення матриці для значення {} {} ".format(i+1, j+1)
        l.append(int(input(s)))
    m.append(l)

for i in range(a):
    s = 0
    for j in range(i, b):
        s += m[j][i]
    print('сума стовпця № {} нижче головної діагоналі {}'.format(i + 1, s))
