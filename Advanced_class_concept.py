class BankAccount:

    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self._balance = balance  # Leading underscore signals a private variable

    # 1. Getter: Allows reading balance like a regular variable
    @property
    def balance(self):
        return self._balance

    # 2. Setter: Runs automatically whenever someone changes the balance
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print(f"Error: Balance cannot be negative! Rejected set to: {amount}")
            return
        self._balance = amount

    # 3. Custom Dunder Method: Controls string output when printing
    def __str__(self):
        return f"Account({self.owner}): ${self._balance:.2f}"


# --- Example Usage ---
if __name__ == "__main__":
    acc = BankAccount("Alice", 100.0)

    # Reading balance (calls the @property getter)
    print(f"Current balance: ${acc.balance}")

    # Updating balance with valid value (calls the @balance.setter)
    acc.balance = 250.0
    print(acc)

    # Trying to set an invalid negative value (triggers validation)
    acc.balance = -50.0

    # Balance remains safe
    print(acc)



#OUTPUT
'''
Current balance: $100.0
Account(Alice): $250.00
Error: Balance cannot be negative! Rejected set to: -50.0
Account(Alice): $250.00
'''
