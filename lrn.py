class Chair:
    def __init__(self, brand, model, name):
        self.brand = brand
        self.model = model
        self.name = name

    def get_brand(self):
        return self.brand
    def set_brand(self, brand1):
        self.brand = brand1

    def get_model(self):
        return self.model
    def set_model(self, model1):
        self.model = model1

    def get_name(self):
        return self.name
    def set_name(self, name1):
        self.name = name1

chairobj = Chair("Jokajok", "slight", "slighty")

chairobj.set_brand("Fumbeh")
chairobj.set_model("panda")
chairobj.set_name("bamboo")

print(chairobj.get_brand())
print(chairobj.get_model())
print(chairobj.get_name())

