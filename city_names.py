def city_country(city, country):
    print (city.title() +', '+ country.title())
    

#diccionario de capitales y países para el loop
capitales = {
    "Santiago" : "Chile",
    "Buenos Aires" : "Argentina",
    "Montevideo" : "Uruguay",
    }
    
for key, value in capitales.items():
    city_country(key, value)
