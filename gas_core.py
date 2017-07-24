def cal_money(gallons, price):
    '''float, float -> float
    returns gallons * price
    >>> cal_money(1, 2.07)
    2.07
    >>> cal_money(20, 2.07) 
    41.4
    >>> cal_money(10, 2.07)
    20.7
    ''' 
    return gallons * price

def price_of(inventory, gas_name):
    ''' ([[str, float, float]], str) -> (float) 
    This function will get a string and it will 
    look in a txt file and pull out the price
    of that gas and return it
    '''
    for item in inventory:
        if gas_name.strip() == item[0].strip().lower():
            return float(item[1]) 