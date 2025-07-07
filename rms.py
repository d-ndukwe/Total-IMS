# Task: Build a "Refinery Management System" for the oil company.

# Requirements:

# Class: Refinery

class Refinery: # create class
    def __init__(self, capacity): # define function
        self.__capacity = capacity
        self.__current_oil = 0

    def receive_oil(self, amount):
        if 0 < amount <= (self.__capacity - self.__current_oil):
            self.__current_oil += amount
            print(f"Received {amount} barrels of oil. Current storage: {self.__current_oil} barrels.")
        else:
            print("Invalid amount requested")

    def refine_oil(self, amount):
        if 0 < amount <= self.__current_oil:
            self.__current_oil -= amount
            print(f"Amount of oil refined: {amount}. Remaining oil stored: {self.__current_oil} barrels.")
        else:
            print("Invalid amount")

    def get_storage_status(self):
        return f"Current storage: {self.__current_oil} / {self.__capacity} barrels."
    
    # testing
refinery = Refinery(10000)
refinery.receive_oil(5000)
refinery.receive_oil(6000)
        
# Private attributes:
# __capacity (maximum barrels the refinery can process)
# __current_oil (amount of oil currently stored)
# Methods:
# receive_oil(amount) — Adds oil to the refinery’s storage if it doesn’t exceed capacity.
# refine_oil(amount) — Processes a given amount of oil if available. Reduces stored oil and shows how many barrels were refined.
# get_storage_status() — Returns the current amount of oil in storage.

# class Product:
#     def __init__(self,product_type):
#         self.__type = product_type
#         self.__quantity = 0



# Class: Product
# Private attributes:
# __type (like gasoline, diesel, jet fuel)
# __quantity (barrels produced)
# Methods:
# add_product(amount) — Increases product quantity.
# get_product_info() — Shows product type and available quantity.
# Simulate the system:

# Create a Refinery instance with a capacity of 10,000 barrels.
# Receive 5,000 barrels of crude oil.
# Refine 3,000 barrels into gasoline.
# Create a Product instance for gasoline and update its quantity.
# Show the refinery’s storage status and gasoline product info.