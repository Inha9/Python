
#Adress = ("Toshkent")
#Manzil = ["Toshkent"]
#print(Adress.__sizeof__())
#print(type(Adress))
#vegatebles = ("carrot", "onions")
#fruits = "Apple", "granata"
#
#Adress = ("Toshkent",("Andijon",("Namangan", "Chortoq", ""),"Fergana"),"Xiva")
#
#Name = {"Jahongir", "Shaxboz", "Eldor"}
#print(len(Name))

#Surname = {"Sobirjonov", "Tursunov", "Qahhorov"}
#print(Surname)
#Surname.add("Gayratxujaev")
#print(Surname)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

Classmets = {"Jahongir", "Shaxboz", "Aziz", "Farrux", "Kamron"}
print(len(Classmets))
print("Jahongir" in Classmets)
Classmets.add("Jamshidni")
Classmets.add("Abdurahimni")

Classmets = {"Jahongir", "Shaxboz", "Aziz", "Farrux", "Kamron"}
tanishla = {"Jahongir", "Shaxboz", "Aziz", "Farrux", "Kamron"}
Classmets.update(tanishla)

