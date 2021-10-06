from Users import User


from Users import User

class Privileges ():

    def __init__(self):
        self.privileges = ["sudo", "can ban users", "can edit post"]

    def show_privileges (self):
        print ("Privileges: ", self.privileges)

class Admin (User):

    def __init__(self, first_name, last_name, gender, age, country):
        super().__init__(first_name, last_name, gender, age, country)
        self.attributes = Privileges()