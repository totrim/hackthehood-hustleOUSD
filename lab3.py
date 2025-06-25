#Task 1: working with strings
food = "pepperoni pizza"
print(food[:3])
print(food[-3:])
first_last = food[0] + food[-1]
print(first_last)
food_list = food.split()
print(food_list)
joined_food = ' ' .join(food_list)
print(joined_food)


# Task 2 working with list
number_list= [1, 23, 13, 5, 8]
number_list. append(789)
print(number_list)
number_list.insert(1, 8)
print(number_list)
number_list.pop()
print(number_list)
number_list.remove(number_list[1])
print(number_list)
print(number_list[:3])
print(number_list[-3:])

# Task 3: working witn dictionaries
books = {'Jeff Kinney': 'Diary of the Wimpy Kid',  'Suzanne Collins ': 'The hunger games', 'Theodor Geisel ': 'Cat in the hat','S. E. Hinton' :'The outsiders'}
print(books.keys())
print(books.values())
print(books.get('Jeff Kinney'))
(books.pop('Jeff Kinney'))
print(books)
del books['Suzanne Collins']
print(books)
