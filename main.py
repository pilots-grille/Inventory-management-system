from product_manager import ProductManager
from transaction_manager import TransactionManager

def main():
    # Initialize product and transaction managers
    product_manager = ProductManager()
    transaction_manager = TransactionManager()

    # Add products
    product_manager.add_product("Laptop", 1000)
    product_manager.add_product("Smartphone", 500)
    product_manager.add_product("Headphones", 50)

    # Display available products
    product_manager.display_products()

    # Perform transactions
    transaction_manager.sell_product("Laptop", 2)
    transaction_manager.sell_product("Smartphone", 3)

    # Display sales report
    transaction_manager.display_sales_report()

if __name__ == "__main__":
    main()
