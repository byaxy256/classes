# Class for Product
class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        # Instance variables
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    # Method to display product details
    def display_product_info(self):
        print(f"Product: {self.product_name}, Price: {self.price}, Quantity in Stock: {self.quantity_in_stock}")
                                                             
# Class for ShoppingCart
class ShoppingCart:
    # Class variable to track total number of shopping carts created
    total_carts = 0

    def __init__(self):
        # Instance variable to store items in the cart
        self.items = []  # List of tuples (Product, quantity)
        ShoppingCart.total_carts += 1  # Increment total carts

    # Method to add a product to the cart
    def add_to_cart(self, product, quantity):
        if quantity <= product.quantity_in_stock:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity
            print(f"Added {quantity} of {product.product_name} to cart.")
        else:
            print(f"Not enough stock for {product.product_name}. Only {product.quantity_in_stock} available.")

    # Method to remove a product from the cart
    def remove_from_cart(self, product):
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)
                product.quantity_in_stock += item[1]  # Return the quantity to the stock
                print(f"Removed {item[1]} of {product.product_name} from cart.")
                return
        print(f"{product.product_name} not found in cart.")

    # Method to display all items in the cart
    def display_cart(self):
        if not self.items:
            print("The cart is empty.")
        else:
            print("Cart contents:")
            for product, quantity in self.items:
                print(f"{product.product_name}: {quantity} @ {product.price} each")

    # Method to calculate the total price of items in the cart
    def calculate_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total

# Instructions:
# 1. Create at least three Product objects with varying prices and quantities
product1 = Product("Laptop", 25000000, 5)
product2 = Product("Phone", 5000000, 10)
product3 = Product("Headphones", 100000, 20)

# 2. Create two separate ShoppingCart instances and perform a series of operations
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Adding items to cart1
cart1.add_to_cart(product1, 2)
cart1.add_to_cart(product2, 1)

# Adding items to cart2
cart2.add_to_cart(product3, 3)
cart2.add_to_cart(product2, 2)

# Displaying the contents of each cart
print("\nCart 1 Contents:")
cart1.display_cart()

print("\nCart 2 Contents:")
cart2.display_cart()

# Calculating and displaying the total amount for each cart
print(f"\nTotal for Cart 1: ${cart1.calculate_total()}")
print(f"Total for Cart 2: ${cart2.calculate_total()}")

# Removing items from carts and displaying updated contents
cart1.remove_from_cart(product1)
cart2.remove_from_cart(product3)

print("\nUpdated Cart 1 Contents:")
cart1.display_cart()

print("\nUpdated Cart 2 Contents:")
cart2.display_cart()

# Display total carts created
print(f"\nTotal number of shopping carts created: {ShoppingCart.total_carts}")
