def CreateWarehouseClassFactory(bolPallet, bolProduct,WHname):

    print(' ')
    with open(WHname + "_WarehouseClass.py", "w") as f:
        f.write("class Warehouse:" + "\n")
        f.write("    def __init__(self, location):" + "\n")
        f.write("         self.location = location" + "\n")

        if bolProduct:
            f.write("         self.products = {}" + "\n")

        if bolPallet:
            f.write("         self.pallets = {}" + "\n")
        f.write(" " + "\n")

        if bolProduct:
            f.write("    def add_product(self, product_name, quantity):" + "\n")
            f.write("         if product_name in self.products:" + "\n")
            f.write("             self.products[product_name] += quantity" + "\n")
            f.write("         else:" + "\n")
            f.write("             self.products[product_name] = quantity" + "\n")
            f.write(" " + "\n")
            f.write("    def remove_product(self, product_name, quantity):" + "\n")
            f.write("         if product_name in self.products and self.products[product_name] >= quantity:" + "\n")
            f.write("             self.products[product_name] -= quantity" + "\n")
            f.write("         else:" + "\n")
            f.write("             print('Error: Not enough product in stock')" + "\n")
            f.write(" " + "\n")

        if bolPallet:
            f.write("    def add_pallet(self, pallet_id, product_name, quantity):" + "\n")
            f.write("         if pallet_id not in self.pallets:" + "\n")
            f.write("             self.pallets[pallet_id] = (product_name, quantity)" + "\n")
            f.write("             self.add_product(product_name, quantity)" + "\n")
            f.write("         else:" + "\n")
            f.write("             print('Error: Pallet ID already exists') " + "\n")
            f.write(" " + "\n")
            f.write("    def remove_pallet(self, pallet_id):" + "\n")
            f.write("         if pallet_id in self.pallets:" + "\n")
            f.write("             product_name, quantity = self.pallets[pallet_id]" + "\n")
            f.write("             del self.pallets[pallet_id]" + "\n")
            f.write("             self.remove_product(product_name, quantity)" + "\n")
            f.write("         else:" + "\n")
            f.write("             print('Error: Pallet ID does not exist')" + "\n")
            f.write(" " + "\n")

        if bolProduct:
            f.write("    def check_stock(self, product_name):" + "\n")
            f.write("         if product_name in self.products:" + "\n")
            f.write("             return self.products[product_name]" + "\n")
            f.write("          else:" + "\n")
            f.write("              return 0" + "\n")

if __name__ == '__main__':
    CreateWarehouseClassFactory(True, True," ")