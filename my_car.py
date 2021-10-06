from car import Car

my_new_car = Car("audi", "a4", 2006)
print (my_new_car.get_descriptive_name())

my_new_car.odometro = 23
my_new_car.read_odometer()