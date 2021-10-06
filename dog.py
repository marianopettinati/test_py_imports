class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sit(self):
        """simulates a dog sitting in response to a command."""
        print (self.name.title() + " is now sitting.")
        
    def roll_over(self):
        """simulates a dog rolling over in response to a command."""
        print (self.name.title() + " rolled over!")

my_dog = Dog("Rulo", 9)
print (my_dog.name.title(), "tiene", str(my_dog.age), "años.")