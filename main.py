# my_name = 'person'

# def say_my_name(name):
#   print(name)
#   return name

# say_my_name(my_name)

# my_numbers = [1,2,3]

# def say_my_numbers(numbers):
#   print(numbers)
#   return(numbers)

# say_my_numbers(my_numbers)

# my_list = [1,2,3,4]

# def say_my_list(list):
#   for number in list:
#     print(number)
#   return list

# say_my_list(my_list)

# def redundant():
#   print(say_my_list(my_list))

# redundant()

def mapping(item):
  print(item + 2)

list = map(mapping, [1,2,3,4])

next(list)
next(list)
next(list)
