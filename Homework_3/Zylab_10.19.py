# Isaac Trevathan
# 1955674

class ItemToPurchase:

    # constructor for ItemToPurchase with parameters item_price, item_quantity, item_ name and item_description
    def __init__(self, item_name='none', item_price=0.0, item_quantity=0.0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    # function that has parameters input_cost and input_quantity
    # gets the product of the two and returns the product
    def print_item_cost(self):
        # sets total to the product of item_price and item_quantity
        total = float(self.item_price * self.item_quantity)

        # prints item_name, item_quantity item_price and the total
        print(self.item_name, '{:.0f}'.format(self.item_quantity), '@', '${:.0f}'.format(float(self.item_price)),
              '=', '${:.0f}'.format(float(total)))

    # function that prints the item name and description
    def print_item_description(self, item_to_purchase):
        print(f'{self.item_name}:', item_to_purchase)


class ShoppingCart:

    # constructor for class shopping cart with parameters customer_name,current date, cart items
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=None):

        # makes an empty list if cart items is empty
        if cart_items is None:
            cart_items = []

        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    # function to add an item to the cart_items list
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    # function to remove an item from the cart_items list
    def remove_item(self, remove_item):
        found = 0

        # checks for wanted item in cart_items list and removes it if found
        for item in self.cart_items:

            if remove_item == item.item_name:
                self.cart_items.remove(item)
                found = 1
                break
        # if item is not found, prints item not found in cart
        if found == 0:
            print()
            print('Item not found in cart. Nothing removed.')
        else:
            print()

    # function to find item in cart_items list and change the quantity
    def modify_item(self, item_to_purchase, quantity):
        found = 0
        for item in self.cart_items:
            if item_to_purchase == item.item_name:
                item.item_quantity = float(quantity)
                found = 1

        # if item not found, prints that the item was not found in the cart_list
        if found == 0:
            print('Item not found in cart. Nothing modified.')

    # function that adds the quantity of all items in cart_list, returns the sum
    def get_num_items_in_cart(self):

        item_quantity_total_sum = 0
        for item in self.cart_items:
            item_quantity_total_sum += item.item_quantity
        return item_quantity_total_sum

    # function that adds the total costs of all of the items in cart_list and returns total
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    # function that prints the total price of the shopping cart, calls the print_item_cost function
    def print_total(self):
        found = 0
        for item in self.cart_items:

            item.print_item_cost()
            found = 1

        # prints that the shopping cart is empty of there are no items in cart_list
        if found == 0:
            print('SHOPPING CART IS EMPTY')

        print()
        print('Total:', '${:.0f}'.format(self.get_cost_of_cart()))

    # function that prints the descriptions of all items in cart_list, calls the print_item_description function
    def print_descriptions(self):
        for item in self.cart_items:
            item.print_item_description(item.item_description)


