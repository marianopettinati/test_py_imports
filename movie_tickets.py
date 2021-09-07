prompt = "Por favor, indique su edad:\n"
prompt += '"Q" = quit\n'

active = True

while active:
    edad = input(prompt)
    if edad == "q": active = False
    else:
        if edad.isnumeric():
            if int(edad) <3: print('\nLos menores de tres años no pagan\n')
            elif 3<= int(edad) <12: print ('\nEl valor de la entrada es $10\n')
            elif int(edad) >=12: print ('\nEl valor de la entrada es $15\n')
        else: print('\nvalue error\n')
    
print ('\ngracias, vuelvas prontos')
