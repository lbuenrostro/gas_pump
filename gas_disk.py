def pre_pay_msj(type_of_gas, gallons, price):
    '''str, float, float -> None'''
    # message = type_of_gas + ", " + str(gallons) + ", " + str(price) + '\n'
    # with open('gas_log.txt', 'a') as file:
    #      file.write(message)
    return 'You bought {:0.2f} gallons of {} gas for ${:0.2f}.'.format(gallons, type_of_gas, price)

def pay_after_msj(type_of_gas, gallons, price):
    ''' str, float, float -> None'''
    return 'Total ${:0.2f} of {} gas for {}gallons.'.format(price, type_of_gas, gallons)

def update_inventory(type_of_gas, gallons, price):
    ''' str, float, float -> None
    ''' 
    message = type_of_gas + ', ' + str(gallons) + ', ' + str(price) + '\n'
    with open ('tank.txt', 'a') as file:
        file.write(message) 
    return None 


def update_inventory(type_of_gas, gallon):
    ''' str, float -> None
    ''' 
    message = type_of_gas + ', ' + str(gallons) + ', ' + str(price) + '\n'
    with open ('tank.txt', 'a') as file:
        file.write(message) 
    return None 

def load_inventory():
    with open('gas_price.txt', 'r') as file:
        file.readline()
        items = file.readlines()
    inventory = []
    for element in items:
        pieces = element.split(', ')
        inventory.append([pieces[0], float(pieces[1].strip()), float(pieces[2].strip())])
    return inventory

def convert_back(inventory):
    """[[string(item name), int(quantity)]] -> str"""
    new_inventory = ''
    for item in inventory:
        new_inventory += '\n' + str(item[0]) + ', ' + str(item[1]) + ', ' + str(item[2])
    return new_inventory

    with open('gas_price.txt', 'r') as file:
        gas_price_list = file.read()
        print(gas_price_list)



