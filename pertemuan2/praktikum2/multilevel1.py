# Python program to demonstrate
# multilevel inheritance
 
# Base class
 
 
class Kakek:
 
    def __init__(self, namakakek):
        self.namakakek = namakakek
 
# Intermediate class
 
 
class   Ayah(Kakek):
    def __init__(self, namaayah, namakakek):
        self.namaayah = namaayah
 
        # invoking constructor of Grandfather class
        Kakek.__init__(self, namakakek)
 
# Derived class
 
 
class Anak(Ayah):
    def __init__(self, namaanak, namaayah, namakakek):
        self.namaanak = namaanak
 
        # invoking constructor of Father class
        Ayah.__init__(self, namaayah, namakakek)
 
    def print_nama(self):
        print('nama kakek :', self.namakakek)
        print("nama ayah :", self.namaayah)
        print("nama anak :", self.namaanak)
 
 
#  Driver code
s1 = Anak('Rama', 'Yusdit', 'Farhan')
print(s1.namakakek)
s1.print_nama()