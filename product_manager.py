class ProductManager:
    def __init__(self):
        self.products = {}

    def add_product(self, name, price):
        if name not in self.products:
            self.products[name] = {'price': price, 'quantity': 0}

    def display_products(self):
        print("Available Products:")
        for name, details in self.products.items():
            print(f"{name} - Price: ${details['price']}, Quantity: {details['quantity']}")
        print()
