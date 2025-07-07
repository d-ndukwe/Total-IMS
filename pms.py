class OilField:
    def __init__(self, name, capacity):
        self.name = name
        self.__capacity = capacity  # Private attribute
        self.__extracted = 0

    def extract_oil(self, amount):
        if 0 < amount <= (self.__capacity - self.__extracted):
            self.__extracted += amount
            print(f"Extracted {amount} barrels from {self.name}.")
        else:
            print("Extraction amount exceeds capacity or is invalid.")

    def get_available_oil(self):
        return self.__extracted

class Pipeline:
    def __init__(self, capacity):
        self.__capacity = capacity  # Private attribute
        self.__current_load = 0

    def transport_oil(self, amount):
        if 0 < amount <= self.__capacity:
            self.__current_load = amount
            print(f"Transporting {amount} barrels through the pipeline.")
        else:
            print("Transport amount exceeds pipeline capacity or is invalid.")

    def clear_pipeline(self):
        print(f"Clearing {self.__current_load} barrels from the pipeline.")
        self.__current_load = 0

class Station:
    def __init__(self, name):
        self.name = name
        self.__storage = 0

    def receive_oil(self, amount):
        self.__storage += amount
        print(f"{amount} barrels received at {self.name} station.")

    def get_storage_status(self):
        return self.__storage

# Simulating the system
field = OilField("Alpha Field", 10000)
pipeline = Pipeline(5000)
station = Station("Delta Station")

field.extract_oil(3000)
pipeline.transport_oil(3000)
station.receive_oil(3000)

print(f"Oil available at field: {field.get_available_oil()} barrels")
print(f"Storage at station: {station.get_storage_status()} barrels")

