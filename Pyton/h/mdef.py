
#def sum_numbers(*args):
#    total = 0
#    for num in args:
#        total += num
#    return total
#
#result = sum_numbers(8, 2, 3, -1, 7)
#print(result)


#def count_letters(text):
#    upper_count = 0
#    lower_count = 0
#    for letter in text:
#        if letter.isupper():
#            upper_count += 1
#        elif letter.islower():
#            lower_count += 1
#    return upper_count, lower_count
#
#text = input("Введите текст: ")
#upper_count, lower_count = count_letters(text)
#print(f"Количество заглавных букв: {upper_count}")
#print(f"Количество строчных букв: {lower_count}")


#def get_toq_numbers(nums: list):
#    new_list = []
#    for i in nums:
#        if i % 2 != 0:
#          new_list.append(i)
#          print(new_list)
#
#get_toq_numbers([1,2,3,4,5,6,7,8,9])


def get_toq_numbers(nums: list):
    counter = 0
    for i in nums:
        if i % 2 == 0:
          counter += 1
    print(counter)

get_toq_numbers([1,2,3,4,5,6,7,8,9])


