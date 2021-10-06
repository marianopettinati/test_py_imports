import datetime

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()

# print(pi_string [:4])
# print (len(pi_string))

fecha = datetime.date(2020,1,1)
hoy = datetime.date.today()

active = True
cumples_en_pi = 0
cumples_no_en_pi = 0
while active:
    if fecha != hoy:
        if fecha.strftime("%Y%m%d") in pi_string: 
            cumples_en_pi +=1
        else: 
            cumples_no_en_pi +=1
        fecha +=  datetime.timedelta(days=1)
    else:
        print("cumples en Pi:", cumples_en_pi)
        print("Cumples no en Pi: ", cumples_no_en_pi)
        active = False

casos_testeados = cumples_no_en_pi +cumples_en_pi
print("Casos testeados:", casos_testeados)
print ('Equivalentes a: ', casos_testeados//365, 'años y',casos_testeados%365, 'dias')