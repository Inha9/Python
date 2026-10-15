#def myloop():
#    for i in range(1, 5):
#        print(i)

#myloop()
#myloop()
#myloop()

#for i in range(1, 4):
#    myloop()
#    print('*' * 30)

# def person(name, age):
#     print(name, age)

#def person(name, age):
#    if age >= 18:
#       print(f"{name} your age {age}")
#    else:
#        print(f"{name} wrong {age}")
#
#person('Kamron', 19)

#def get_number_list(num):
#  numbers = []
#  for i in range(1, num+1):
#    numbers.append(i)
#    print(tuple(numbers))
#
#    number = int(input("Son kiriting: "))
#
#    get_number_list(number)

#inp = input("Ism kiriting: ")
#age = input("ENTER YOUR AGE: ")
#text = f"Salom {inp}"
#text = "Hello {ag}.How old are you: {0}".format(inp, age)
#text = "Hello {1}.How old are you: {0}".format(inp, age)
#text = "Hello %s .How old are you: %s " % (inp, age)
#print(text)

#def students(name, age, coin)

#def teacher(*salom, result):
#    print(salom)
#    print(result)
#
#teacher("Jony", "Keyn", "Mia", 1, True, result = 9.5)

def teacher(price,**kwargs):
    print(kwargs)

teacher(500, leader1 = "Jony", leader2 = "Keyn", leader3 = "Mia")


