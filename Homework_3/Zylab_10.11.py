# Isaac Trevathan
# 1955674

# creates a class called FoodItem
class FoodItem:

    # constructor that initializes name, fat, carbs and protein to their defaults
    def __init__(self, name='None', fat=0.0, carbs=0.0, protein=0.0):

        # instance attribute of name
        self.name = name

        # instance attribute of fat
        self.fat = fat

        # instance attribute of carbs
        self.carbs = carbs

        # instance attribute of protein
        self.protein = protein

    def get_calories(self, num_servings):
        # calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self):

        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))

        # prints 'Number of servings followed by a space', formats to 2 decimal points
        print('Number of calories for {:.2f}'.format(servings), end='')

        # prints 'serving(s)', calls get_calories function with servings amount as the argument,
        # formats to 2 decimal places
        print(' serving(s): {:.2f}'.format(self.get_calories(servings)))


if __name__ == "__main__":

    # creates and instance of FoodItem
    food_item = FoodItem()

    # gets name input
    my_name = input()

    # gets fat input
    my_fat = float(input())

    # get carbs input
    my_carbs = float(input())

    # get protein input
    my_protein = float(input())

    # get servings input
    servings = float(input())

    # calls the get calories function using servings as argument to calculate calories
    food_item.get_calories(servings)

    # prints the output by calling print_info function
    food_item.print_info()

    # prints empty line
    print()

    # creates another instance of FoodItem using user inputs as parameters
    food_item = FoodItem(my_name, my_fat, my_carbs, my_protein)

    # calls get_calories function using servings as an argument to calculate calories
    food_item.get_calories(servings)

    # prints output by calling print_info function
    food_item.print_info()
