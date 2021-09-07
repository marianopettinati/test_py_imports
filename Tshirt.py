def make_shirt(size = "M", color = "blanco"):
    output = "Se ha tomado el siguiente pedido:\n"
    output += "Remera talle " + size.upper() + "\nColor " + color.lower()
    print (output, '\n')
    
make_shirt()
make_shirt (size = "s", color = "azul")
make_shirt (color = "verde", size = "xl")
