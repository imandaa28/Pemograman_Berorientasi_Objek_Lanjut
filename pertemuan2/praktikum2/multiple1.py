# Python program to demonstrate
# multiple inheritance
 
# Base class1
class Ibu:
    namaibu = ""
 
    def ibu(self):
        print(self.namaibu)
 
# Base class2
 
 
class Ayah:
    namaayah = ""
 
    def ayah(self):
        print(self.namaayah)
 
# Derived class
 
 
class Anak(Ibu, Ayah):
    def parents(self):
        print("Ayah :", self.namaayah)
        print("Ibu :", self.namaibu)
 
 
# Driver's code
s1 = Anak()
s1.namaayah = "Yogi"
s1.namaibu = "Iik"
s1.parents()