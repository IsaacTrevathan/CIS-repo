
# Isaac Trevathan
# 1955674

# imports math module
import math

# prompts user for all height
wall_height = float(input('Enter wall height (feet):'))

# prompts user for all width
wall_width = float(input('\nEnter wall width (feet):'))

# calculates wall area
area = (wall_height * wall_width)

# prints wall area
print('\nWall area:','{:.0f}'.format(area), 'square feet')

# calculates paint gallons
paint_gallons = (((wall_height * wall_width)/350))

# converts paint cans to paint gallons
paint_cans = int(math.ceil(paint_gallons))

# prints paint needed in gallons
print('Paint needed:', '{:.2f}'.format(paint_gallons) , 'gallons')

# prints cans needed
print('Cans needed:', paint_cans, 'can(s)')

# initializes dictionary for paint colors an prices
color = {'red': 35, 'green': 23, 'blue': 25}

# takes user input on which color
choose_color = input('\nChoose a color to paint the wall:')

# sets paint_cost to price value of user's color choice
paint_cost = color[choose_color]

# calculates the total cost of the paint
total_cost = paint_cost * paint_cans

# prints the final cost of the paint of the users color choice
print('\nCost of purchasing', choose_color, 'paint:', '${:.0f}'.format(total_cost))



