from random import randint
cuisines = ['Indonesian', 'Turkish', 'Thai', 'Spanish', 'Moroccan', 'Japanese', 'Indian', 'Italian', 'French', 'Chinese']
value = randint(0, cuisines.__len__() - 1)
print(cuisines[value])