from abc import ABC, abstractmethod
#interface for stratergy
class PaymentStratergy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

#credit card payment(cpp)
class CCP(PaymentStratergy):
    def pay(self, amount):
        print("Payment of ",amount," using your credit card was SUCCESSFULL!!")

#debit card payment(DCP)
class DCP(PaymentStratergy):
    def pay(self, amount):
        print("Payment of ",amount," using your debit card was SUCCESSFULL!!")

#UPI payment
class UPI(PaymentStratergy):
    def pay(self, amount):
        print("Payment of ",amount," using your UPI was SUCCESSFULL!!")

#net banking payment(NB)
class NB(PaymentStratergy):
    def pay(self, amount):
        print("Payment of ",amount," using your net banking was SUCCESSFULL!!")

#main class
class pay_process:
    def __init__(self, stratergy=None):
        self.stratergy=stratergy
    def set_stratergy(self, stratergy):
        self.stratergy=stratergy
    def process(self, amount):
        if self.stratergy==None:
            print("No payment method selected!!! Please select one")
        else:
            self.stratergy.pay(amount)
p=pay_process()
while True:
    print(''' ========== Welcome to the processing system ===========
    Choose your payment method:
    1. Credit Card
    2. Debit Card
    3. UPI
    4. Net Bankling
    5. Exit''')
    ch=int(input("Enter your choice: "))
    if ch==5:
        print("Thank you for using our services!!!")
        break
    if ch==1:
        amount=float(input("Enter your payable amount: "))
        p.set_stratergy(CCP())
    elif ch==2:
        amount=float(input("Enter your payable amount: "))
        p.set_stratergy(DCP())
    elif ch==3:
        amount=float(input("Enter your payable amount: "))
        p.set_stratergy(UPI())
    elif ch==4:
        amount=float(input("Enter your payable amount: "))
        p.set_stratergy(NB())
    else:
        print("Invalid choice!!!! Enter from above menu")
        continue
    p.process(amount)


#OUTPUT

'''
========== Welcome to the processing system ===========
    Choose your payment method:
    1. Credit Card
    2. Debit Card
    3. UPI
    4. Net Bankling
    5. Exit
Enter your choice: 1
Enter your payable amount: 1000
Payment of  1000.0  using your credit card was SUCCESSFULL!!
 ========== Welcome to the processing system ===========
    Choose your payment method:
    1. Credit Card
    2. Debit Card
    3. UPI
    4. Net Bankling
    5. Exit
Enter your choice: 2
Enter your payable amount: 1000 
Payment of  1000.0  using your debit card was SUCCESSFULL!!
 ========== Welcome to the processing system ===========
    Choose your payment method:
    1. Credit Card
    2. Debit Card
    3. UPI
    4. Net Bankling
    5. Exit
Enter your choice: 3
Enter your payable amount: 1000 
Payment of  1000.0  using your UPI was SUCCESSFULL!!
 ========== Welcome to the processing system ===========
    Choose your payment method:
    1. Credit Card
    2. Debit Card
    3. UPI
    4. Net Bankling
    5. Exit
Enter your choice: 4
Enter your payable amount: 1000 
Payment of  1000.0  using your net banking was SUCCESSFULL!!
 ========== Welcome to the processing system ===========
    Choose your payment method:
    1. Credit Card
    2. Debit Card
    3. UPI
    4. Net Bankling
    5. Exit
Enter your choice: 5
Thank you for using our services!!!

'''
