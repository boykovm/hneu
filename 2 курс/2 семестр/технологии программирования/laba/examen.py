from datetime import datetime, date, timedelta

class LivingPlace:
    n = 0

    def __init__(self, name = None, is_available = True):
        if not name:
            raise Exception('Name must be provided')
        self._id = self.__create_id()
        self._name = name
        self._is_available = is_available

    def __create_id(self):
        LivingPlace.n +=1
        return LivingPlace.n

    def __str__(self):
        return f'{self._name} is {"available" if self._is_available else "not available"}'

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def set_name(self, name = None):
        if not name:
            raise Exception('Name must be provided')
        self._name = name

    def is_available(self):
        return self._is_available

    def rent(self):
        self._is_available = False

    def set_available(self):
        self._is_available = True

class Orendodator:
    n = 0

    def __init__(self, name = None, places = []):
        if not name:
            raise Exception('Name must be provided')
        self._name = name
        self._id = self.__create_id()
        self._places = places

    def __create_id(self):
        Orendodator.n +=1
        return Orendodator.n

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_place_ids(self):
        ids = []
        for place in self._places:
            ids.append(place.get_id())

        return ids

    def get__available_places(self):
        places = []
        for place in self._places:
            if place.is_available:
                places.append(place.get_id())

        return places

    def add_living_place(self, living_place = None):
        if not living_place:
            raise Exception('living_place must be provided')
        self._places.append(living_place)

    def remove_place_by_id(self, id = None):
        if not id:
            raise Exception('id must be provided')
        idx = None
        for i in range(len(self._places)):
            if self._places[i].get_id() == id:
                idx = i
                break
        if not idx:
            raise Exception('It\'s not your place')
        del self._places[i]

    def __str__(self):
        return self._name

class Orendodavec:
    n = 0

    def __init__(self, name = None):
        if not name:
            raise Exception('Name must be provided')
        self._name = name
        self._id = self.__create_id()

    def __create_id(self):
        Orendodavec.n +=1
        return Orendodavec.n

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def __str__(self):
        return self._name

class RentAgreement:
    n = 0

    def __init__(self, orendodator = None, orendodavec = None, livingPlace = None, start_date = datetime.now(), end_date = datetime.now()):
        if not orendodator:
            raise Exception('Orendodator must be provided')

        if not orendodavec:
            raise Exception('Orendodavec must be provided')

        if not livingPlace:
            raise Exception('Living place must be provided')
        diff = end_date - start_date
        if diff.total_seconds() < 0:
            raise Exception('End date must after starting time')

        if not livingPlace.is_available():
            raise Exception('This living place is already rented')


        self._id = self.__create_id()
        self._orendodator = orendodator
        self._orendodavec = orendodavec
        self._livingPlace = livingPlace
        self._start_date = start_date
        self._end_date = end_date
        self._livingPlace.rent()

    def __create_id(self):
        RentAgreement.n +=1
        return RentAgreement.n

    def get_orendodator_id(self):
        return self._orendodator.get_id()

    def get_orendodavec_id(self):
        return self._orendodavec.get_id()

    def get_living_place_id(self):
        return self._livingPlace.get_id()

    def get_start_time(self):
        return self._start_date

    def get_end_time(self):
        return self._end_date


    def __str__(self):
        return f'Rent agreement between {self._orendodator.get_name()} and {self._orendodavec.get_name()}, place: {self._livingPlace.get_name()}'

# creating few living places
try:
    lp1 = LivingPlace()
except:
    print('we should provide name value')
lp2 = LivingPlace('2')
lp3 = LivingPlace('3')
lp4 = LivingPlace('4')
lp5 = LivingPlace('5')

# getters test
print(lp2.get_id())
print(lp2.get_name())
print(lp2)

#seters test
try:
    lp2.set_name()
except:
    print('name must be provided')

lp2.set_name('qwe')
print(lp2.get_name())

lp2.rent()
print(lp2.is_available())

lp2.set_available()
print(lp2.is_available())

#create few Orendodator
try:
    or_1 = Orendodator()
except:
    print('we should provide name of Orendodator')
or_2 = Orendodator('o1', [lp2])
or_3 = Orendodator('o2', [lp4, lp5])

#test geters
print(or_2.get_id())
print(or_2.get_name())
print(or_2.get_place_ids())
print(or_2.get__available_places())
print(or_2)

#seter tests
try:
    or_2.remove_place_by_id()
except:
    print('id must be provided')
try:
    or_2.remove_place_by_id(lp3.get_id())
except:
    print('it is not your place')

try:
    or_2.add_living_place()
except:
    print('Living place must be provided')
or_2.add_living_place(lp3)
print(or_2.get_place_ids())

or_2.remove_place_by_id(lp3.get_id())
print(or_2.get_place_ids())

or_2.add_living_place(lp3)
print(or_2.get_place_ids())

#create few Orendodavecs
try:
    oc_1 = Orendodavec()
except:
    print('we must provide name of orendodavec')
oc_2 = Orendodavec('o2')
oc_3 = Orendodavec('o3')
oc_4 = Orendodavec('o4')
oc_5 = Orendodavec('o5')

#test geters
print(oc_2.get_id())
print(oc_2.get_name())
print(oc_2)

#create few rent agreements
try:
    ra_1 = RentAgreement()
except:
    print('we should provide orendodator, Orendodavec and living place')

try:
    ra_1 = RentAgreement(or_2)
except:
    print('we should provide Orendodavec and living place')

try:
    ra_1 = RentAgreement(or_2, oc_2)
except:
    print('we should provide living place')
try:
    ra_1 = RentAgreement(or_2, oc_2, lp2, datetime(2023, 7, 7), datetime.now())
except:
    print('we should provide correct date')
ra_2 = RentAgreement(or_2, oc_2, lp2, datetime.now(), datetime(2023, 7, 7))
ra_3 = RentAgreement(or_2, oc_3, lp3, datetime(2023, 6, 7), datetime(2023, 7, 7))
ra_4 = RentAgreement(or_3, oc_4, lp4, datetime.now(), datetime(2023, 7, 7))

try:
    ra_5 = RentAgreement(or_3, oc_4, lp4, datetime.now(), datetime(2023, 7, 7))
except:
    print('living place is rented')

#geters test
print(ra_2.get_orendodator_id())
print(ra_2.get_orendodavec_id())
print(ra_2.get_living_place_id())
print(ra_2.get_start_time())
print(ra_2.get_end_time())
print(ra_2)





