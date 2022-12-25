class Location:
    def __init__(self, name, coordinates, description, index=0) -> None:
        self.name = name
        self.coordinates = coordinates
        self.description = description
        self.index = index

    def printInfo(self):
        print(
            f"\nName: {self.name}\nCoordinates:{self.coordinates}\nDescription: {self.description}")


class Place(Location):
    def __init__(self, name, coordinates, description, rating, whereIsIt, index=0) -> None:
        super().__init__(name, coordinates, description, index)
        self.whereIsIt = whereIsIt
        self.rating = rating

    def printInfo(self):
        print(
            f"\nName: {self.name}\nCoordinates:{self.coordinates}\nDescription: {self.description}\nWhereIsIt: {self.whereIsIt}\nPlace rating: {self.rating}")


class Region(Location):
    def __init__(self, name, coordinates, description, rating, Depend_city, area, index=0) -> None:
        super().__init__(name, coordinates, description, index)
        self.Depend_city = Depend_city  # Регіон якого міста
        self.rating = rating
        self.area = area

    def printInfo(self):
        print(
            f"\nName: {self.name}\nCoordinates:{self.coordinates}\nDescription: {self.description}\nWhich city region:{self.Depend_city}\nPlace rating: {self.rating}\nRegion area: {self.area}")


class City(Location):
    def __init__(self, country, humanity_capacity, name, coordinates, description, index=0) -> None:
        super().__init__(name, coordinates, description, index)
        self.country = country
        self.humanity_capacity = humanity_capacity

    def printInfo(self):
        print(
            f"\nName: {self.name}\nCoordinates:{self.coordinates}\nDescription: {self.description}\nCountry: {self.country}\nHumanity capacity: {self.humanity_capacity}\n")


class Megapolis(City):
    def __init__(self, AirPolution, NumOfMetro, country, humanity_capacity, name, coordinates, description,
             index=0) -> None:
        super().__init__(country, humanity_capacity, name, coordinates, description, index)
        self.NumOfMetro = NumOfMetro
        self.AirPolution = AirPolution

    def printInfo(self):
        print(
            f"\nName: {self.name}\nCoordinates:{self.coordinates}\nDescription: {self.description}\nCountry: {self.country}\nHumanity capacity: {self.humanity_capacity}\nNumber of metro station: {self.NumOfMetro}\nAir polution : {self.AirPolution}\n ")


loc1 = Location("Руднічок", "М.Макієвка", "Місце помсти", "10012")
loc1.printInfo()

plc1 = Place("Водоспад", "Житомир", "Найбільший водоспад району", 4.5, "500м. по руслу р. Тетерів")
plc1.printInfo()

reg1 = Region("київська область", "Територія радіусом 100км навколо м.Київ", "околиці міста Київ", 5, "Київ", 16534,
              10003)
reg1.printInfo()

city = City("Україна", 1000000, "Житомир", "-100,500", "Не дуже відоме але красиве місто", 10010)
city.printInfo()

megacity = Megapolis("high", 26, "Україна", 6000000, "Одеса", "400,260", "Чудове місто")
megacity.printInfo()