def sandwiches(*ingredientes):
    nuestro_sandwich =[]
    for ingrediente in ingredientes:
        nuestro_sandwich.append(ingrediente)
    print(nuestro_sandwich)
    
def tomar_pedido():
    active = True
    print( "Presione 'q' en cualquier momento para salir\n")
    n= 1
    ingredientes = []
    
    while active:
        prompt = ('Ingrediente ' + str(n) + ': ')
        ingrediente = input(prompt)
        n+= 1
        if ingrediente == "q": active = False
        else: ingredientes.append(ingrediente)

    return ingredientes




sandwiches (tomar_pedido())

