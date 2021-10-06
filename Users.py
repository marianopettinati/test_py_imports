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
