import random

variant = [""]

print("")

variant = random.choice(variant)

while True:
    user_word = input("")
    if user_word == variant:
        print("WINNER")
        break
    else:
        print("WRONG")