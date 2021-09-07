import sys

def make_car(marca, modelo, **car_info):
    """Construye un diccionario con información acerca de un auto"""

    car ={}
    car["Marca"] = marca
    car["Modelo"] = modelo

    for key, value in car_info.items():
        car[key] = value

    return car

mi_auto = make_car("VW", "gol", color = "blanco", motor = "naftero")
print (mi_auto, '\n')
print (sys.path)
