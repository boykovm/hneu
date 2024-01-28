# Шифр магічний квадрат!
print("Шифр магічний квадрат!")


# створюємо функцію генерації магічного квадрата
def magic_square(n):
    length = n * n
    mx = [[None for z in range(n)] for z in range(n)]
    y = 0
    x = n // 2
    mx[y][x] = 1
    for i in range(2, length + 1):
        old_x, old_y = x, y
        x = (x + 1) % n
        y = (y - 1) % n
        if not mx[y][x] is None:
            x = old_x
            y = (old_y + 1) % n
        mx[y][x] = i
    a = []
    for y in mx:
        a += y
        print(' '.join(map(str, y)))
    return a

n1 = int(input("Введіть розмір магічного квадрата: "))
# Вносимо значення магічного квадрату у нову змінну
m = magic_square(n1)


# Створюємо функцію кодування
def enc(message):
    # Записуємо розмір таблиці у нову змінну
    size = n1 ** 2

    # Визначаємо кількість рядків, на які буде ділитись наш текст
    if len(message) % size != 0:
        a = len(message) // size + 1
    else:
        a = len(message) // size

    # У тексті міняємо пробіли на підкреслення
    message = message.replace(' ', '_')

    # Шифруємо наш текст за допомогою сгенерованих значень магічного квадрата
    f1 = ''
    for i in range(0, a):
        for j in range(size):
            el = m[j] + i * size - 1
            # Так як текст не завжди може заповняти конжу клітинку таблиці, то потрібно виключити з циклу
            # можливість брати ті номера знаків, які більше довжини самого тексту
            try:
                f1 += str(message[el])
            except IndexError:
                continue
    return f1


message1 = input('Введіть текст: ').lower()
print("Зашифрований текст: " + enc(message1))

