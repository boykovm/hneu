import re

def PrintT1():
    print("Перша таблиця:")
    for i in range(len(table1)):
        for j in range(len(table1[i])):
            print(table1[i][j], end=' ')
        print()

def PrintT2():
    print("Друга таблиця:")
    for i in range(len(table2)):
        for j in range(len(table2[i])):
            print(table2[i][j], end=' ')
        print()

def Bigramms(text1):
    bigramm = re.findall('..?',text1)
    print("Исходны биграмми:", bigramm)
    return bigramm

table1 = [
    ["і", "п", "у", "й", "я"],
    ["н", "а", "ь", "ц", "ф"],
    ["щ", "с", "л", "э", "б"],
    [" ", "в", "ч", "ж", "к"],
    ["у", "е", "м", ",", "ю"],
    ["р", "о", "ї", "г", "."],
    ["д", "з", "ш", "т", "и"],
]
table2 = [
    ["а", "щ", " ", "т", "д"],
    ["к", "с", "г", "о", "е"],
    ["п", ".", "й", "ї", "ш"],
    ["ф", "х", "р", "я", "л"],
    ["і", "б", "ч", "ю", "н"],
    ["ж", "и", "у", "м", "ь"],
    ["в", "э", "ц", ",", "з"],
]

PrintT1()
PrintT2()

print("Введіть текст: ")
text1 = input().lower()

bigramm = Bigramms(text1)