#Vehicle Showroom Management System

class Vehicle:
    def __init__(self, vehicle_number, brand, price):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.price = price
        self.category = self._categorize_vehicle()

    def _categorize_vehicle(self):
        # Vehicles priced at $50,000 or above are categorized as Luxury
        if self.price >= 50000:
            return "Luxury"
        return "Economy"

    def display_details(self):
        print(f"ID: {self.vehicle_number:<10} | Brand: {self.brand:<12} | "f"Price: ${self.price:<10,.2f} | Category: {self.category}")


class Showroom:
    def __init__(self, name):
        self.name = name
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"Added vehicle: {vehicle.brand} ({vehicle.vehicle_number})")

    def display_all_vehicles(self):
        print(f"\n{'=' * 15} {self.name} - Inventory {'=' * 15}")
        if not self.vehicles:
            print("No vehicles in inventory.")
            return

        for vehicle in self.vehicles:
            vehicle.display_details()


# Demonstration
if __name__ == "__main__":
    # Create Showroom Instance
    my_showroom = Showroom("Apex Auto Motors")

    # Create Vehicle Instances
    v1 = Vehicle("VH-101", "Toyota", 24500.00)
    v2 = Vehicle("VH-102", "BMW", 68000.00)
    v3 = Vehicle("VH-103", "Honda", 19500.00)
    v4 = Vehicle("VH-104", "Porsche", 115000.00)

    # Add Vehicles to Showroom
    print("--- Adding Vehicles to Inventory ---")
    my_showroom.add_vehicle(v1)
    my_showroom.add_vehicle(v2)
    my_showroom.add_vehicle(v3)
    my_showroom.add_vehicle(v4)

    # Display All Vehicles
    my_showroom.display_all_vehicles()



#OUTPUT

'''
--- Adding Vehicles to Inventory ---
Added vehicle: Toyota (VH-101)
Added vehicle: BMW (VH-102)
Added vehicle: Honda (VH-103)
Added vehicle: Porsche (VH-104)

=============== Apex Auto Motors - Inventory ===============
ID: VH-101     | Brand: Toyota       | Price: $24,500.00  | Category: Economy
ID: VH-102     | Brand: BMW          | Price: $68,000.00  | Category: Luxury
ID: VH-103     | Brand: Honda        | Price: $19,500.00  | Category: Economy
ID: VH-104     | Brand: Porsche      | Price: $115,000.00 | Category: Luxury
'''
