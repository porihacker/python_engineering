class Car:
    def __init__(
        this, name, year, model, color="black"
    ):  # Color parameter has default value will be optional

        this.name = name  # this.name is attribute setting to name parameter
        this.year = year  # this.year is attribute setting to year parameter
        this.model = model  # this.model is attribute setting to model parameter
        this.color = color  # this.color is attribute setting to color parameter
        this.speed = 0  # this.name is attribute setting to 0 , which is default

    def accelerate(this, increase):
        this.speed += increase  # this.speed refers to the speed attribute of THIS specific car instance

    def __str__(this):
        return f" {this.name} {this.year} {this.model} {this.model} {this.speed}"


car1 = Car("AUDI", "2025", "RS4", "CREME WHITE")  # in these case *this*  is car1
car1.accelerate(320)
print(car1)
