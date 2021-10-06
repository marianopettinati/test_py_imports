class Car():
    """A simple attemp to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.marca = make
        self.modelo = model
        self.año = year
        self.odometro = 0

    def get_descriptive_name(self):
        """Return a neatly formatted name."""
        nombre_completo = str(self.año) + ' ' + self.marca + ' ' + self.modelo
        return nombre_completo.title()

    def read_odometer (self):
        """Prints a statement showing the car mileage"""
        print ("Este auto tiene " + str(self.odometro) + ' kms')
    
    def update_odometer(self, kms):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if kms >= self.odometro:
            self.odometro = kms
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, kms):
        """Add the given amount to the odometer reading."""
        self.odometro += kms

class Battery ():
    """A simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size = 70):
        """Initialize th battery's attributes"""
        self.battery_size = battery_size

    def describe_battery (self):
        """Print a statement describing the battery size"""
        print ("This car has a " + str(self.battery_size) + "-kWh battery.")

    def upgrade_battery (self):
        """Checks the battery size and sets the capacity to 85"""
        if self.battery_size != 85: self.battery_size =85

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """Represents the aspects of a car specific to electric vehicles"""
    def __init__(self, make, model, year):
        """Initializes the attributes of the parent class.
        Then initializes the attributes specific to an electric car"""
        super().__init__(make, model, year)
        self.battery = Battery ()