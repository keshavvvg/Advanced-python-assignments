# 1. Define distinct strategies as standard functions
def flat_discount(price):
    return price - 20.0  # $20 off

def percentage_discount(price):
    return price * 0.80  # 20% off

def no_discount(price):
    return price  # Full price

# 2. Context class that accepts any strategy function
class ShoppingCart:
    def __init__(self, price, discount_strategy):
        self.price = price
        self.discount_strategy = (discount_strategy)# Holds the chosen strategy

    def calculate_total(self):
        # Executes whichever strategy was passed in
        return self.discount_strategy(self.price)

# 3. Usage
if __name__ == "__main__":
    original_price = 100.0

    # Apply $20 off strategy
    cart1 = ShoppingCart(original_price, flat_discount)
    print(f"Flat Discount Total: ${cart1.calculate_total():.2f}")  # $80.00

    # Apply 20% off strategy
    cart2 = ShoppingCart(original_price, percentage_discount)
    print(f"Percentage Discount Total: ${cart2.calculate_total():.2f}")  # $80.00

    # Apply no discount strategy
    cart3 = ShoppingCart(original_price, no_discount)
    print(f"Regular Total: ${cart3.calculate_total():.2f}")  # $100.00




#OUTPUT

'''
Flat Discount Total: $80.00
Percentage Discount Total: $80.00
Regular Total: $100.00
'''
