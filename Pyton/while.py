#i = 8  #<= gacha
#while i < 39:
#  print(i)
#  i += 1


#i = 0
#while i <=10:
#   print("Hello world")

#while True:
#  print()

#i = 1
#while i < 100:
#    print(i)
#    if i == 50:
#        break
#    i += 1
    
#my_cars = ["BMW", "Tesla", "KIA", "Ravon", "Ferrari"]
#i = 0
#while i < len(my_cars):
#    if not my_cars[1] == "Ravon":
#        print(my_cars[i])
#        i += 1

#while i < len(my_cars):
#    if my_cars[i] != "Ravon":
#        print(my_cars[i])
#        i += 1
#    else:
#        i += 1
#        continue
#
#    odam = int(input("Son:"))

#i = 1
#total = 0
#user_number = int(input("ENter number"))
#while i <= user_number:
#        total += i
#        i += 1
#print(total)

    # 2
# question = input("Enter: ")
# ismlar = []
# while question.lower() != "stop":
#     question = input("ENter: ")
#     append(question)
#     if sorov.lower() == "stop":
#         ismlar.remove("stop")
#         print(*name)
#         break    

words = []
while True:
        user_word = input("Enter word: ")
        if user_word == "stop":
                  #if user_word == ["stop", "стоп", "toxta"]:
                break
        words.append(user_word)
        print(words)

# 3
# i = 0 
# while i < 100:
#     i = i + 1
#     if i % 2 == 0:
#       i = i + 1
#       print(i)
#     else:
#        i = i + 1
#        print(i)
#        continue

i = 0
while i <= 100:
        if i % 2 == 0:
                print(i)
                i += 1
    

# 4
# i = 0 
# while i < 99:
#     i = i + 1
#     if i % 2 > 0:
#       print(i)
#     else:
#        i = i + 1
#        print(i)
#        continue

i = 0
while i <= 100:
        if i % 2 != 0:
         print(i)
         i += 1

# 5
# i = 0 
# while i <= 99:
#    i = i + 1
#    if i % 3 == 0:
#       continue
#    else:
#       i = i + 1
#       print(i)

i = 1
if i % 3 != 0:
       print(i)
       i += 1