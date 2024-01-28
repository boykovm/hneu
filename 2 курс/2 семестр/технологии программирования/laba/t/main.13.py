from ЛР13 import Route, Train, Stop, Ticket, TrainTicketOffice, SoldOutError , Carriage

# Створення об'єкту TrainTicketOffice
tto = TrainTicketOffice()

# Створення станцій та зупинок
kharkiv = Stop('Kharkiv', '10:00', '10:05')
kyiv = Stop('Kyiv', '12:30', '12:35')
poltava = Stop('Poltava', '15:00', '15:05')
lviv = Stop('Lviv', '18:00', '18:20')

# Створення маршрутів та додавання зупинок
route1 = Route('001', 'Kharkiv', 'Kyiv',  [kharkiv, kyiv])
route2 = Route('002', 'Kyiv', 'Lviv', [kyiv, poltava, lviv])
route3 = Route('003', 'Kharkiv', 'Lviv', [kharkiv, kyiv, poltava, lviv])

# Додавання поїздів до TrainTicketOffice
#Створення списку вагонів
carriages1 = [(36, 10), (40, 10), (32, 10)]
carriages2 = [(36, 3), (40, 3), (32, 3)]

tto.add_train('228', route1, '2023-04-20', carriages1)
tto.add_train('229', route2, '2023-04-25', carriages1)
tto.add_train('001', route3, '2023-05-20', carriages1)
tto.add_train('LUX1', route1, '2023-04-20', carriages2)
tto.add_train('LUX2', route2, '2023-04-25', carriages2)
tto.add_train('LUX3', route3, '2023-05-20', carriages2)
# Продаж квитків
for train in tto.trains:
    if train.train_number == '228':
        for j in range(1,11):
            for i in range(1, 4):
                try:
                    if tto.sell_ticket('228', route1, '2023-04-20', j, i, f'Passenger_fuul_name {i}', 'Kharkiv', 'Kyiv'):
                        print('Ticket sold successfully!')
                except SoldOutError as e:
                    print(f'Ticket for seat {i} is already sold: {e}')
                    print('Do you want to see available seats? (yes/no)')
                    choice = input().lower()
                    if choice == 'yes':
                        available_seats = []
                        for k in range(1, 4):
                            try:
                                tto.sell_ticket('228', route1, '2023-04-20', j, k, f'Passenger_fuul_name {k}', 'Kharkiv', 'Kyiv')
                            except SoldOutError:
                                available_seats.append(k)
                        print(f'Available seats for carriage {j}: {available_seats}')
                    elif choice == 'no':
                        continue
                    else:
                        print('Invalid choice. Please enter yes or no.')

    elif train.train_number == 'LUX1':
        for j in range(1, 4):
            for i in range(1, 3):
                try:
                    if tto.sell_ticket('LUX1', route1, '2023-04-20', j, i, f'Passenger_fuul_name {i}', 'Kharkiv', 'Kyiv'):
                        print('Ticket sold successfully!')

                except SoldOutError as e:
                    print(f'Ticket for seat {i} is already sold: {e}')
                    print('Do you want to see available seats? (yes/no)')
                    choice = input().lower()
                    if choice == 'yes':
                        available_seats = []
                        for k in range(1, 3):
                            try:
                                tto.sell_ticket('LUX1', route1, '2023-04-20', j, k, f'Passenger_fuul_name {k}', 'Kharkiv', 'Kyiv')
                            except SoldOutError:
                                available_seats.append(k)
                        print(f'Available seats for carriage {j}: {available_seats}')
                    elif choice == 'no':
                        continue
                    else:
                        print('Invalid choice. Please enter yes or no.')

#Щойно ми продали усі місця на ці поїзди ,
# тому якщо зараз спробувати купити будь-яке місце на котромусь з цих поїздів,то виникне помилка.
try:
    if tto.sell_ticket('LUX1', route1, '2023-04-20', 1, 2, f'Passenger_fuul_name {1}', 'Kharkiv', 'Kyiv'):
        print('Ticket sold successfully!')

except SoldOutError as e:
    print(f'SoldOutError: {e}')


