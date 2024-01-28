class Train:
    def __init__(self, train_number, route, date, carriages):
        self.train_number = train_number
        self.route = route
        self.date = date
        self.carriages = carriages


class Carriage:
    def __init__(self, carriage_number, number_of_seats):
        self.carriage_number = carriage_number
        self.number_of_seats = number_of_seats
        self.reserved_seats = []


class Stop:
    def __init__(self, station, arrival_time, departure_time):
        self.station = station
        self.arrival_time = arrival_time
        self.departure_time = departure_time


class Route:
    def __init__(self, route_number, start_station, end_station, stops):
        self.route_number = route_number
        self.start_station = start_station
        self.end_station = end_station
        self.stops = stops


class Ticket:
    id_counter = 1

    def __init__(self, train_number, route, date, carriage_number, seat_number, passenger_full_name,
                 departure_station, arrival_station):
        self._id = Ticket.id_counter
        Ticket.id_counter += 1
        self.train_number = train_number
        self.route = route
        self.date = date
        self.carriage_number = carriage_number
        self.seat_number = seat_number
        self.passenger_full_name = passenger_full_name
        self.departure_station = departure_station
        self.arrival_station = arrival_station


class SoldOutError(Exception):
    def __init__(self, message, available_seats=None):
        super().__init__(message)
        self.available_seats = available_seats


class TrainTicketOffice:
    def __init__(self):
        self.trains = []
        self.tickets_sold = []

    def add_train(self, train_number, route, date, carriages):
        self.trains.append(Train(train_number, route, date, [Carriage(cn, ns) for cn, ns in carriages]))

    def sell_ticket(self, train_number, route, date, carriage_number, seat_number, passenger_name, departure_station,
                    arrival_station):
        for train in self.trains:
            if train.train_number == train_number and train.route.route_number == route.route_number and train.date == date:
                for ticket in self.tickets_sold:
                    if ticket.train_number == train_number and ticket.carriage_number == carriage_number and ticket.seat_number == seat_number:
                        available_seats = [seat for carriage in train.carriages for seat in
                                           range(1, carriage.number_of_seats + 1) if not any(
                                t.train_number == train_number and t.carriage_number == carriage.carriage_number and t.seat_number == seat
                                for t in self.tickets_sold)]
                        raise SoldOutError('The seat is already sold. Please choose another one.', available_seats)

                for carriage in train.carriages:
                    if carriage.carriage_number == carriage_number and seat_number in range(1, carriage.number_of_seats + 1) and not any(
                            t.train_number == train_number and t.carriage_number == carriage_number and t.seat_number == seat_number
                            for t in self.tickets_sold):
                        self.tickets_sold.append(
                            Ticket(train_number, route, date, carriage_number, seat_number, passenger_name,
                                   departure_station, arrival_station))
                        carriage.reserved_seats.append(seat_number)
                        return True

                available_seats = [seat for carriage in train.carriages for seat in
                                   range(1, carriage.number_of_seats + 1) if
                                   carriage.carriage_number == carriage_number and not any(
                                       t.train_number == train_number and t.carriage_number == carriage_number and t.seat_number == seat
                                       for t in self.tickets_sold)]
                raise SoldOutError('The seat is not available. Please choose another one.', available_seats)

        available_seats = [seat for train in self.trains for carriage in train.carriages for seat in
                           range(1, carriage.number_of_seats + 1) if
                           train.train_number == train_number and carriage.carriage_number == carriage_number and not any(
                               t.train_number == train_number and t.carriage_number == carriage_number and t.seat_number == seat
                               for t in self.tickets_sold)]
        raise SoldOutError('No available seats on this train.', available_seats)


    # def sell_ticket(self, train_number, route, date, carriage_number, seat_number, passenger_name,
    #                 departure_station, arrival_station):
    #     for train in self.trains:
    #         if train.train_number == train_number and train.route.route_number == route.route_number and train.date == date:
    #             for ticket in self.tickets_sold:
    #                 if ticket.train_number == train_number and ticket.carriage_number == carriage_number and ticket.seat_number == seat_number:
    #                     available_seats = [seat for carriage in train.carriages for seat in
    #                                        range(1, carriage.number_of_seats + 1)
    #                                        if not any(
    #                             t.train_number == train_number and t.carriage_number == carriage.carriage_number and t.seat_number == seat
    #                             for t in self.tickets_sold)]
    #                     raise SoldOutError('The seat is already sold. Please choose another one.', available_seats)
    #             for carriage in train.carriages:
    #                 if carriage.carriage_number == carriage_number and seat_number in range(1,
    #                                                                                         carriage.number_of_seats + 1) and not any(
    #                         t.train_number == train_number and t.carriage_number == carriage_number and t.seat_number == seat_number
    #                         for t in self.tickets_sold):
    #                     self.tickets_sold.append(
    #                         Ticket(train_number, route, date, carriage_number, seat_number, passenger_name,
    #                                departure_station, arrival_station))
    #                     carriage.reserved_seats.append(seat_number)
    #                     return True
    #             available_seats = [seat for carriage in train.carriages for seat in
    #                                range(1, carriage.number_of_seats + 1)
    #                                if carriage.carriage_number == carriage_number and not any(
    #                     t.train_number == train_number and t.carriage_number == carriage_number and t.seat_number == seat
    #                     for t in self.tickets_sold)]
    #             raise SoldOutError('The seat is not available. Please choose another one.', available_seats)
    #     available_seats = [seat for train in self.trains for carriage in train.carriages for seat in
    #                        range(1, carriage.number_of_seats + 1)
    #                        if
    #                        train.train_number == train_number and carriage.carriage_number == carriage_number and not any(
    #                            t.train_number == train_number and t.carriage_number == carriage_number and t.seat_number == seat
    #                            for t in self.tickets_sold)]
    #     raise SoldOutError('No available seats on this train.', available_seats)








# class TrainTicketOffice:
#     def __init__(self):
#         self.trains = []
#         self.tickets_sold = []
#
#     def add_train(self, train_number, route, date, carriages):
#         self.trains.append(Train(train_number, route, date, carriages))
#
#     def sell_ticket(self, train_number, route, date, carriage_number, seat_number, passenger_name,
#                     departure_station, arrival_station):
#         for train in self.trains:
#             if train.train_number == train_number and train.route.route_number == route.route_number and train.date == date:
#                 for carriage in train.carriages:
#                     if carriage.carriage_number == carriage_number:
#                         # check if the seat is already sold
#                         for ticket in self.tickets_sold:
#                             if ticket.train_number == train_number and ticket.carriage_number == carriage_number and ticket.seat_number == seat_number:
#                                 free_seats = self._get_free_seats(train_number, carriage_number)
#                                 if free_seats:
#                                     message = f"The seat is already sold. Please choose another one. These seats are available: {free_seats}."
#                                     raise SoldOutError(message)
#                                 else:
#                                     raise SoldOutError('The seat is already sold and there are no available seats.')
#                         # add the new ticket to the list of sold tickets
#                         self.tickets_sold.append(
#                             Ticket(train_number, route, date, carriage_number, seat_number, passenger_name,
#                                    departure_station, arrival_station))
#                         return True
#                 break
#         return False
#
#     def _get_free_seats(self, train_number, carriage_number):
#         for train in self.trains:
#             if train.train_number == train_number:
#                 for carriage in train.carriages:
#                     if carriage.carriage_number == carriage_number:
#                         return [seat for seat in range(1, carriage.number_of_seats + 1) if seat not in [ticket.seat_number for ticket in self.tickets_sold if ticket.train_number == train_number and ticket.carriage_number == carriage_number]]
#         return None
