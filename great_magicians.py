def show_magicians(magos):
    for mago in magos: print (mago)

def make_great(magos):
    for i in range (len(magos)):
        magos[i] = "El gran "  + magos[i]
    print(magos)


    
magos = ["Mandrake", "Merlín", "David Coperfield", "Mago Enmascarado"]
make_great (magos)
show_magicians (magos)

