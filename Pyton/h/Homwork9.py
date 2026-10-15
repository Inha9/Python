# 1
#Transports = ["BMW", "ferari", "Lamborgini"]
# print(cars[0],cars[-1])

# 2
# print(Transports[2],Transports[-1])

#  3
# Transports.append("Matiz")
# Transports.append("Kamaz")
# Transports.append("Tiko")
# print(*cars)

# 4
# Transports.remove("Malibu")
# print(*cars)

# 5
# Transports.insert(2, "BMW")
# print(cars)

# 6
#Transports.pop()
#print(Transports)

#7
#Transports.remove("Tiko")
#Transports.insert(5, "Lamborgini")
#print(Transports)

#Transports[-1] = "Lamborgini"
#print(Transports)

#8

#if Transports == "Cobalt":
#     print(Transports)
#elif Transports > "Cobalt":
#     pr
#elif Transports < "Cobalt":

cars = ["BMW", "ferari", "Lamborgini", ]
   
# cars = ['Malibu', "Spark", "Toyota", "Ferrari", "Cobalt"]
# print(cars[0])
# print(cars[-1])
# print(cars[1:4])

# cars.append("Tico")
# cars.append("Matiz")
# cars.append("Kamaz")
# print(cars)
# cars.remove("Malibu")
# cars.insert(1, "BMW")
# print(cars)

# last_car = cars.pop()
# print(cars)
# cars[-1] = "Lamborgini"
# print(cars)

# print(last_car)

cars = ['Malibu', "Spark", "Toyota", "Ferrari", "Cobalt"]
print("Cobalt" in cars)

trucks = []
trucks.append("MAN")
trucks.append("Isuzu")
trucks.append("Volvo")
print("Volvo" in trucks)
print(*cars + trucks)