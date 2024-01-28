UPPER_LETTERS = [
    "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V",
    "B", "N", "M", "Й", "Ц", "У", "К", "Е", "Н", "Г", "Ш", "Щ", "З", "Х", "Э", "Ж", "Д", "Л", "О", "Р", "П", "А", "V",
    "В", "V", "Ф", "Я", "Ч", "С", "М", "И", "Т", "Б", "Ю", "Ё", "І", "Ї",
]
SPLITTERS = [",", ".", "?", "!", ";"]

l = input("Введіть рядок ")

for i in SPLITTERS:
    l = l.replace(i, " ")

l = l.split(" ")

l1 = [x for x in l if x != '']

c = 0
for i in l1:
    if i[0] in UPPER_LETTERS:
        c += 1

print(c)




