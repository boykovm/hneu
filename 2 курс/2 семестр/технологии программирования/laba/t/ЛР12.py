from typing import List


def sum_elements(numbers: List[int]) -> int:

    return sum(numbers)


class Train:
    id_counter = 1

    def __init__(self, destination: str, train_number: str, num_seats: tuple):
        self._id = Train.id_counter
        Train.id_counter += 1
        self.destination = destination
        self.train_number = train_number

        self.num_seats = num_seats

    @property
    def id(self):
        return self._id

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value: str):
        self._destination = value

    @property
    def train_number(self):
        return self._train_number

    @train_number.setter
    def train_number(self, value: str):
        self._train_number = value



    @property
    def num_seats(self):
        return self._num_seats

    @num_seats.setter
    def num_seats(self, value: tuple):
        self._num_seats = value

    def __str__(self):
        return f'Train ID: {self.id}, \n Destination: {self.destination}, Train Number: {self.train_number}, Number of Seats: {self.num_seats}'


class Stop:
    id_counter = 1

    def __init__(self, name: str, arrival_time: str, departure_time: str):
        self._id = Stop.id_counter
        Stop.id_counter += 1
        self.name = name
        self.arrival_time = arrival_time
        self.departure_time = departure_time

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def arrival_time(self):
        return self._arrival_time

    @arrival_time.setter
    def arrival_time(self, value: str):
        self._arrival_time = value

    @property
    def departure_time(self):
        return self._departure_time

    @departure_time.setter
    def departure_time(self, value: str):
        self._departure_time = value

    def __str__(self):
        return f'Stop ID: {self.id}, Name: {self.name}, Arrival Time: {self.arrival_time}, ' \
               f'Departure Time: {self.departure_time}'


class Route:
    id_counter = 1

    def __init__(self, departure_station: str, arrival_station: str, stops: List[Stop]):
        self._id = Route.id_counter
        Route.id_counter += 1
        self.departure_station = departure_station
        self.arrival_station = arrival_station
        self.stops = stops if stops is not None else []

    def add_stop(self, stop: Stop):

        self.stops.append(stop)

    @property
    def id(self):
        return self._id

    @property
    def departure_station(self):
        return self._departure_station

    @departure_station.setter
    def departure_station(self, value: str):
        self._departure_station = value

    @property
    def arrival_station(self):
        return self._arrival_station

    @arrival_station.setter
    def arrival_station(self, value: str):
        self._arrival_station = value

    @property
    def stops(self):
        return self._stops

    @stops.setter
    def stops(self, value: List[Stop]):
        self._stops = value

    def __str__(self):
        return f'Route ID: {self.id}, Departure Station: {self.departure_station}, Arrival Station: {self.arrival_station}, ' \
               f'Stops: {[str(stop) for stop in self.stops]}'


class Ticket:
    id_counter = 1

    def __init__(self, passenger_name: str, passenger_surname: str,
                 train: Train, route: Route, wagon_number: str,
                 seat_number: str):
        if int(seat_number) < 1:
            raise Exception('Seat number have to be a positive number')
        self._id = Ticket.id_counter
        Ticket.id_counter += 1
        self.passenger_name = passenger_name
        self.passenger_surname = passenger_surname
        self.train = train
        self.route = route
        self.wagon_number = wagon_number
        self.seat_number = seat_number

    @property
    def id(self):
        return self._id

    @property
    def passenger_name(self):
        return self._passenger_name

    @passenger_name.setter
    def passenger_name(self, value: str):
        self._passenger_name = value

    @property
    def passenger_surname(self):
        return self._passenger_surname

    @passenger_surname.setter
    def passenger_surname(self, value: str):
        self._passenger_surname = value

    @property
    def train(self):
        return self._train

    @train.setter
    def train(self, value: Train):
        self._train = value

    @property
    def route(self):
        return self._route

    @route.setter
    def route(self, value: Route):
        self._route = value

    @property
    def wagon_number(self):
        return self._wagon_number

    @wagon_number.setter
    def wagon_number(self, value: str):
        self._wagon_number = value

    @property
    def seat_number(self):
        return self._seat_number

    @seat_number.setter
    def seat_number(self, value: str):
        self._seat_number = value

    def __str__(self):
        return f'Ticket ID: {self.id}, Passenger Name and Surname: {self.passenger_name} {self.passenger_surname}, Train: {str(self.train)}, ' \
               f'Route: {str(self.route)}, Wagon Number: {self.wagon_number}, Seat Number: {self.seat_number}'

# Створення потягів
train1 = Train("Kyiv-Vinnitsa", "001", (5, 10, 15))
train2 = Train("Lviv-Kharkiv", "002", (8, 12, 16))

# Створення зупинок для потягів
stop1_train1 = Stop("Kyiv", "10:00", "10:20")
stop2_train1 = Stop("Bila Tserkva", "10:45", "11:00")
stop3_train1 = Stop("Vinnytsia", "13:00", "13:40")

stop1_train2 = Stop("Lviv", "12:30", "13:00")
stop2_train2 = Stop("Ternopil", "14:00", "14:50")
stop3_train2 = Stop("Ivano-Frankivsk", "16:30", "16:50")

# Створення маршруту для потягу 1
route_train1 = Route(train1, "Kyiv", [])
route_train1.add_stop(stop1_train1)
route_train1.add_stop(stop2_train1)
route_train1.add_stop(stop3_train1)

# Створення маршруту для потягу 2
route_train2 = Route(train2, "Lviv", [])
route_train2.add_stop(stop1_train2)
route_train2.add_stop(stop2_train2)
route_train2.add_stop(stop3_train2)

# Виведення списку зупинок для потягів
print("Stops for Train 1:")
for stop in route_train1.stops:
    print(stop)

print("Stops for Train 2:")
for stop in route_train2.stops:
    print(stop)

# Продаж квитка на потяг 1
ticket = Ticket( "John Smith", train1, "A5","2023-03-27","5","31")
try:
    ticket2 = Ticket( "John Smith", train1, "A5","2023-03-27","5","0")
except:
    print('Can\'t buy a ticket')

# Виведення квитка
print(ticket)
