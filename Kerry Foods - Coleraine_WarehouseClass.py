class Warehouse:
    def __init__(self, location):
         self.location = location
         self.products = {}
         self.pallets = {}
 
    def add_product(self, product_name, quantity):
         if product_name in self.products:
             self.products[product_name] += quantity
         else:
             self.products[product_name] = quantity
 
    def remove_product(self, product_name, quantity):
         if product_name in self.products and self.products[product_name] >= quantity:
             self.products[product_name] -= quantity
         else:
             print('Error: Not enough product in stock')
 
    def add_pallet(self, pallet_id, product_name, quantity):
         if pallet_id not in self.pallets:
             self.pallets[pallet_id] = (product_name, quantity)
             self.add_product(product_name, quantity)
         else:
             print('Error: Pallet ID already exists') 
 
    def remove_pallet(self, pallet_id):
         if pallet_id in self.pallets:
             product_name, quantity = self.pallets[pallet_id]
             del self.pallets[pallet_id]
             self.remove_product(product_name, quantity)
         else:
             print('Error: Pallet ID does not exist')
 
    def check_stock(self, product_name):
         if product_name in self.products:
               return self.products[product_name]
         else:
              return 0
