class Restaurant():
    """Ejercicio de clases"""

    def __init__(self, restaurant_name, cuisine_type):
        self.nombre_del_restaurant = restaurant_name
        self.tipo_de_cocina  = cuisine_type
        self.mesas_servidas = 0

    def describe_restaurant (self):
        print("Este resto se llama " + self.nombre_del_restaurant + " y sirve comida " + self.tipo_de_cocina)
        
    def open_restaurant(self):
        print(self.nombre_del_restaurant + ' está abierto.')

    def set_number_served (self, atendidos):
        self.mesas_servidas = atendidos
        print ("Ahora el número de mesas servidas se ha incrementado a: " + str(atendidos))

    def increment_number_served (self, incremento):
        if incremento >= 0: 
            self.mesas_servidas += incremento

class IceCreamStand (Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        sabores = ["chocolate", "sambayón", "ddl", "limon", "frutilla"]
        self.sabores = sabores

    def carta_de_sabores (self):
        print ("Nuestros gustos son:", self.sabores)

# resto = Restaurant("La Vicente López", "mediterránea")
# print (resto.nombre_del_restaurant)
# print (resto.tipo_de_cocina)
# print ('Mi restaurant favorito del barrio es', resto.nombre_del_restaurant, 'y sirve comida', resto.tipo_de_cocina)
# resto.open_restaurant()
# print ("la cantidad de mesas servidas es: ", resto.mesas_servidas)
# resto.set_number_served (10)
# resto.increment_number_served (5)
# print (resto.mesas_servidas)

heladeria = IceCreamStand("chungo", "heladería")
print (heladeria.nombre_del_restaurant)
print (heladeria.tipo_de_cocina)
heladeria.carta_de_sabores()
 
