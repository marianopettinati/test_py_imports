height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

base = len(height) - 1
container_posibilities = []
for h in height:
    if h < height[-1]: altura = h
    if h > height [-1]: altura = height[-1]
    container = base* altura
    base -= 1
    container_posibilities.append(container)

maximo = (max(container_posibilities))
print ("Vertical nro (i): ", container_posibilities.index(maximo)+ 1)
print ("Valor de la vertical (ai): ", height[container_posibilities.index(maximo)])
