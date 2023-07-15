# Isaac Trevathan
# 1955674

class ItemToPurchase:

    # constructor with parameters item_name, item_price and item_quantity
    def __init__(self, item_name='none', item_price=0.0, item_quantity=0.0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    # function that has parameters input_cost and input_quantity
    # gets the product of the two and returns the product
    def print_item_cost(self):

        # sets total to the product of item_price and item_quantity
        total = float(self.item_price * self.item_quantity)

        # prints item_name, item_quantity item_price and the total
        print(self.item_name, self.item_quantity, '@', '${:.0f}'.format(float(self.item_price)),
              '=', '${:.0f}'.format(float(total)))


if __name__ == "__main__":

    # creates an instance of ItemToPurchase
    item_purchase = ItemToPurchase()

    # prints Item 1
    print('Item 1')

    # gets the 1st item name
    my_name = input('Enter the item name:')
    print()

    # sets item_name to my_name
    item_purchase.item_name = my_name

    # gets the 1st item price
    my_price = float(input('Enter the item price:'))
    print()

    # sets item_price to my_price
    item_purchase.item_price = my_price

    # gets the 1st item quantity
    my_quantity = int(input('Enter the item quantity:'))
    print()
    print()

    # sets item_quantity to my_quantity
    item_purchase.item_quantity = my_quantity

    # creates a second instance of item to purchase
    item_purchase_2 = ItemToPurchase()

    # prints Item 2
    print('Item 2')

    # gets the 2nd item name
    my_name_2 = input('Enter the item name:')
    print()

    # sets item_name to my_name_2
    item_purchase_2.item_name = my_name_2

    # gets the 2nd item price
    my_price_2 = float(input('Enter the item price:'))

    print()

    # sets item_price to my_price_2
    item_purchase_2.item_price = my_price_2

    # gets the 2nd item quantity
    my_quantity_2 = int(input('Enter the item quantity:'))
    print()

    # sets item_quantity to my_quantity_2
    item_purchase_2.item_quantity = my_quantity_2
    print()

    # prints TOTAL COST and calls the print_item_cost for both instances of ItemToPurchase
    print('TOTAL COST')
    item_purchase.print_item_cost()
    item_purchase_2.print_item_cost()
    print()

    # adds the total for the 1st item and the 2nd item together and prints it out
    print('Total:', '${:.0f}'.format((my_price * my_quantity) + (my_price_2 * my_quantity_2)))
