#!/usr/bin/env python3

# series 1

fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)
response1 = input("Please add another fruit to the list: ")
response1 = response1.capitalize()
fruits.append(response1)
print(fruits)
fruit_count = len(fruits)
response2 = input("Pick a number between 1 and {}: ".format(fruit_count))
num = int(response2)
y = num - 1
name_fruit = fruits[y]
print("{} is {}".format(num, name_fruit))
response3 = input("Add another fruit to the list: ")
fruits = [response3.capitalize()] + fruits
print(fruits)
response4 = input("Give me one more fruit: ")
fruits.insert(0, response4.capitalize())
print("The fruits that start with the letter P are:")
for p_fruit in fruits:
    if p_fruit[0] == 'P':
        print(p_fruit)