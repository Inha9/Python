language = input("choose language")

if language == "Uzb":
    print("Assalom aleykunm")
elif language == "English":
    print("Hello")
elif language == "Russian":
    print("Privet")
else:
    ("choose Uzb/English/Russia")

from random import randint

a = randint(1, 50)
b = randint(1, 50)

c = int(input('{} + {} ='.format(a, b)))

if c == (a + b):
     print("Right")
else:
    print("wrong")

a = input("write number")
b = input("write number")

if a > b:
    print("a > b")
elif a == b:
    print("a == b")
else :
     print("a < b")

age = int(input("Enter your age: "))
if age >= 18: 
    print("You are eligible to vote")
else :
    print("You arent eligible to vote")


number = input("1 before 30 number enter: ")
if number.isdigit():
    number = int(number)
    if number > 0 and number < 30:
        remainder = number % 10
        letter = ''
        if number > 9 and number <20:
            letter = "on"
        elif number > 19 and number < 30:
            letter = "yigirma"

            if remainder == 1:
                letter += "bir"
            elif remainder == 2:
                letter += "ikki"
            elif remainder == 3:
             letter += "uch"
            elif remainder == 4:
             letter += "tort"
            elif remainder == 5:
             letter += "besh"
            elif remainder == 6:
             letter += "olti"
            elif remainder == 7:
             letter += "yetti"
            elif remainder == 8:
             letter += "sakkiz"
            elif remainder == 9:
             letter += "toqiz"
            elif remainder == 10:
             letter += "on"
             print(letter)


             put =   int(input("a:"))
rest =   int(input("b:"))
if   put > rest :
         print(put)
elif         rest > put:
    print(rest)
else:
     put, star = 0
     print(put, "," ,rest)
                
