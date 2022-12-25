class Detal:
    def __init__(self, name = ''):
        self.name = name
        self.work = False

    def do(self):
        self.work = not self.work
        print(f'{self.name} works: {self.work}')

    def isWorking(self):
        return self.work


class Mechanism(Detal):
    def __init__(self, name = ''):
        super().__init__(name)
        self.rotate = False

    def action(self):
        self.rotate = not self.rotate
        print(f'{self.name} rotate: {self.work}')

    def do(self):
        self.work = not self.work
        print(f'{self.name} works: {self.work}')
        self.action()


class Virib:
    def __init__(self, name = '', mechanisms = []):
        self.name = name
        self.work = False
        self.mechanisms = mechanisms

    def toggle(self):
        if not self.work:
            print(f'{self.name} starts work')
            for mechanism in self.mechanisms:
                mechanism.do()
            print(f'{self.name} is working')
        else:
            print(f'{self.name} stops')
            for mechanism in self.mechanisms:
                mechanism.do()
            print(f'{self.name} has been stopped')

class Vuzol(Virib):
    def __init__(self, name = '', mechanisms = [], safeMechanism = Mechanism()):
        super().__init__(name, mechanisms)
        self.safeMechanism = safeMechanism
        
    def toggle(self, number = 1):
        if number % 2 == 0:
            if not self.safeMechanism.isWorking():
                self.safeMechanism.do()
            print(f'{self.name} starts work')
            for mechanism in self.mechanisms:
                mechanism.do()
            print(f'{self.name} is working')
        else:
            print('not safe')



d1 = Detal('detal 1')
d2 = Detal('detal 2')
d3 = Detal('detal 3')

m1 = Mechanism('mechanism 1')
m2 = Mechanism('mechanism 1')
m3 = Mechanism('mechanism 3')

virib1 = Virib('Virib 1', [d1, m1])
virib2= Virib('Virib 2', [d2, m2])

safeMechanism =  Mechanism('Safe mechanism')

vuzol1 = Vuzol('Vuzol 1', [d3, m3], safeMechanism)

print('===detal===')
d1.do()
print(d1.isWorking())
d1.do()
print(d1.isWorking())
print('===detal===')
print()

print('===mechanism===')
m1.do()
print(m1.isWorking())
m1.do()
print(m1.isWorking())
m1.action()
m1.action()
print('===mechanism===')
print()

print('===virib===')
virib2.toggle()
virib2.toggle()
print('===virib===')
print()

print('===vuzol===')
vuzol1.toggle(9)
vuzol1.toggle(10)
vuzol1.toggle(10)
print('===vuzol===')
print()
