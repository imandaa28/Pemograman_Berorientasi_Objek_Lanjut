# Base class
class Kendaraan:
    def Kendaraan_info(self):
        print('Kendaraan Motor')

# Child class
class Mobil(Kendaraan):
    def mobil_info(self):
        print('Kendaraan Mobil')

# Create object of Car
Mobil = Mobil()

# access Vehicle's info using car object
Mobil.Kendaraan_info()
Mobil.mobil_info()