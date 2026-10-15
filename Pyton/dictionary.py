cars = {
    "name": "Tesla",
    "color": ["black", "red", "green"],
    "price": 10000000.0,
    "energy": {100, 150, 300}
}

print(cars["name"])
print(cars["color"])
print(cars["price"])
print(cars["energy"])
print(type(cars))
print(len(cars))

x = dict(name = "John", age = 36, country = "Norway")
print(x)
print(dict(name = "BMW", color=["white", "orange"], price = 9000000000))
print(cars.get('color'))

x = tuple(cars.get("energy"))
cars.update({"energy": x})
print(cars)

cars['energy'] = tuple(cars["energy"])

print(cars)

cars = {
    "name": "Tesla",
    "color": ["black", "red", "green"],
    "price": 10000000.0,
    "energy": {100, 150, 300}
}

print(cars.keys())
