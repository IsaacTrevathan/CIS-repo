# Isaac Trevathan
# 1955674

Services = {'Oil change': 35 , 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 'No service' }

print('Davy\'s auto shop services')
print('Oil change --', '${:.0f}'.format(Services['Oil change']))
print('Tire rotation --', '${:.0f}'.format(Services['Tire rotation']))
print('Car wash --', '${:.0f}'.format(Services['Car wash']))
print('Car wax --', '${:.0f}'.format(Services['Car wax']))

Choose_1 = input('\nSelect first service:')
Service_choice_1 = Services[Choose_1]
Choose_2 = input('\nSelect second service:')
Service_choice_2 = Services[Choose_2]

print('\n\nDavy\'s auto shop invoice')
if Service_choice_1 == 35:
    print('\nService 1: Oil change,','${:.0f}'.format(Services['Oil change']) )
elif Service_choice_1 == 19:
    print('\nService 1: Tire rotation,', '${:.0f}'.format(Services['Tire rotation']))
elif Service_choice_1 == 7:
    print('\nService 1: Car wash,', '${:.0f}'.format(Services['Car wash']))
elif Service_choice_1 == 12:
    print('\nService 1: Car wax,', '${:.0f}'.format(Services['Car wax']))
elif Service_choice_1 == 'No service':
    print('\nService 1: No service')


if Service_choice_2 == 35:
    print('Service 2: Oil change,','${:.0f}'.format(Services['Oil change']) )
elif Service_choice_2 == 19:
    print('Service 2: Tire rotation,', '${:.0f}'.format(Services['Tire rotation']))
elif Service_choice_2 == 7:
    print('Service 2: Car wash,', '${:.0f}'.format(Services['Car wash']))
elif Service_choice_2 == 12:
    print('Service 2: Car wax,', '${:.0f}'.format(Services['Car wax']))
elif Service_choice_2 == 'No service':
    print('Service 2: No service')

if Service_choice_1 == 'No service':
    Service_choice_1 = 0
if Service_choice_2 == 'No service':
    Service_choice_2 = 0

Total = Service_choice_1 + Service_choice_2
print('\nTotal: ${:.0f}'.format(Total))