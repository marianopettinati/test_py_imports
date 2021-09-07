def mascotas(nombre, dueño):
    """Displays info sobre mascotas"""
    print(nombre.title(), 'es la mascota de ', dueño.title())
     

dicc_mascotas = {
    "mariano" : "Rulo",
    "juan" : "chispita",
    "marcos" : "uri",
    "fernando" : "tortu", 
    }
    
for key, value in dicc_mascotas.items():
    mascotas(value, key)
    

    
