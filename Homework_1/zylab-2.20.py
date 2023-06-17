
# Isaac Trevathan
# 1955674


# prompts the user for amount of lemon juice
num_Lemon = float(input('Enter amount of lemon juice (in cups):'))


# prompts the user for amount of water
num_Water = float(input('\nEnter amount of water (in cups):'))


# prompts the user for amount of agave nectar
num_Agave = float(input('\nEnter amount of agave nectar (in cups):'))


# prompts the user for amount of servings the ingredients make
num_Servings = float(input('\nHow many servings does this make?'))


# prints Lemonade servings yield
print('\n\nLemonade ingredients - yields', '{:.2f}'.format(num_Servings), 'servings')


# prints amount of lemon juice cups
print('{:.2f}'.format(num_Lemon), 'cup(s) lemon juice')


# prints amount of water cups
print('{:.2f}'.format(num_Water), 'cup(s) water')


# prints amount of agave nectar cups
print('{:.2f}'.format(num_Agave), 'cup(s) agave nectar')


# prompts the user for amount of total servings wanted
num_Total_Servings = float(input('\nHow many servings would you like to make?'))


# prints the amount of total servings
print('\n\nLemonade ingredients - yields', '{:.2f}'.format(num_Total_Servings), 'servings')


# prints the amount of lemon juice cups for the total servings amount
print('{:.2f}'.format((num_Total_Servings/num_Servings) * num_Lemon), 'cup(s) lemon juice')


# prints the amount of water cups for the total servings amount
print('{:.2f}'.format((num_Total_Servings/num_Servings) * num_Water), 'cup(s) water')


# prints the amount of agave nectar cups for the total servings amount
print('{:.2f}'.format((num_Total_Servings/num_Servings) * num_Agave), 'cup(s) agave nectar')


# prints the amount of total servings
print('\nLemonade ingredients - yields', '{:.2f}'.format(num_Total_Servings), 'servings')


# prints the amount of lemon juice gallons for the total servings amount
print('{:.2f}'.format(((num_Total_Servings/num_Servings) * num_Lemon)/16), 'gallon(s) lemon juice')


# prints the amount of water gallons for the total servings amount
print('{:.2f}'.format(((num_Total_Servings/num_Servings) * num_Water)/16), 'gallon(s) water')


# prints the amount of agave nectar gallons for the total servings amount
print('{:.2f}'.format(((num_Total_Servings/num_Servings) * num_Agave)/16), 'gallon(s) agave nectar')
