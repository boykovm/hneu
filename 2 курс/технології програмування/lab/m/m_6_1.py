n = int(input("Введіть кількість елементів "))

positive_numbers = []

while n > 0:
    number = int(input("Введіть число для обчислення "))
    if number > 0:
        positive_numbers.append(number)
    n -= 1

print("Сума п'яти останніх позитивних елементів - {}".format(sum(positive_numbers[-5::])))

