def show_magicians(magos):
    for mago in magos: print (mago)

def make_great(magos):
    for i in range (len(magos)):
        magos[i] = "El gran "  + magos[i]
    return magos
    
    


    
magos = ["Mandrake", "Merlín", "David Coperfield", "Mago Enmascarado"]
new_magos = make_great (magos [:])
print(new_magos)
show_magicians (magos)


