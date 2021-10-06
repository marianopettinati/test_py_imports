from random import randint

class Die ():
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
     #   print ('Este dado tiene', self.sides, 'caras')
        x = randint (1,self.sides)
        return  (x)

    def muchos_tiros(self):
        tiros = 1
        while tiros <= self.sides:
            #print ("tiro nro", tiros)
            print (self.roll_die(),end= " ")
            tiros += 1
        #print ('\n')



dado1 = Die()
dado2 = Die(10)
dado3 = Die(20)

print ('\nUNO:')
dado1.muchos_tiros()
print ('\nDOS:')
dado2.muchos_tiros()
print ('\nTRES:')
dado3.muchos_tiros()