if __name__ == "__main__":
    # creates an empty list called my_cart_items
    my_cart_items = []

    # creates new instance of ItemToPurchase
    item_purchase = ItemToPurchase()

    # sets cart_items equal to my_cart_items
    item_purchase.cart_items = my_cart_items

    # creates instance of ShoppingCart
    my_shopping_cart = ShoppingCart()

    # gets name input from user
    my_customer_name = input('Enter customer\'s name:')
    print()

    # sets customer_name equal to my_customer_name
    my_shopping_cart.customer_name = my_customer_name

    # gets input for date from user
    my_date = input('Enter today\'s date:')
    print()

    # sets current_date equal to my_date
    my_shopping_cart.current_date = my_date
    print()

    # prints customer name and date
    print('Customer name:', my_customer_name)
    print('Today\'s date:', my_date)

    # sets choice equal to '0'
    choice = '0'
    print()

    # prints out the shopping cart menu
    print('MENU')
    print('a - Add item to cart')
    print('r - Remove item from cart')
    print('c - Change item quantity')
    print('i - Output items\' descriptions')
    print('o - Output shopping cart')
    print('q - Quit')

    # checks if input is equal to 'q'
    while choice != 'q':
        print()

        # gets choice input from user
        choice = input('Choose an option:')

        # checks if user input equals 'a'
        if choice == 'a':
            print()

            # prints Add item title
            print('ADD ITEM TO CART')

            # creates second instance of ItemToPurchase
            item_purchase_2 = ItemToPurchase()

            # gets input for item name
            my_name = input('Enter the item name:')
            print()

            # sets item_name equal to my_name
            item_purchase_2.item_name = my_name

            # gets item description from user
            description = input('Enter the item description:')
            print()

            # sets item_description equal to description
            item_purchase_2.item_description = description

            # gets price from user
            my_price = float(input('Enter the item price:'))
            print()

            # sets item_price equal to my_price
            item_purchase_2.item_price = my_price

            # gets quantity from user
            my_quantity = int(input('Enter the item quantity:'))
            print()

            # sets item_quantity equal to my_quantity
            item_purchase_2.item_quantity = my_quantity

            # calls the add_item function
            my_shopping_cart.add_item(item_purchase_2)
            print()

            # outputs the menu choices
            print('MENU')
            print('a - Add item to cart')
            print('r - Remove item from cart')
            print('c - Change item quantity')
            print('i - Output items\' descriptions')
            print('o - Output shopping cart')
            print('q - Quit')

        # checks if user choice equals 'r'
        elif choice == 'r':
            print()

            # prints remove item title
            print('REMOVE ITEM FROM CART')

            # gets input for item to be removed
            remove_this = input('Enter name of item to remove:')

            # calls the remove_item function
            my_shopping_cart.remove_item(remove_this)
            print()

            # outputs menu choices
            print('MENU')
            print('a - Add item to cart')
            print('r - Remove item from cart')
            print('c - Change item quantity')
            print('i - Output items\' descriptions')
            print('o - Output shopping cart')
            print('q - Quit')

        # checks if user choice equals 'c'
        elif choice == 'c':
            print()

            # prints title for change item
            print('CHANGE ITEM QUANTITY')

            # gets user input for item name to change
            my_item_name = input('Enter the item name:')
            print()

            # gets user input for new item quantity
            change_quantity = input('Enter the new quantity:')
            print()

            # calls the modify_item function
            my_shopping_cart.modify_item(my_item_name, change_quantity)
            print()

            # outputs menu choices
            print('MENU')
            print('a - Add item to cart')
            print('r - Remove item from cart')
            print('c - Change item quantity')
            print('i - Output items\' descriptions')
            print('o - Output shopping cart')
            print('q - Quit')

        # checks if user input equals 'i'
        elif choice == 'i':
            print()

            # output item descriptions title
            print('OUTPUT ITEMS\' DESCRIPTIONS')

            # prints customer name and date
            print(f'{my_customer_name}\'s Shopping Cart -', my_date)
            print()

            # prints item descriptions
            print('Item Descriptions')

            # calls print_descriptions function
            my_shopping_cart.print_descriptions()
            print()

            # prints menu choices
            print('MENU')
            print('a - Add item to cart')
            print('r - Remove item from cart')
            print('c - Change item quantity')
            print('i - Output items\' descriptions')
            print('o - Output shopping cart')
            print('q - Quit')

        # checks if user choice equals 'o'
        elif choice == 'o':
            print()

            # prints output shopping cart tile
            print('OUTPUT SHOPPING CART')

            # prints customer name and date
            print(f'{my_customer_name}\'s Shopping Cart -', my_date)

            # prints out the number of items in cart, calls get_num_items_in_cart function
            print('Number of Items:', '{:.0f}'.format(my_shopping_cart.get_num_items_in_cart()))
            print()

            # calls print total function
            my_shopping_cart.print_total()

            print()

            # prints menu choices
            print('MENU')
            print('a - Add item to cart')
            print('r - Remove item from cart')
            print('c - Change item quantity')
            print('i - Output items\' descriptions')
            print('o - Output shopping cart')
            print('q - Quit')
    print()
