# Шифр Трісемуса до українського алфавіту

print(f'Шифр Трісемуса!\n{"-"*15}')
alphabet_UK = "абвгдеєжзиіїйклмнопрстуфхцчшщьюя .,'"
key_word = input("Введіть ключове слово -> ").lower()
message = input("Введіть повідомлення, яке хочете зашифрувати -> ").lower()

# Формуємо список і відкидаємо літери, які повторюються
new_key = []
for i in key_word:
    if i not in new_key:
        new_key.append(i)
print(f'\nОтримаємо новий ключ, без повторів:\n{new_key}')

# Формуємо новий алфавіт, видаливши літери з нового ключового слова
for i in new_key:
    if i in alphabet_UK:
        alphabet_UK = alphabet_UK.replace(i, '')

# Формуємо таблицю представлень
my_list = []
my_list.extend(new_key)
my_list.extend(alphabet_UK)

# Формуємо таблицю, тобто матрицю 6х6
count = 0
table = [[0] * 6 for i in range(6)]
for i in range(6):
    for j in range(6):
        table[i][j] = my_list[count]
        count += 1

# Виводимо таблицю в зручному форматі
print("\nГотова таблиця для шифрування:")
for i in table:
    print(i)

# Зашифровуємо текст
mylist = list(message)
cipher_text = []
for e in mylist:
    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] in e:
                if i == len(table) - 1:
                    cipher_text.append(table[0][j])
                else:
                    cipher_text.append(table[i + 1][j])
print("\nПовідомлення - >", message)
print("Зашифроване повідомлення ->", "".join(cipher_text))
