import Restaurant

resto1 = Restaurant.Restaurant("La Vicente López", "mediterránea")
resto2 = Restaurant.Restaurant ("La Fugazza Loca", "pizzería")
resto3 = Restaurant.Restaurant ("Mucho gaita", "española")

print (resto1.nombre_del_restaurant, resto1.tipo_de_cocina)
print (resto2.nombre_del_restaurant, resto2.tipo_de_cocina)
print (resto3.nombre_del_restaurant, resto3.tipo_de_cocina)

print ('\n---\n')

resto1.describe_restaurant()
resto2.describe_restaurant()
resto3.describe_restaurant()