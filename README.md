# test_py_imports
Test de módulo e importación en Python



#/home/mariano
def make_car(marca, modelo, **car_info):
    """Construye un diccionario con información acerca de un auto"""

    car ={}
    car["Marca"] = marca
    car["Modelo"] = modelo

    for key, value in car_info.items():
        car[key] = value


#/home/mariano
import cars

miauto = car.make_cars("VW", "gol", color = "rojo", motor = "naftero")
print (miauto)


import sys

type(sys.path)

for path in sys.path:
    print (path)

#>>>
/home/mariano
/usr/lib/python38.zip
/usr/lib/python3.8
/usr/lib/python3.8/lib-dynload
/usr/local/lib/python3.8/dist-packages
/usr/lib/python3/dist-packages
/usr/lib/python3.8/dist-packages

