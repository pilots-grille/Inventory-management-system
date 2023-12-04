class TransactionManager:
    def __init__(self):
        self.transactions = []

    def sell_product(self, product_name, quantity):
        if product_name in product_manager.products and product_manager.products[product_name]['quantity'] >= quantity:
            product_manager.products[product_name]['quantity'] -= quantity
            transaction = {'product': product_name, 'quantity': quantity, 'amount': product_manager.products[product_name]['price'] * quantity}
            self.transactions.append(transaction)
            print(f"Sold {quantity} units of {product_name}.")
        else:
            print(f"Error: Insufficient stock of {product_name}.")

    def display_sales_report(self):
        total_sales = sum(transaction['amount'] for transaction in self.transactions)
        print("Sales Report:")
        for transaction in self.transactions:
            print(f"Product: {transaction['product']}, Quantity: {transaction['quantity']}, Amount: ${transaction['amount']}")
        print(f"Total Sales: ${total_sales}\n")
