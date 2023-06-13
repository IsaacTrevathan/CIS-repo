# Isaac Trevathan
# 1955674

# creates directory of services that can be chosen
Services = {'Oil change': 35 , 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 'No service' }

# outputs the shop services title
print('Davy\'s auto shop services')

# outputs the Oil change price
print('Oil change --', '${:.0f}'.format(Services['Oil change']))

# outputs the Tire rotation price
print('Tire rotation --', '${:.0f}'.format(Services['Tire rotation']))

# outputs the Car wash price
print('Car wash --', '${:.0f}'.format(Services['Car wash']))

# outputs the Car wax price
print('Car wax --', '${:.0f}'.format(Services['Car wax']))

# gets first choice input from user
Choose_1 = input('\nSelect first service:')

# sets first choice to the corresponding dictionary value
Service_choice_1 = Services[Choose_1]

# gets second choice input from user
Choose_2 = input('\nSelect second service:')

# sets second choice to the corresponding dictionary value
Service_choice_2 = Services[Choose_2]

# outputs the tile for the shop invoice
print('\n\nDavy\'s auto shop invoice')

# if statement for the value of Oil change choice. Prints out choice and value for the 1st service
if Service_choice_1 == 35:
    print('\nService 1: Oil change,','${:.0f}'.format(Services['Oil change']) )

# else if statement for the value of Tire rotation choice. Prints out choice and value for the 1st service
elif Service_choice_1 == 19:
    print('\nService 1: Tire rotation,', '${:.0f}'.format(Services['Tire rotation']))

# else if statement for the value of Car wash choice. Prints out choice and value for the 1st service
elif Service_choice_1 == 7:
    print('\nService 1: Car wash,', '${:.0f}'.format(Services['Car wash']))

# else if statement for the value of Car wax choice. Prints out choice and value for the 1st service
elif Service_choice_1 == 12:
    print('\nService 1: Car wax,', '${:.0f}'.format(Services['Car wax']))

# else if statement for the value of No service choice. Prints out choice and value for the 1st service
elif Service_choice_1 == 'No service':
    print('\nService 1: No service')

# if statement for the value of Oil change choice. Prints out choice and value for the 2nd service
if Service_choice_2 == 35:
    print('Service 2: Oil change,','${:.0f}'.format(Services['Oil change']) )

# else if statement for the value of Tire rotation choice. Prints out choice and value for the 2nd service
elif Service_choice_2 == 19:
    print('Service 2: Tire rotation,', '${:.0f}'.format(Services['Tire rotation']))

# else if statement for the value of Car wash choice. Prints out choice and value for the 2nd service
elif Service_choice_2 == 7:
    print('Service 2: Car wash,', '${:.0f}'.format(Services['Car wash']))

# else if statement for the value of Car wax choice. Prints out choice and value for the 2nd service
elif Service_choice_2 == 12:
    print('Service 2: Car wax,', '${:.0f}'.format(Services['Car wax']))

# else if statement for the value of No service choice. Prints out choice and value for the 2nd service
elif Service_choice_2 == 'No service':
    print('Service 2: No service')

# if statement for the No service choice. changes the output value to $0 for the 1st choice
if Service_choice_1 == 'No service':
    Service_choice_1 = 0

# if statement for the No service choice. changes the output value to $0 for the 2nd choice
if Service_choice_2 == 'No service':
    Service_choice_2 = 0

# adds the value of service choice 1 and service choice 2. Outputs the final total value
Total = Service_choice_1 + Service_choice_2
print('\nTotal: ${:.0f}'.format(Total))