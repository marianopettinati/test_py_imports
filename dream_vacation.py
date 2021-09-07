#presentación
print ('Encuesta de viaje\nEn cualquier momento, presione Q para salir\n')

dicc_destinos={}
active = True

while active:
    usuario = input ('Nombre de usuario: ')
    if usuario.lower() != 'q':
        destino = input ('Destino favorito: ')
        if destino.lower() != 'q': 
            dicc_destinos[usuario] = destino
            print ('\n')
        else: active = False
    else: active = False
    
print ('--- Resultados ---')
for key, value in dicc_destinos.items():
    print ('El destino favorito de', key, 'es', value, '\n')
    
    
