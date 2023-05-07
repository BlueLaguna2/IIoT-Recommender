def CreateWarehouseClassFactory(bolPallet, bolProduct):
    print(' ')
    print('class Warehouse:')
    print('    def __init__(self, location):')
    print('         self.location = location')

    if bolProduct:
        print('         self.products = {}')

    if bolPallet:
        print('         self.pallets = {}')
    print(' ')

    if bolProduct:
        print('    def add_product(self, product_name, quantity):')
        print('         if product_name in self.products:')
        print('             self.products[product_name] += quantity')
        print('         else:')
        print('             self.products[product_name] = quantity')
        print(' ')
        print('    def remove_product(self, product_name, quantity):')
        print('         if product_name in self.products and self.products[product_name] >= quantity:')
        print('             self.products[product_name] -= quantity')
        print('         else:')
        print('             print("Error: Not enough product in stock")')
        print(' ')

    if bolPallet:
        print('    def add_pallet(self, pallet_id, product_name, quantity):')
        print('         if pallet_id not in self.pallets:')
        print('             self.pallets[pallet_id] = (product_name, quantity)')
        print('             self.add_product(product_name, quantity)')
        print('         else:')
        print('             print("Error: Pallet ID already exists")')
        print(' ')
        print('    def remove_pallet(self, pallet_id):')
        print('         if pallet_id in self.pallets:')
        print('             product_name, quantity = self.pallets[pallet_id]')
        print('             del self.pallets[pallet_id]')
        print('             self.remove_product(product_name, quantity)')
        print('         else:')
        print('             print("Error: Pallet ID does not exist")')
        print(' ')

    if bolProduct:
        print('    def check_stock(self, product_name):')
        print('         if product_name in self.products:')
        print('             return self.products[product_name]')
        print('          else:')
        print('              return 0')

if __name__ == '__main__':
    CreateWarehouseClassFactory(True, True)