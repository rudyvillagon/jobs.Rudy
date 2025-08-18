#Extensión de comportamiento

#Una subclase puede combinar y extender el comportamiento de múltiples clases base.

class Motorcycle:
    def petroleum_energy(self):
        print("\n 🏍 Power of burning Gasoline")

class Bicycle:
    def mechanical_energy(self):
        print("\n 🚲 Pedal power \n")

class Moped(Motorcycle, Bicycle):
    pass


mp = Moped()
mp.petroleum_energy()
mp.mechanical_energy()