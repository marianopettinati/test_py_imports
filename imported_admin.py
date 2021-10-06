from admin_privileges import Admin

mariano = Admin("Mariano", "Pettinati", "masculino", 39, "Argentina")
mariano.greet_user()
mariano.attributes.show_privileges()