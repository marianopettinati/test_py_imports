sandwich_orders=[
    'BLT',
    'tostado mixto', 
    'pastrami',
    'pastrami',
    'crudo y queso', 
    'jamón y huevo',
    'pastrami'
    ]

finished_sandwiches = []
print ('Nos quedamos sin pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich == 'pastrami':
        continue
    else:
        print ('Sandwich', sandwich, 'listo')
        finished_sandwiches.append(sandwich)

print('\nSe hicieron todos los sandwiches')

print ('\n', sandwich_orders)
print (finished_sandwiches)
