import gas_disk
import gas_core
import time
from gas_disk import load_inventory
def main():
    print('\n🌷WELCOME to Violet Flowers Gas StAtIoN!!🌷\n')
    print('\nLoading...\n')
    time.sleep(1)
    inventory = load_inventory()
    print(inventory)
    payment = input('\n💵pre_pay or pay_after?💵\n')
    if not (payment == 'pay_after' or payment == 'pre_pay'):
        print('Sorry I could not get that\n')
        exit()
    choice = input("What would you like for today? regular, mid-grade, or premium?\n")
    price = gas_core.price_of(inventory, choice)
    if payment == 'pay_after':
        gallons = float(input('\nHow many gallons did you pump?\n'))
        money = float(gallons) * float(price)
        print('\npumping....⛽\n')
        time.sleep(1.5)
        x = gas_disk.pay_after_msj(choice, gallons, money)
        print(x)
        # money = gas_core.pay_after(choice, gallons)

    elif payment == 'pre_pay':
        money = float(input('\nHow much would you like to pay?\n'))
        print('\npumping....⛽\n')
        time.sleep(1.5)
        gallons = money / price
        result = gas_disk.pre_pay_msj(choice, gallons, money)
        print(result)
    print('Thanks for stopping by, come back SOON!!') 
if __name__ == '__main__':
    main()
