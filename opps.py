class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
c1 = Car("Maruti", "Baleno")
c1.display()

#OUTPUT:
'''
Brand: Maruti
Model: Baleno
'''
