c = int(input('Кількість значен в таблиці: '))
d = float(input('Інтервал значень: '))

t = 0
g = 9.8

print('-' * 40)
print('Час, с \t\t\t Швидкість, м/с')
print('-' * 40)
for i in range(c):
    v = g * t
    print('{:.2f}\t\t\t\t{:.2f}'.format(t, v))
    t += d
l