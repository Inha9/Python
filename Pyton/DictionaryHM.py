#robots = {
#    "name": "Tesla",
#    "color": ["black", "red", "green"],
#    "energy": {100, 150, 300}
#}
#
#robots.update({"amount":50000.0})
#print(robots)
# 
#x = type(int(robots.get("amount")))
#print(x)

human = {
    "name": "Toxir",
    "age": 25,
    "Father": {"name": "Teshaboy", "age" : 58, "car": True, "children" : 2, "work" : "yes"},
    "Mother": {"name": "Karomat", "age" : 50, "car": True, "children" : 2, "work" : "no"},
    "work_place": ["proramer", "buisnessmen", ""]
}

fruits = [
    {"name": "apple", "color": "red"},
    {"name": "peace", "color": "red"},
    {"name": "qivi", "color": "red"},
]
#print(fruits[1]['name'])
print(fruits[2].keys())
print(list(fruits[0].keys())[1])
print(fruits[2].values())
dict_2 = fruits.copy()
print(fruits)
print(dict_2)

print(fruits[0].items())
print(fruits[0].pop("color"))
print(fruits[0].popitem())
print(fruits[0])

