class User():

    def __init__(self, first_name, last_name, gender, age, country):
        self.nombre = first_name
        self.apellido = last_name
        self.sexo = gender
        self.edad = age
        self.pais = country
        self.login_attempts = 0

    def describe_user (self):
        prompt = "Síntesis de la user's information:\n"
        print (prompt) 
        print (self.nombre)
        print (self.apellido)
        print (self.sexo)
        print (self.edad)
        print (self.pais)
      
    def increment_login_attempts (self): 
        self.login_attempts += 1

    def reset_login_attempts (self):
        self.login_attempts = 0

    def greet_user(self):
        print ("Bienvenido", self.nombre, self.apellido)


class Privileges ():

    def __init__(self):
        self.privileges = ["sudo", "can ban users", "can edit post"]

    def show_privileges (self):
        print ("Privileges: ", self.privileges)

class Admin (User):

    def __init__(self, first_name, last_name, gender, age, country):
        super().__init__(first_name, last_name, gender, age, country)
        self.attributes = Privileges()

usuario2 = User ("Pedro", "Pettinati", "hombre", 3, "Argentina")
usuario3 = User ("Felipe", "Pettinati", "hombre", 5, "Argentina")
usuario4 = User ("Sole", "Villafañe", "Mujer", 35, "Argentina")

administrador = Admin ("Mariano", "Pettinati", "hombre", 39, "Argentina")

administrador.greet_user()
#administrador.describe_user()
administrador.attributes.show_privileges()
#print (type(administrador).__name__)
