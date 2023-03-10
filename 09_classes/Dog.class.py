

class Dog():
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name   = name
        self.age    = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")



mydog = Dog('willie', 6)

print("My dog's name is " + mydog.name.title() + ".")
print("My dog is " + str(mydog.age) + " years old.")
print('-----------------------')
mydog.sit()
mydog.roll_over()



