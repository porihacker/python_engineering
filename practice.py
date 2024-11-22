class Car:
    def __init__(self, name, year, model):
        self.name = name
        self.year = year
        self.model = model
        self.mileage = 0

    def __repr__(self):
        return f"Name : {self.name} Year: {self.year} model: {self.model} Mileage: {self.mileage}"


car1 = Car("BMW", "2010", "325")
car1.name = "Mercedes"
print(car1)
