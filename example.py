class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def get_brand(self):
        return self.brand
    def set_brand(self, name):
        self.brand = name
    def get_model(self):
        return self.model
    def set_model(self, name2):
        self.model = name2
carObj = Car("Honda", "Civic")
carObj.set_brand("Toyota")
carObj.set_model("Corolla")

print(carObj.get_brand())
print(carObj.get_model())


        